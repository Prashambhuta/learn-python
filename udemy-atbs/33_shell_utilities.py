import os
import send2trash
import shutil

os.chdir('/home/prasham')
print(os.getcwd())
print(os.listdir())
send2trash.send2trash('waste.txt')

