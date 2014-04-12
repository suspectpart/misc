import sys
from struct import *
  
#http://robinhoksbergen.com/papers/howto_elf.html


code = """7F 45 4C 46 01 01 01 00 00 00 00 00 00 00 00 10 02 00 03 00
01 00 00 00 80 80 04 08 34 00 00 00 00 00 00 00 00 00 00 00
34 00 20 00 02 00 00 00 00 00 00 00 01 00 00 00 80 00 00 00
80 80 04 08 00 00 00 00 24 00 00 00 24 00 00 00 05 00 00 00
00 10 00 00 01 00 00 00 A4 00 00 00 A4 80 04 08 00 00 00 00
20 00 00 00 20 00 00 00 07 00 00 00 00 10 00 00 00 00 00 00
00 00 00 00 00 00 00 00 BB 01 00 00 00 B8 04 00 00 00 B9 A4
80 04 08 BA 0D 00 00 00 CD 80 B8 01 00 00 00 BB 2A 00 00 00
CD 80 00 00 48 65 6C 6C 6F 20 57 6F 72 6C 64 21 0A"""

bytes = bytearray([pack('B', int(byte, 16)) for byte in code.replace("\n", " ").split(" ")])

with open('elf', 'w+') as f:
  f.write(bytes) # don't forget to chmod 755 this file in order to run it!