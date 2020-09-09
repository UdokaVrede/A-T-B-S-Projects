# #This is a phone number and email extractor program that scans through a text and returns the phone numbers and emails in the text.
# #Steps followed:
# 1. get the text from the clipboard using pyperclip module
# 2. findall matches in the text,create 2 regex,format nicely
# 3. paste onto clipboard, display some message if none is found.

#Note: to use this code, before running the program, copy a text containing emails and address or any other text

import re, pyperclip
#phone number regex
phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?          #area code...digits
        (\s|-|\.)?                  #space,newline or tab, seperator and .(this would match either a space,newline,tab,-,or .)
        (\d{3})                       #digits
        (\s|-|\.)
        (\d{4})
        (\s*(ext|x|ext.)\s*)?
        (\d{2,5})?
        )''', re.VERBOSE)

#email regex
emailRegex = re.compile(r'''([a-zA-Z0-9.%+-]+
            @
            [a-zA-Z0-9.-]+
            (\.[a-zA-Z]{2,4})
            )''',re.VERBOSE)

#find matches in the clipboard
text = str(pyperclip.paste())       #pastes the copied value into the text variable
matched_values= []
for nums in phoneRegex.findall(text):   #iterates through the values pasted in text and finds all matching patterns to the phoneRegex
    phoneNum = '-'.join([nums[1],nums[3],nums[5]])  #joins the values in groups 1(the area code),3,5 to phoneNum
    if nums[8]!= '':                        #checks that group 8 is not empty
        phoneNum += 'x' + nums[8]       #adds group 8 to phoneNum
    matched_values.append(phoneNum)     #appends phoneNum to the empty list 'matched_values'
for mails in emailRegex.findall(text):  
    matched_values.append(mails[0])     #appends mails to matched_values, note that groups(0) returns the whole matched value, this is the same as mails[0] in this code
    print(matched_values)

#copy results to the clipboard
if len(matched_values) > 0:             #checks for that length matched_values is > 0
    pyperclip.copy('\n'.join(matched_values))   #joins with newline and copies the values in matched_values to the clipboard
    print('copied to clipboard:')
    print('\n'.join(matched_values))
else:
    print('No matches found')

