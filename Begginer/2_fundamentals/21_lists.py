# Lists hold many items in order. Use square brackets.

dogs = ["Roger", "Syd"]

print(dogs[0])       # Roger
dogs[1] = "Max"      # change an item
print(dogs)

dogs.append("Bella")       # add to the end
dogs.insert(0, "Luna")     # add at a spot
print(dogs)

dogs.remove("Max")         # remove by value
last = dogs.pop()          # remove the last one and give it back
print("Popped:", last)

print(len(dogs))           # how many
print("Roger" in dogs)     # is it there?
print(dogs[0:2])           # slicing works like strings

more = dogs + ["Rex"]      # join lists
print(more)
