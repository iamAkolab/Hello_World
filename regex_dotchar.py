import re

#^ enforces search match at the beginning of the string
beginsWithHelloRegex = re.compile(r'^Hello')

print(beginsWithHelloRegex.search('Hello there!'))
print(beginsWithHelloRegex.search('He said "Hello!"'))

#$ enforces search match at the end of the string
endsWithHelloRegex = re.compile(r'there!$')

print(endsWithHelloRegex.search('Hello there!'))
print(endsWithHelloRegex.search('He said there! they are are'))

#starts and ends with a number
allDigitsRegex = re.compile('r^\d+$')

print(allDigitsRegex.search('234879065387477448'))
print(allDigitsRegex.search('2348x9065x87477448'))


#wildcard character single character
#dot means anything but the new line *means anything from 0
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

atRegex1 = re.compile(r'.{1,2}at')
print(atRegex1.findall('The cat in the hat sat on the flat mat'))

#dot star (greedy mode)
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: AI Last Name: Sweigart'))

#dot star question mark (non greedy)
serve = '<To serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))

greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

# dot star doesnt go beyound new line
prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law'

dotStar = re.compile(r'.*')
print(dotStar.search(prime))

#greedy version to truly get all
dotStar1 = re.compile(r'.*', re.DOTALL)
print(dotStar1.search(prime))

#Upper case
roboCop = 'AL, Why does your programming book talk about RoboCop so much?'
vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall(roboCop))

vowelRegex1 = re.compile(r'[aeiou]', re.I)
print(vowelRegex1.findall(roboCop))

