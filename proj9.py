



import re, shutil, os, time

fi = open('fi.txt','a')
fi.write('07-04-1900, ff gghbhjbjh 09-09-2000')

fi.close()
dateRegex = re.compile(r'''^(.*?)       #all characters before date
((0|1)?\d)-                             #month
((0|1|2|3)?\d)-                         #day
((19|20)\d\d)                           #year
(.*?)$                                  #characters at the end
''',re.VERBOSE)                     

for AmericaFile in os.listdir('.'):
    x = dateRegex.search(AmericaFile)
    if x == None:
        continue
    beforePart = x.group(1)
    monthPart = x.group(2)
    dayPart = x.group(4)
    yearPart = x.group(6)
    lastPart = x.group(8)

    euroFile = beforePart + dayPart + '-' + monthPart + '-' + yearPart + lastPart
    
    actualPath = os.path.abspath('.')
    AmericaFile = os.path.join(actualPath,AmericaFile)
    euroFile = os.path.join(actualPath,euroFile)
    print(AmericaFile)
    print(euroFile)

    print('Renaming "%s" to "%s"...'%(AmericaFile,euroFile))
    time.sleep(3)
    shutil.move(AmericaFile,euroFile)       #this moves the Americafile to the eurofile
    print('%s successfully moved to %s'%(AmericaFile,euroFile))
