# Loops repeat code so you don't have to.

# while loop - keeps going while the condition is True
count = 0
while count < 3:
    print("while:", count)
    count += 1

# for loop - goes through each item
dogs = ["Roger", "Syd"]
for dog in dogs:
    print("for:", dog)

# range() gives you numbers
for i in range(3):  # 0, 1, 2
    print("range:", i)

# enumerate() gives you the position AND the item
for index, dog in enumerate(dogs):
    print(index, dog)
