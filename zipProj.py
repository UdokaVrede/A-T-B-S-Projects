'''Say you’re working on a project whose files you keep in a folder named
C:\AlsPythonBook. You’re worried about losing your work, so you’d like
to ­create ZIP file “snapshots” of the entire folder. You’d like to keep dif-
ferent versions, so you want the ZIP file’s filename to increment each
time it is made; 
for example, AlsPythonBook_1.zip, AlsPythonBook_2.zip,
Organizing Files AlsPythonBook_3.zip, and so on. You could do this by hand, but it is rather
annoying, and you might accidentally misnumber the ZIP files’ names. It
would be much simpler to run a program that does this boring task for you'''

import zipfile, os, time  #import modules
def zipBackup():    #function definition    

    folder = os.path.abspath('.')   #asssign the current path to folder
    num = 1                     #initialize num for file name differentation later

    while True:             #do while condition is true
        
        zipfileName = os.path.basename(folder) + ('_' + str(num) + '.zip')      #create new zipfile 
        print(os.path.exists(zipfileName))
        if not os.path.exists(zipfileName):         #checks that the file path doesn't exist then break out of the loop, this helps your program quit after the first execution is done
            break

        num+=1          #initiate an incremental variable 
        print('Creating %s...'%(zipfileName))       #display to screen the created zipfile

    backup = zipfile.ZipFile(zipfileName,'w')       #create the zipfile object i write mode and assign to the backup variable
    for folders, subfolders, files in os.walk(folder):      #walk through the contents of the file path
        print('Adding files in %s...' %(folders))           #display the contents of the folder
        backup.write(folders)               #write to the zipile object created

        for allfiles in files:          #loop throught he list of files
            newbase = os.path.basename(folder)+'_'          #get the base name of each file and add an underscore 

            if allfiles.startswith(newbase) and allfiles.endswith('.zip'):      #ignore files that start with the values in newbase and end with zip
                continue
            
            backup.write(os.path.join(folders, allfiles))           #write the folders and the files to backup
    backup.close()      #close the zipfile
    print('Done.')      #output done
zipBackup()