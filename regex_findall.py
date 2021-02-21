import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#get all the matches and returns a list like above
print(phoneRegex.findall('Call me 415-555-1101, or 555-8787 tomorrow'))

phoneRegex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#get all the matches and returns a list or a tuples for groups like above
print(phoneRegex1.findall('Call me 415-555-1101, or 555-8787 tomorrow'))


phoneRegex2 = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
#get all the matches and returns a list or a tuples for groups like above
print(phoneRegex2.findall('Call me 415-555-1101, or 555-8787 tomorrow'))

#get any numeric digit from 0 to 9
digitRegex = re.compile(r'\d')

#get any character not a numeric digit from 0 to 9
nonNumRegex = re.compile(r'\D')

#get any letter numeric or underscore character
numericRegex = re.compile(r'\w')

#get any non - letter numeric or underscore character
notRegex = re.compile(r'\W')

#get any space tab or newline character
numericRegex = re.compile(r'\s')


###
lyrics = '''12 Drummers Drumming, 11 Pipers Piping, 10 Lords a Leaping,
9 Ladies Dancing, 8 Maids a Milking, 7 Swans a Swimming,6 Geese a Laying,
5 Golden Rings, 4 Calling Birds, 3 French Hens, 2Turtle Doves, and 1 Partridge in a Pear Tree'''

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

charolRegex = re.compile(r'\d+\s\w+\s\w+')
print(charolRegex.findall(lyrics))

###
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocops eats baby food'))

doubleRegex = re.compile(r'[aeiouAEIOU][2]')
print(doubleRegex.findall('Robocops eats baby food'))

### do the opposite (^)
notvowelRegex = re.compile(r'[^aeiouAEIOU]')
print(notvowelRegex.findall('Robocops eats baby food'))