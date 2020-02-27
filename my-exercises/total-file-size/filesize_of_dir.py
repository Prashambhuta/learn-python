"""
Example: Create a program that returns a list of individual sizes of the
directory and files and also the total of the directory.
"""

import os

# create a list that stores all the totals.

FILESIZE = 0

os.chdir('/home/prasham/learn-python/')

# create a loop that calculates the size of files in a directory and
#  returns the total.

# for files in os.listdir(os.getcwd()):
#     FILESIZE["name"] = files
#     if os.path.isdir(os.path.join(os.getcwd(), files)):
#         for more_files in os.listdir(os.path.join(os.getcwd(), files)):
#             # print(more_files)
#             FILESIZE["size"] = sum(range(os.path.getsize(os.path.join(
#                 os.getcwd() +
#                 '/' +
#                 files,
#                 more_files))))
#
#         print(FILESIZE)

# Try using os.walk
for folder_name, sub_folder, filename in os.walk(os.getcwd()):
    for files in filename:
        filepath = os.path.join(folder_name, files)
        FILESIZE += os.path.getsize(filepath)
        #FILESIZE += os.path.getsize(os.path.join(os.getcwd(), files))
print(FILESIZE)
# append the total to the size list and add all the entries to
#  calculate the grand total.
# FILESIZE["name"] = "TOTAL DIR"
# FILESIZE["size"] = sum(range(FILESIZE["size"]))
# print(FILESIZE)

