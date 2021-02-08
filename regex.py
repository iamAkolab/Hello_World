import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('Call me 415-555-1101 tomorrow, or ')
print(mo.group())

print(phoneNumRegex.findall('Call me 415-555-1101 tomorrow, or text on 415-555-1234'))


#Phone Number regex group
groupNmuRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
zoe = groupNmuRegex.search('Call me 415-555-1101 tomorrow, or ')

print(zoe.group())
print(zoe.group(1))
print(zoe.group(2))

#Escape parenthesis when we looking for parenthesis
bracNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
tash = bracNumRegex.search('Call me (415) 555-1101 tomorrow')

print(tash.group())

#Pipe