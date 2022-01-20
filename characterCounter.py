# create a function
def message_counter(msg):
    
    # dictionary to hold the counter
    count = {}
    
    # loop to iterate variable
    for character in msg.lower():
        count.setdefault(character,0)
        count[character] = count[character] + 1
        
    # print
    print(count)

# create a string variable
message = " When her father unexpectedly dies, young Ella finds herself at the mercy of her cruel stepmother and her scheming stepsisters"


message_counter(message)

'''

for character in message.lower():
    count.setdefault(character,0)
    count[character] = count[character] + 1

# print
print(count)
'''