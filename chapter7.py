import re #import regex functions in re module

#REGULAR EXPRESSION METHODS
#1. THE SEARCH METHOD RETURNS ONLY A SINGLE OCCURRENCE OF A MATCHING PATTERN
try:
    #d:digits,extra (\ before and after the rawstring in the 1st column used to escape the ()
    #numRegex: returned Regex object from raw string gotten from marking the strings '\d\d' with r' passed to re.compile() function
    numRegex=re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
    #numba: match object returned from the method .search() on the regex object
    numba = numRegex.search('(222)-222-2222')
    #.groups() or group(0) returns the matching groups of text
    #numba.groups() returns tuple of values 
    #assigning the values in group(1)&group(2) to first and second 
    first,second = numba.groups()
    print(first)
    print(second)
except AttributeError:
    print('Incorrect')

#using pipe | for matching the 1st occurrence one of many expressions 
try:
    textRegex = re.compile(r'Raphael|Noriode')
    #search the 1st occurrence of any of the match object Raphael
    Text = textRegex.search('The love of my life is Raphael Noriode')
    tExt= Text.group()
    print(tExt)
 
except AttributeError:
    print('What was that')

#using pipe | to match patterns
try:
    patRegex = re.compile(r'Anti(pate|cipate|girn)')
    patMatch = patRegex.search('Antiate Anticipate')
    #display the whole matched 1st occurrence from the match object
    patText=patMatch.group()
    #return the suffix of the 1st occurrence
    patText1=patMatch.group(1)
    print(patText)
    print(patText1)
except AttributeError:
    print('Check the code')


#using \ to escape pipe | character 
try:
    patRegex = re.compile(r'Anti(pate|\|cipate|girn)')
    patMatch = patRegex.search('Antiate Anti|cipate')
    #display the whole matched 1st occurrence from the match object
    patText=patMatch.group()
    #return the suffix of the 1st occurrence
    patText1=patMatch.group(1)
    print(patText)
    print(patText1)
except AttributeError:
    print('Check the code')
    
#using question mark ? to optionally match patterns
try:
    #(cip)?  allows for return a match if it exists or not
    patRegex = re.compile(r'Anti(cip)?ate')
    patMatch = patRegex.search('Antiate Antipate')
    patMatch2 = patRegex.search('Anticipate Antiate')
    #display the whole matched 1st occurrence from the match object
    patText=patMatch.group()
    #return the suffix of the 1st occurrence
    patText2 = patMatch2.group()
    print(patText)
    print(patText2)
except AttributeError:
    print('Check the code')
    
#using * to get 0 or more matching optional patterns
try:
    #me: optional string passed in to re.compile function
    starRegex=re.compile(r'so(me)*times')
    starMatchsearch=starRegex.search('so there are seems hard and confusing somememetimes are')
    starMatchsearch2=starRegex.search('times when sotimes life ')
    starReturn=starMatchsearch.group()
    starReturn2=starMatchsearch2.group()
    print(starReturn)
    print(starReturn2)
except AttributeError:
    print('There\'s an error ')

#using + in matching atleast one occurrence of the optional pattern
try:
    plusRegex=re.compile(r'Anti(cip)+ate')
    plusMatchSearch1=plusRegex.search('Anticipcipate')
    plusMatchSearch2=plusRegex.search('Anticipate')
    plusReturn=plusMatchSearch1.group()
    plusReturn2=plusMatchSearch2.group()
    print(plusReturn)
    print(plusReturn2)
except AttributeError:
    print('Check the error please')

#using {} to match a specific ocurrence of a pattern
#{1,2} matches 1-2 occurrences,{,4}matches 0-4 occurrences, {1,} matches 1 and more occurrences
#{1,4} where there up to 4 occurrences, the highest occurrence, 4 would be returned
try:
    bracketRegex=re.compile(r'(\d){2,3}')
    bracketMatchSearch=bracketRegex.search('re2j122ern')
    bracketReturn=bracketMatchSearch.group()
    print(bracketReturn)
except AttributeError:
    print('Seems something is wrong')

#using {} and ? to match the 1st least occurrence of a pattern
try:
    bracketRegex=re.compile(r'(\d){2,3}?')
    bracketMatchSearch=bracketRegex.search('re2j122ern')
    bracketReturn=bracketMatchSearch.group()
    print(bracketReturn)
except AttributeError:
    print('Seems something is wrong')

#2. THE FINDALL METHOD RETURNS ALL OCCURRENCES OF THE MATCHING PATTERNS
#The .findall() method doesn't use the .group() method but returns a list of matching patterns
try:
    findAllRegex=re.compile(r'Raphael')
    findSearch=findAll.findAllRegex('All my life, Raphael has been my way, Raphael my love, Raphael my guy')
    print(findSearch)
except:
    print('There should be an error')

#using .findall() in grouped patterns
#when used on grouped patterns it returns a list of the groups and doesn't use group
try:
    numRegex=re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
    numba = numRegex.findall('(222)-222-2222 (132)-444-4444')
    print(numba)
except AttributeError:
    print('Incorrect')

#> CHARACTER CLASSES USED IN REGULAR EXPRESSIONS
# \d: numbers
# \D: characters that are non-digits
# \w: letter, digits & underscore characters (word character)
# \W: characters that are non-letters, digits or underscore
# \s: space,tab, newline character  (space character)
# \S: non-space,tab or newline character 

#using the \d \w \s in matching patterns
try:
    charRegex=re.compile(r'\d+\s\w+')
    charReturn=charRegex.findall('2 girls, 45 bras, 23 boys, 34cakes')
    #the last one didn't match cause of the absence of space in it
    print(charReturn)
except AttributeError:
    print('There is an error')


print('=================================================================================')
#DEFINING CUSTOMISED CLASSES IN REGULAR EXPRESSIONS USING []
try:
    #custom string jo.
    customRegex=re.compile(r'[jo]')
    #findall returns all matches of all occurrences of the letters j and o
    customReturn=customRegex.findall('my bae jo is a jojo bunch Jo of joyfulness')
    print(customReturn)
except AttributeError:
    print('something is wrong')

#using [] and - to create a class that specifies a range of characters or numbers
try:
    hyphenRegex=re.compile(r'[a-g]')
    hyphenReturn=hyphenRegex.findall('my bae jo is a jojo bunch Jo of joyfulness')
    print(hyphenReturn)
except AttributeError:
    print('Okay you have an error')

#using [] and ^ to create a negated class
try:
    #caret negating the string to give s-y as pattern/regex object passed in caretR
    caretRegex = re.compile(r'[^a-p]')
    caretReturn = caretRegex.findall('bambi is a very awesome zealous babe')
    print(caretReturn)
except AttributeError:
    print('Oh check back each line of code')

#using ^ to match strings that begins with same string pattern
#this would only match strings that begin with same strings as the regex object
try:
    startsWithRegex=re.compile(r'^Bambi')
    startsWith=startsWithRegex.findall('Bambi is a babe')
    print(startsWith)
except AttributeError:
    print('You have an error')

#using $ to match strings that ends with values same as the regex object
try:
    endsWithRegex = re.compile(r'\w$')
    endsWithReturn = endsWithRegex.findall('She is Udoka')
    print(endsWithReturn)
except AttributeError:
    print('Check the code please')

#combining ^ and $ to check matching strings that start and end with a regex object
#this matches when the whole string matches the regex object pattern
try:
    startEndRegex = re.compile(r'^\d+$')
    startEndReturn = startEndRegex.findall('14467898')
    print(startEndReturn)
except AttributeError:
    print('Oh that\'s an issue')

#using . to match only one character which is not a newline
try:
    dotRegex=re.compile(r'.at')
    dotReturn=dotRegex.findall('The 6at flat fat cat *at sat on the mat')
    print(dotReturn)
except AttributeError:
    print('Check for the error')

#using the .* any character
try:
    #this first searches for first name and last name then matches all characters after it
    dotStarRegex = re.compile(r'First Name:(.*) Last Name:(.*)')
    dotStarReturn = dotStarRegex.findall('First Name: UDOKA Last Name: UGOCHUKWU')
    print(dotStarReturn)
except AttributeError:
    print('Oh check your errors')

#using the . * and ? to match specific characters
try:
    #this would return all characters in the shortest <> only
    nonGreedyRegex = re.compile(r'<.*?>')
    nonGreedyReturn = nonGreedyRegex.search('<Python is awesome> for Data Science>')
    print(nonGreedyReturn.group())
except AttributeError:
    print('Check your code again')

#using the . * and re.DOTALL to match all characters including the newline
try:
    #this would return all characters including the newline
    reDotAllRegex = re.compile(r'.*',re.DOTALL)
    reDotAllReturn = reDotAllRegex.search('<Python is awesome> \n for Data Science>')
    print(reDotAllReturn.group())
except AttributeError:
    print('You might be missing something')


#using re.I to match all cases of a character
try:
    caseRegex = re.compile(r'God',re.I)
    caseReturn = caseRegex.findall('I have a very big GOD oh, who is always by My side a very big God oh by my sIde, by my Side')
    print(caseReturn)
except AttributeError:
    print('That\'s an error')

# THE .SUB() METHOD SUBSTITUTES PATTERNS IN A REGEX PATTERN WITH NEW VALUES AND RETURNS THE NEW  VALUE
#using sub() method to substitute patterns, the 1st is the regex pattern and the 2nd is the new pattern to be substituted with th regex pattern
try:
    #1st regex pattern, 'Outrage'
    substRegex = re.compile(r'burglar',re.I)
    #2nd regex pattern, 'thief' to substitute 'burglar' in the text passed into the .sub() method
    v = 'Yesterday a burglar, came to our office, the Burglar was caught'
    substReturn = substRegex.sub('Thief', v)
    print(substReturn)
except AttributeError:
    print('Okay, you should check your code again')

#using (\w)\w* and \1**** to censor character
#This substitutes the character in the regex pattern with an * and also the next 1 word with *
#If you choose to censor more than 1 word using the number followed by * substitutes the word
try:
    #1st regex pattern, "agent"
    censorRegex = re.compile(r'agent (\w)\w*')
    #2nd regex pattern, '\1***' also passed into rawstring,r to substitute 'agent' in the text passed into the .sub() method
    v = 'the murdered agents were agent thomas, agent victor, agent susanna and agent madpik'
    censorReturn = censorRegex.sub(r'\1****', v)
    print(censorReturn)
except AttributeError:
    print('Check your code')

#WORKING WITH COMPLEX REGEX 
#using re.verbose() to ignore comments, newline and whitespaces in a regex pattern
try:
    #the triple quote is used to create a multiline string to enable the regular expression to be spread to all other lines
# ''' The # symbol and everything after it to the end of the
# line are ignored. Also, the extra spaces inside the multiline string for the reg-
# ular expression are not considered part of the text pattern to be matched.
# This lets you organize the regular expression so it’s easier to read.'''
    
    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?          #area code...digits
        (\s|-|\.)?                  #space,newline or tab, seperator and .(this would match either a space,newline,tab,-,or .)
        \d{3}                       #digits
        (\s|-|\.)
        \d{4}
        (\s*(ext|x|ext.)\s*\d{2,5})?
        )''', re.VERBOSE)
    v=input('Enter the phone number: ')
    print((phoneRegex.search(v)).group())
    #this would return the actual phone number removing the country code

except AttributeError:
    print('OH DEAR YOUR CODE IS TRASH')

#using the | to pass more than one value to the re.compile() function
#the re.compile() function usually takes only one value alongside the pattern passed in the rawstring, r, so to be able to pass more than one value, you use the |
try:
    multiRegex=re.compile(r'bam',re.I|re.DOTALL|re.VERBOSE)
except AttributeError:
    print('Where is the bug?')