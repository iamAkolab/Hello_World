import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group)

wo = batRegex.search('The Adventures of Batwoman')
print(wo.group)

no = batRegex.search('The Adventures of Batwowowowowowoman')
print(no == None) #if true was not found

# check for zero or more matches
#we can also use this for number without area code
phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('Call me 415-555-1101 tomorrow, or ')
print(mo.group())

no = phoneNumRegex.search('Call me 555-1101 tomorrow, or ')
print(no.group())#if true was not found

#matches zero or more 
zo = batRegex.search('The Adventures of Batwowowowowowoman')
print(zo == None) #if true was not found

#matches 1 or more (must occur)
batRegex1 = re.compile(r'Bat(wo)+man')
mo1 = batRegex1.search('The Adventures of Batwowowowowoman')
print(mo1.group())

#escaping * +
regex = re.compile(r'\+\*\?')
regex.search('I learned anout +*? regex syntax')

#3 Phone numbers
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d(,)?')
ph = phoneRegex.search("my numbers are 415-555-1101, 415-555-1102, 415-555-1103")
print(ph.group())

# range (start, end)
haRegex = re.compile(r'(Ha)(3,5)')
ha = haRegex.search('He said "Hahahaha"')
print(ha == None) #if true was not found

#Greedy Matching given range
digitRegex  = re.compile(r'(\d)(3,5)')
digitRegex.search('1234567890') #gets the end range i,e its greedy

#enforce smallest range 
digitRegex1  = re.compile(r'(\d)(3,5)?') #gets non greedy match
digitRegex1.search('1234567890')