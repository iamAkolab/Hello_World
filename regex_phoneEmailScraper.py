#! python3

import re, pyperclip

#Create a regex for phone numbers
phoneRegex =  re.compile(r'''
#phone number types 415-555-000, (415) 555-000, 555-000 ext 12345, ext.12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?    #Arera code (opttional)
(\s|-)                      # first separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s)|x)           # extension word-part (optional)
 (\d{2,5}))?                # extension number-part (optional)
)''',re.VERBOSE)

# check to see if phoneRegex is working ....
print(phoneRegex.findall(r'814-825-6659'))

#Create a regex for email addresses
emailRegex =  re.compile(r'''
#some.+_thing@(\d{2,5}))?.com
[a-zA-Z0-9_+.]+   # name part
@                 # @ symbol
[a-zA-Z0-9_+.]+   # domain name part
''', re.VERBOSE)

# check to see if emailRegex is working ....
print(emailRegex.findall(r'mail me at autopython@py.com'))


#Get the text off the clipboard
text = pyperclip.paste()

#Extraxt the email/phone from this text
extractedPhoneRegex = phoneRegex.findall(text)
extractedEmailRegex = emailRegex.findall(text)



allPhoneNumbers = []
for phoneNumbers in extractedPhoneRegex:
    allPhoneNumbers.append(phoneNumbers[0])


#Todo: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmailRegex)
pyperclip.copy(results)

