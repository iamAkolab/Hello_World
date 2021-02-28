import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

print(namesRegex.sub('REDACTED','Agent Alice gave the secret documents to Agent Bob.'))


#Lets just use their first nme
namesRegex1 = re.compile(r'Agent (\w)\w*')
print(namesRegex1.findall('Agent Alice gave the secret documents to Agent Bob.'))

print(namesRegex1.sub(r'Agent \1*****','Agent Alice gave the secret documents to Agent Bob.'))


#print(namesRegex.sub('Agent \1*****','Agent Alice gave the secret documents to Agent Bob.'))
#printed this \
#Agent ☺***** gave the secret documents to Agent ☺*****

