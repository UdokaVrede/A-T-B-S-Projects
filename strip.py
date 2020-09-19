# Write a function that takes a string and does the same thing as the strip()
# string method.
# If no other arguments are passed other than the string to
# strip, then whitespace characters will be removed from the beginning and
# end of the string. Otherwise, the characters specified in the second argu-
# ment to the function will be removed from the string.

import re

def stringStrip(val):
    stringRegex=re.compile(r'''((^(\s*|\w*|\d*)$)?
                            (\w*\d*)''',re.VERBOSE)
    stringReturn=stringRegex.findall(val)
    return stringReturn

print(stringStrip(' hello gabby '))