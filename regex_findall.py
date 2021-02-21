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

