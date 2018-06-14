import sys
import os

def offset_audioscrobbler_line(scrobble, offset):
    scrobble_parts = scrobble.split("\t")
    time = int(scrobble_parts[-2])
    scrobble_parts[-2] = str(time + offset)

    return "\t".join(scrobble_parts)

scrobble_file = open(sys.argv[1], 'r' )
output_file = open(sys.argv[1] + "_corrected", 'w' )
offset = int(sys.argv[2])

for scrobble in scrobble_file:
    if scrobble[0] != "#":
        output_file.write(offset_audioscrobbler_line(scrobble, offset))
    else:
        output_file.write(scrobble)

output_file.close()
scrobble_file.close()



