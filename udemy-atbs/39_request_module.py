#! usr/bin/env python3
import requests
res = requests.get('http://automatetheboringstuff.com/files/rj.txt')    #
# returns a Response Object

print(res.raise_for_status())   # Check status of 'res', returns None if
# successful

ROMEO_JULIET = open('39_romeo_and_juliet.txt', 'wb')   # Append 'res' to a
# local file. Use 'wb' to write in binary.

for chunks in res.iter_content(10000):  # Write binary in form of chunks.
    # Each chunk of 10000 unicode will be iterated and appended to the file
    # ROMEO_JULIET
    ROMEO_JULIET.write(chunks)

ROMEO_JULIET.close()
