# os module handles all operating system based functions
import os

# get current working directory, same as pwd.
print(os.getcwd())

# change directory
os.chdir('/home/prasham/learn-python')
print(os.getcwd())

# convert to absolute path
print(os.path.abspath('hello.py'))

# get relative path between two file paths.
print(os.path.relpath('/home/prasham/vocab/my-word.ods', ''))

# get directory name or filename from complete filepath.
print(os.path.dirname('/home/prasham/learn-python/udemy-atbs/30_filename_and_filepath.py'))
print(os.path.basename('/home/prasham/learn-python/udemy-atbs/30_filename_and_filepath.py'))

# to check if certain file exists in the directory
print(os.path.exists('/home/prasham'))
print(os.path.exists('/home/prasham-a'))

# get size of the directory
print(os.path.getsize('/home/prasham/learn-python/udemy-atbs/'))
'''.getsize only works on files and not on directory, so if ran on a 
directory it will return the default value of 4096. AS IN EXAMPLE'''

# get list of directory + files within a directory
print(os.listdir('/home/prasham/learn-python/udemy-atbs'))

'''
Example: Create a program that returns a total of individual sizes of the 
files, ignore the directories.
'''
# define a variable that will store the sum of size
total_size = 0

# iterate over files in listdir
os.chdir('/home/prasham/learn-python/udemy-atbs') # change working directory
for files in os.listdir(os.getcwd()):
    # check if the files is a file or a dir
    if os.path.isdir(os.path.join(os.getcwd(), files)):
        continue
    total_size = total_size + os.path.getsize(os.path.join(os.getcwd(), files))

print("%d KB" % (int(total_size) / 100))