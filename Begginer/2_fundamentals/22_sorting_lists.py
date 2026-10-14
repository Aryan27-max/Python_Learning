# Two ways to sort a list.

items = ["banana", "Apple", "cherry"]

# sorted() gives a NEW list, the original stays untouched
print(sorted(items, key=str.lower))
print(items)

# .sort() changes the list itself
items.sort(key=str.lower)  # key=str.lower so capitals don't mess up the order
print(items)

nums = [3, 1, 2]
nums.sort(reverse=True)
print(nums)  # [3, 2, 1]
