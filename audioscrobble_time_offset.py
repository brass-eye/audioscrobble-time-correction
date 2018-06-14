def offset_audioscrobbler_line(scrobble, offset):
    scrobble_parts = scrobble.split("\t")
    time = int(scrobble_parts[-1])
    scrobble_parts[-1] = str(time + offset)

    return "\t".join(scrobble_parts)