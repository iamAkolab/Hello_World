import traceback
"""[summary]

    this function print box


    **************
    *            *
    *            *
    *            *
    **************
"""

def printbox(symbol,width,height):
    if len(symbol) != 1:
        raise Exception ('"Symbol" needs to be astring of length 1.')
    if (width <2) or (height < 2):
        raise Exception ('"Width" and "Height" must be greater than or equal to 2')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + ' ' * (width - 2) + symbol)

    print(symbol * width)

## printbox('*', 1, 1)    
#printbox('*', 2, 3) found bug that return flat
printbox('*', 3, 3)
printbox('*', 8, 5)

#this part should be implemented inside the code function
try:
    raise Exception("this is the error message")

except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written error_log.txt')

#Triangle Quest Print a numerical triangle of height n-1
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i*10**i//9)