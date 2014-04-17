#!/usr/bin/awk -f
BEGIN { OFS=" "; FS="[ ]"; print "{"; }
{
	print "{\n'timestamp':'" $1,$2,$3 "',";
	print "'user:'" $4 "',";
	print "'message:'" substr($0, index($0,$5)); 
}
END { print "}"; }
