import re

#this program does the same thing the third_exercise.py would do
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')           #r-gives the rawstring, of '\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d' and passes it to re.compile() that is passed into the variable'phoneNumRegex'

mo = phoneNumRegex.search('My number is 415-505-4242.')         #search checks for matching objects from the regex object,'phoneNumRegex' which the string is passed into
print('Phone number found: ' + mo.group())                      #grouping the match objects into a string
print('Phone number found: ',mo)            #output of the ungrouped match objects.


#grouping expressions
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  
mop = phoneNumRegex.search('My number is 415-505-4242.')          #search checks for matching objects from the regex object,'phoneNumRegex' which the string is passed into
print('Phone number found: ' + mop.group(2))
print(len(mop.group(2)))



#using shortcuts in defining regular expressions
phoneNumRegex = re.compile(r'(\d{1,2})-(\d{1,2}-\d{4})')  
my = phoneNumRegex.search('23-2-2000.')  
print('Phone number found: ' + my.group(0))

