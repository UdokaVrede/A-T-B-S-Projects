#READING AND WRITING TO FILES

# #make python scripts run on any environment(windows,linux,osx)
import os
#this would join usr,bin,spam with a /
print(os.path.join('usr','bin','spam'))

#os.path.join() function is helpful if you want to create strings for filenames like
myfiles = ['accounts.txt', 'peace.docx','bk.png','dsn.pdf']
#this would print each file's path
for afile in myfiles:
    print(os.path.join('~/Desktop/Peace/python',afile))

#CURRENT WORKING FOLDER OR DIRECTORY(cwd)
#getting the cwd using os.getcwd() function
print(os.getcwd())      #this returns the path of your cwd as a string
#changing the cwd using os.chdir() function
#note if you try changing to a directory that doesn't exist you would get a FileNotFoundError 
os.chdir('/home/udoka/Desktop')
print(os.getcwd())      #check the new cwd

#ABSOLUTE vs RELATIVE PATHS
# Absolute path begins with the root folder / e.g) /home
# Relative path is relative to the program cwd , it may or maynot use the ../ or ./ before the cwd
# Note: dot(.) is the short for the cwd dot-dot(..) is the short for the root/parent folder
# the ./ at the start of a relative path is optional.

#making directories with os.makedirs()
'''os.makedirs('/home/udoka/Ambit')        #makes a directory Ambit in the home/udoka path, if you check your system, you'd see this folder
os.chdir('/home/udoka/Ambit')
print(os.getcwd())'''

# #HANDLING ABSOLUTE AND RELATIVE PATHS
# The os.path module provides functions that check if a given path is an absolute path
# It also provides functions that return the bsolute path of a relative path.
#OS.PATH MODULE FUNCTIONS:-

#returning the absolute path of a relative (rel.) path using os.path.abspath('path')
print(os.path.abspath('./Ambit'))
#this returns the absolute (abs.) path, /home/udoka/Desktop/Ambit

#using os.path.abspath('.') to return the cwd
print(os.path.abspath('.'))
#this returns the cwd /home/udoka/Desktop

#using os.path.isabs('path') to check that path is an abs. path
print(os.path.isabs(os.path.abspath('./Ambit')))
#this returns a boolean value,'true',beacause the rel. path has been converted to an abs path by os.path.abspath('path')
print(os.path.isabs('.'))
#this returns false because the '.' which gives the cwd, is a relative path

#using os.path.relpath('abs. path', 'path to be made rel. path') to convert abs path to relpath
print(os.path.relpath('/home/udoka/Desktop','/home/udoka'))
#this returns a rel.path 'Desktop' which is same as ./Desktop

#returning a rel.path of the abs path using 2 different paths
print(os.path.relpath('/home/udoka/Desktop', '/home/udoka/Downloads/ludo'))
#this would return '../../Desktop'
print(os.path.abspath('../../Desktop'))
#/home/Desktop same as ../../Desktop

#using os.path.dirname('path') to return the dirname and os.path.basename('path') to return the filename
#Note the dirname is everyother thing asides the basename(filename)
path = '/home/udoka/Desktop/mum.jpg'
print(os.path.dirname(path))
#this returns the dirname of the path, /home/udoka/Desktop
print(os.path.basename(path))
#this returns the basename of the path, mum.jpg

#using os.path.split() to get a tuple of a path's dirname and basename
PATH = '/home/udoka/Desktop/moni/moni.py'
print(os.path.split(PATH))
#this would return a tuple, ('/home/udoka/Desktop/moni', 'moni.py')

#using .split() str method and os.path.sep() to seperate filepaths
sepPATH = '/home/udoka/Desktop/Peace/Doka/ISN.pdf'
print(sepPATH.split(os.path.sep))
#this returns a list containing each of the path seperated like this
# ['', 'home', 'udoka', 'Desktop', 'Peace', 'Doka', 'ISN.pdf']
# notice the blank space at the beginning his represents the root path '/'

#GETTING THE FILESIZE AND FILE FOLDER CONTENTS
#using the os.path module function os.path.getsize('path') to get the  file size
print(os.path.getsize('/home/udoka/Desktop/Peace/Doka/ISN.pdf'))
#this returns the file size, 7,823,461 bytes being the size of the ISN.pdf file

#using the os.listdir() to get the file folder contents
print(os.listdir('/home/udoka/Desktop'))
#the result of this would be a list of all folders in my Desktop
#Note: this doesn't have .path using os.path.listdir would result in an Attribute Error.

#using the os.path.getsize() and os.listdir() to get the totalsize of files in a directory
totalSize = 0
for filename in os.listdir('/home/udoka/Desktop'):       #filename iterates the list returned by the os.listdir() getting each filename
    myfile = os.path.getsize(os.path.join('/home/udoka/Desktop',filename))     #this joins the filename returned to the path to get the files path, then return its size to myfolder
    totalSize = totalSize + myfile      #adding each filesize up
    print(filename, myfile)     #this returns a tuple of each file and its size
print(totalSize)        #totalsize of all folders in the desktop

#CHECKING THE VALIDITY OF A PATH
#using the os.path.exists('path') to check that a file or folder exists.
V = '/home/udoka/Downloads/MYPROJECT/what.py'
print(os.path.exists(V)) #this returns true, if the file exists or false, if the file doesn't exist
#Note: this can be used to also check if an external drive exists.

#using the os.path.isfile('path') to check that a path is a file
print(os.path.isfile(V))

#using the os.path.isdir('path') to check that a path is a folder
print(os.path.isdir(V)) #this would be false cause the path in V is a file not a folder

#THE READING AND WRITING PROCESS
# Note: Plaintext files are files that contain basic text characters no fonts,size or color info., with ext. like .txt and .py 
# Binary files are all other file types like .exe,.png,.xsl, when opened it with a texteditor is meaningful

#Opening files with the open() function which returns a file object
myFile = open('/home/udoka/Desktop/myPracticeProjects/strip.py')
print(myFile)
#this opens the file in read mode, and you can only read its contents but cannot write or modify its contents
#to read the files outside pythons default add 'r' at the end of the path like:
thisFile = open('/home/udoka/Desktop/myPracticeProjects/strip.py','r')

#READING THE FILE CONTENT
#using the .read() method to read file content
print(thisFile.read())    #this returns the actual text/string content of the file opened and read

#using the .readlines() method to get a list of all the strings values in the opened file
print(myFile.readlines())
#notice I used myFile not thisFile cause readlines gives an empty list when 'r' is used after the file path to be opened
#this returns a list of all string content of the file, with the \n character where a newline occurred

# WRITING TO A FILE
# Inorder to write to a file, you would need to open it in a write (w) or append (a) mode not in a read mode
#then you call the .write() method on the variable where the file was opened
# pass the values to be writen to the file then close the file using the .close() method
X = '/home/udoka/Desktop/moni/buff.txt'
texts = 'I have been happy all day'
#Note: a new file can be created if none exists by:
open('NEWFILE.txt','w')
#opening the file in write mode with 'w', this erases the existing file contents for new content writing
Afile = open(X,'w')
Afile.write(texts)
Afile.close()       #to see the file content then read it
###############
Op = open(X,'r')
print(Op.read())        #this would show the file contents in X which was opened for writing as Afile

#opening a file in append mode for writing, this writes to the file without deleting existing contents
ApFile = open(X,'a')
ApFile.write(', Bob marley is a vibe')
ApFile.close()
#~~~~~~~~~~~~~~~~~~~
Op = open(X,'r')
print(Op.read())        #this is to show the file contents


#USING THE SHELVE MODULE TO ADD, SAVE AND OPEN FEATURES TO YOUR PROGRAM
#by the using the shelve module, variables data can be saved to the harddrive and reloaded back to the variable when the program is run next time.

import shelve       #importing the shelve module
shelfFile = shelve.open('myData')       #calling shelve.open() function with the flename to be created and/or opened and stored in the shelfFile variable
mice = ['Okon', 'Okafor', 'Derrick','Samson']   
shelfFile['cats'] = mice       #modifying the contents of the shelfFile like a dictionary
#note: the contents of a shelve variable (shelfFile) is modified as a dict. 
#This means that ['cats'] is the key and the contents of mice is stored as its values
shelfFile.close()       #after making modifications use the .close() method to close the file and save it's contents to the hard drive
#when this is done, check the cwd for a file with .db,.bak,.dir,or .dat extension 
# using the os.listdir() and os.getcwd() to see the file
print(os.listdir(os.getcwd()))
#you would see a myData.db file for linux, which is a binary file containing the values you added.

#RE-OPENING THE SHELF FILE TO VIEW ITS' CONTENT
#Note: you don't need to open shelve files in a read/write mode, once shelve.open() is called it does the both
shelfFile = shelve.open('myData')
#to see its data type, you can do type()
print(type(shelfFile))
#To see the contents of the file added earlier
print(shelfFile)        #this returns a dict.
print(shelfFile['cats'])        #just like with the dictionaries
#close the file
shelfFile.close()
