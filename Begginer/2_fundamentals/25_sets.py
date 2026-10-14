# Sets are like lists but with NO duplicates and no order.

set1 = {"Roger", "Syd"}
set2 = {"Roger", "Luna"}

print(set1 & set2)  # in both          -> {'Roger'}
print(set1 | set2)  # everything       -> all three names
print(set1 - set2)  # only in set1     -> {'Syd'}

# Quick trick: remove duplicates from a list
nums = [1, 2, 2, 3, 3, 3]
print(set(nums))  # {1, 2, 3}
