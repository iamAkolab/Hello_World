# instruction to user
print('How many cars do you have')

# get user inputs
numCar = input()

# try block
try:
    if int(numCar) > 4:
        print("That is a lot of Cars!, you are quite the collecter")
    elif int(numCar) < 0:
        print("you can not have a negative numbers of cars")
    elif int(numCar) == 0:
        print("ooop2s! sorry to hear about that")
    else:
        print("Not bad, you are doing well")
except ValueError:
    print("Sighs, you did not enter a number genius")