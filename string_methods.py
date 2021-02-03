#String method
#strings are immutable objects
spam = "hello world!"

spam.count()
spam.title()
spam.lower()
spam.upper()
spam.replace()
spam.join()

#returns Boolean response
spam.isalnum()
spam.isalpha()
spam.isdecimal()
spam.islower()
spam.isupper()
spam.istitle()
spam.isspace()
spam.startswith()
spam.endswith()

spam.strip()
spam.rstrip()
spam.lstrip()

spam.center(10,"-")
spam.ljust()
spam.rjust()



#String formatting

name =  "opomiulero"
address = "19 chevron drive"
deserts = "tulips pie"

"Hello %s, the party is at %s, kindly print %s when you are coming", (name, address, deserts)

#PyperpyModule
# go to the python folder on CMD enetr the "Scripts" directory
# then type " pip.exe install pyperclip"

#Pyperclip has a copy and paste function 
#that copies and paste to your clipboard