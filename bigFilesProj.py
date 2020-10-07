''''You can walk a directory tree and add files to compressed ZIP archives in
several other programs. For example, you can write programs that do the
following:
Walk a directory tree and archive just files with certain extensions, such
as .txt or .py, and nothing else
Walk a directory tree and archive every file except the .txt and .py ones
Find the folder in a directory tree that has the greatest number of files
or the folder that uses the most disk space'''

import zipfile,os
#File archiver for .txt and .py files
def archiveFiles(path):
    idx = 0
    for folders,subfolders,files in os.walk(path):
        for Afile in files:
            if Afile.endswith('.txt') or Afile.endswith('.py'):
                idx += 1
                zipfileName = os.path.basename(path)+ str(idx) +'.zip'
                archive = zipfile.ZipFile(zipfileName,'w')
                archive.write(os.path.join(folders,Afile),compress_type= zipfile.ZIP_DEFLATED)
    archive.close()
    return archive


path = os.path.abspath('.')
archiveFiles(path)




