# create a string variable
message = " When her father unexpectedly dies, young Ella finds herself at the mercy of her cruel stepmother and her scheming stepsisters"
count = {}

# loop to iterate variable
for character in message.lower():
    count.setdefault(character,0)
    count[character] = count[character] + 1

print(count)