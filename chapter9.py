# # '''ORGANIZING FILES
# # THE SHUTIL MODULE'''
# # '''Using the shutil.copy() module to copy files from and to different locations
# # the shutil.copy(source, destination)takes 2 args, the destination filename becomes the new name of the copied file'''
import shutil,os

# # print(shutil.copy('/home/udoka/Desktop/frees/frees.txt', '/home/udoka/Desktop/strip.txt'))
# # #the contents of the source file are moved to the destination file but the filename of the destinatin folder is used in place of source folder
# # #where a folder is the specified destination, the filename of the source file is used.

# # '''USING SHUTIL.COPYTREE()TO COPY A FOLDER AND ITS CONTENTS'''
# # print(shutil.copytree('/home/udoka/Desktop/frees','/home/udoka/Desktop/organs'))
# # #the shutil.copytree() also takes two args, but the destination folder should not be an already existing folder
# # #the shutil.copytree() creates the destination folder itself when executed

# '''USING THE SHUTIL.MOVE() TO TOTALLY CHANGE THE LOCATION OF THE CONTENTS A FILE OR A FOLDER TO ANOTHER DESTINATION
# when the destination file or folder having the same name already exists, its contents are overwritten by the contents of the source file or folder'''
# print(shutil.move('/home/udoka/Desktop/ppp.txt','/home/udoka/Desktop/organn'))
# #when the file or folder already exists in the destination, an error is encountered


'''DELETING FILES AND FOLDERS PERMANENTLY USING THESE:'''
#Using the os.unlink(path) to delete a file path
#print(os.unlink('/home/udoka/Desktop/strip (copy).txt'))
#where the file doesn't exist an error message would be shown

#using os.rmdir(path) to remove an empty folder
#this would not delete a folder with contents
#print(os.rmdir('/home/udoka/Desktop/organn'))

#using shutil.rmtree to remove folder and all its contents
#print(shutil.rmtree('/home/udoka/Desktop/organn'))

#note while using these modules, it is a good practice to first, list all files and folders in the location, using the os.listdir() module, you want to perform the os.unlink(),os.rmdir() and the shutil.rmtree()
for files in os.listdir('/home/udoka/Desktop/'):
    if files.endswith('.rxt'):  
        #commenting this out before the initial run helps avoid deleting important files
        os.unlink('/home/udoka/Desktop/'+files)

'''SAFE DELETES WITH THE send2trash MODULE to safely delete files or folders, this sends files/folders to the trash but cannot be used to restore files/folders from trash
inorder to safelt delete files/folders use the send2trash.send2trash() function
else, you can use the os() and shutil() to delete permanently.'''
import send2trash
createFile = open('someFile.txt','a')
createFile.write('only some things should be told of these')
createFile.close()
send2trash.send2trash('someFile.txt')   #this sends the file to the trash bin

'''Walking through the files/folders in a path using the os.walk() function
The os.walk() returns  3 values on each iteration through the loop:
a string of the current folder's name, a list of strings of the folders in the current folder
 and a list of strings of the files in the current folders. 
'''
# for folderName, subfolder, fileName in os.walk('/home/udoka/Desktop'):
#     print('the current folder is' + folderName)
#     print(subfolder)
#     print(fileName)
    # for sub in subfolder:
    #     print('the current subfolder =' + sub)
    # for theFile in fileName:
    #     print('the file inside is =' + folderName + theFile)
    # print('\n')

'''COMPRESSING, OPEN or EXTRACT FILE WITH THE ZIPFILE MODULE'''
#READING FILE CONTENTS OF A ZIP FILE
#inorder to read the contents of a Zip file, a ZipFile object
#must be first created using the zipfile.ZipFile()function
# and passing in a string  
import zipfile
# os.chdir('/home/udoka/Desktop/Peace/looklearncode')
# testFile = zipfile.ZipFile('ok.zip')    #this opens the ok.zip file into the testFile
# print(testFile.namelist())      #this returns a list of strings of all contents of the zip file

#CHECKING THE SIZE OF A ZIPFILE USING .getinfo() and the .file_size
#.getinfo() method takes one args which is a file in the zipfile
#Diva = testFile.getinfo('recovery-key.txt')     #this returns a zipinfo object about the file
#the zipinfo objects(which holds info about a single file in the archive) have the file_size and compress_size attributes in bytes
# print(Diva.file_size)

#COMPRESSING THE FILE CONTENTS
#print(Diva.compress_size)

#let's see to what % the file has been reduced
# print('the file has been reduced by %sx ' %(round(Diva.file_size / Diva.compress_size, 1)))
# testFile.close()

#EXTRACTING FROM ZIP FILES USING .extractall() 
# os.chdir('/home/udoka/Desktop/')
# extFile = zipfile.ZipFile('top.zip')
# extFile.extractall()     #this extracts all the contents of the .zip file to the location where the zip file is.
#you can also specify the folder for the extraction files
# extFile.extractall('/home/udoka/Desktop/mine')       #and all files would be extracted to the specified path

#EXTRACTING A SINGLE FILE USING .extract() method
#this method can take one or two args, where it takes two args the first
#is the file to be extracted while the next is the location to extract the files
# extFile.extract('README.md','/home/udoka/Desktop/under')
#else it takes just the file to be extracted.
# extFile.extract('README.md')
#also if the folder where the file is to be extracted doesn't exist it is 
#automatically created.

'''
CREATING AND ADDING TO ZIP FILES
to create a zip file, you open aa ZipFile object in write mode
then write the file to be to compressed, just like with the open() function
followed by the compress type parameter letting the pc know the algorithm to be used
The ZIP_DEFLATED works on file types '''
os.chdir('/home/udoka/Desktop')
myZip = zipfile.ZipFile('myZipFile.zip','w')
myZip.write('tobe.txt', compress_type = zipfile.ZIP_DEFLATED)
myZip.close()


