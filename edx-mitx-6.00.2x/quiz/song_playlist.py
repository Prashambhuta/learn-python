#!/usr/bin/python3

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """
    songs_list = []
    avail_size = max_size
    first_song_size = songs[0][2]
    first_song_name = songs[0][0]
    if first_song_size <= avail_size:
        songs_list.append(first_song_name)
        avail_size -= first_song_size
    else:
        return []

    if len(songs) == 1:
        return songs_list

    flag = True
    while flag:
        temp = songs[1][0]
        current = max_size
        for song in songs[1:]:
            if song[0] not in songs_list:
                if song[2] <= current:
                    current = song[2]
                    temp = song[0]
            # else:
            #     continue
        if temp in songs_list:
            # print(songs_list)
            break

        if current <= avail_size:
            songs_list.append(temp)
            avail_size -= current
        else:
            flag = False
            # break

    print(songs_list)
    return songs_list

song_playlist([('z', 0.1, 0.1), ('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 1)

