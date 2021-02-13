import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group)

wo = batRegex.search('The Adventures of Batwoman')
print(wo.group)

no = batRegex.search('The Adventures of Batwowowowowowoman')
print(no == None)


#we can also use this for number without area code
phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('Call me 415-555-1101 tomorrow, or ')
print(mo.group())

no = phoneNumRegex.search('Call me 555-1101 tomorrow, or ')
print(no.group())