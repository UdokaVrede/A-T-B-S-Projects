# #This is a phone number and email extractor program that scans through a text and returns the phone numbers and emails in the text.
# #Steps followed:
# 1. get the text from the clipboard using pyperclip module
# 2. findall matches in the text,create 2 regex,format nicely
# 3. paste onto clipboard, display some message if none is found.

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
text = str(pyperclip.paste())
matched_values= []
for nums in phoneRegex.findall(text):
    print(nums)
    phoneNum = '-'.join([nums[1],nums[3],nums[5]])
    if nums[8]!= '':
        print(nums[8])
        phoneNum += 'x' + nums[8]
    matched_values.append(phoneNum)
    print(phoneNum)
    print(matched_values)
for mails in emailRegex.findall(text):
    matched_values.append(mails[0])
    print(matched_values)

#copy results to the clipboard
if len(matched_values) > 0:
    pyperclip.copy('\n'.join(matched_values))
    print('copied to clipboard:')
    print('\n'.join(matched_values))
else:
    print('No matches found')

