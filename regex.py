import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me 415-555-1101 tomorrow, or ')
print(mo.group())