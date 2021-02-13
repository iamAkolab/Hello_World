import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group)

wo = batRegex.search('The Adventures of Batwoman')
print(wo.group)

no = batRegex.search('The Adventures of Batwowowowowowoman')
print(no == None)