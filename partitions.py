import exceptions
import sys

def main():
    #PhysicalDrive0
    partitionTable = MasterBootRecord("PhysicalDrive0").partitionTable()
    partitions = partitionTable.getPartitions()

    for partition in partitions:
        print "---- Partition -----"

        print "Type:\t\t" + partition.getType() + " (" + ("primary" if partition.isPrimary() else "extended") + ")"
        print "Boot partition: " + str("yes" if partition.isBootable() else "no")
        print "Total sectors:\t" + str(partition.numberOfSectors())
        print "First sector:\t" + partition.firstSector().toString()
        print "Last sector:\t" + partition.lastSector().toString()
        #print "total bytes: " + str(partition.getBytes())
        print "Size in MiB:\t" + str(partition.size())
        print "\n"

    if (len(sys.argv) > 1 and sys.argv[1] == "-h"):
        print "Help!"

def readBytesFromFile(file, offset, length):
    movePointer(file, offset)
    return [ord(x) for x in file.read(length)]

def movePointer(drive, bytes):
    drive.read(bytes)

class MasterBootRecord(object):
    def __init__(self, physicalDrive):
        drive = file(r"\\.\\" + physicalDrive, "rb")
        masterBootSector = bytearray(readBytesFromFile(drive, 0, 512))
        self.__partitionTable = PartitionTable(masterBootSector[446:511])

    def partitionTable(self):
        return self.__partitionTable

class Partition(object):
    __bootable = 0x80
    __types = dict([
                    (0x00, 'leer/unbenutzt'),
                    (0x01, 'FAT12 (Floppy Disks)'),
                    (0x04, 'FAT16 = 32 MiB'),
                    (0x05, 'erweiterte Partition'),
                    (0x06, 'FAT16 > 32 MiB'),
                    (0x07, 'NTFS (Windows NT/2000/XP/Vista/7) oder HPFS (OS/2)'),
                    (0x0B, 'FAT32'),
                    (0x0C, 'FAT32 mit BIOS-Extensions (LBA)'),
                    (0x0E, 'FAT16 > 32 MiB mit BIOS-Extensions (LBA)'),
                    (0x0F, 'erweiterte Partition mit BIOS-Extensions (LBA)'),
                    (0x12, 'OEM Partition fuer Konfiguration, Diagnose, BIOS-Erweiterung (fuer Microsoft-Betriebssysteme unsichtbar)'),
                    (0x27, 'Windows RE versteckte Partition'),
                    (0x42, 'Dynamischer Datentraeger'),
                    (0x82, 'Linux Swap / Solaris 2.6 X86 bis Solaris 9 X86'),
                    (0x83, 'Linux Native'),
                    (0x8E, 'Linux LVM'),
                    (0xA5, 'FreeBSD'),
                    (0xA6, 'OpenBSD'),
                    (0xA9, 'NetBSD'),
                    (0xEE, 'Legacy MBR mit folgendem EFI-Header'),
                    (0xEF, 'EFI-Dateisystem'),
                ])

    def __init__(self, bytes):
        self.__bytes = bytes

    def getBytes(self):
        return toHexArray(self.__bytes)

    def isPrimary(self):
        return self.__getType() != 0x0F and self.__getType() != 0x05

    def isBootable(self):
        return self.__bytes[0] == Partition.__bootable

    def firstSector(self):
        return CHS(self.__bytes[1:4])

    def lastSector(self):
        return CHS(self.__bytes[5:8])

    def numberOfSectors(self):
        i1 = self.__bytes[15] << 24
        i2 = i1 | (self.__bytes[14] << 16)
        i3 = i2 | (self.__bytes[13] << 8)
        i4 = i3 | (self.__bytes[12])

        return  i4

    def size(self):
        return (self.numberOfSectors() * 512) / (1024 * 1024)

    def getType(self):
        return self.__types[self.__getType()]

    def __getType(self):
        return self.__bytes[4]


class PartitionTable(object):
    def __init__(self, bytes):
        self._bytes = bytes

    def getBytes(self):
        return toHexArray(self.__bytes)

    def getPartitions(self):
        entrySize = 16
        partitions = []
        for i in range(0, 4):
            offset = (entrySize * (i + 1)) - entrySize
            partitions.append(Partition(self._bytes[offset:(offset + entrySize)]))

        return partitions


class CHS(object):
    def __init__(self, bytes):
        self.__bytes = bytes

    def cylinder(self):
        return ((self.__bytes[1] & 0b11000000) << 2) + self.__bytes[2]

    def sector(self):
        return self.__bytes[1] & 0b00111111

    def head(self):
        return self.__bytes[0]

    def toString(self):
        return "Cylinder: " + str(self.cylinder()) + ", Head: " + str(self.head()) + ", Sector: " + str(self.sector())


def toHexArray(bytearray):
    return [hex(x) for x in list(bytearray)]

if __name__ == "__main__":
    main()
