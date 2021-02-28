import re

#verbose mode: this helps with documentation 

verboseCoder12 = re.compile(r'''
(\d\d\d-)|      #area code (without parens, with dash)
(\(\d\d\d\) )    # -or- araea code with parens and no dash
\d\d\d          #first 3 digits
-               # second dash
\d\d\d\d        #last 4 digits
\sx\d{2,4}      #extension, like x 1234''',re.IGNORECASE | re.DOTALL |re.VERBOSE)

print(verboseCoder12.findall("my numbers are 415-555-1101, 415-555-1102, 415555-1103, 415-555-1103"))