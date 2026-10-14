# break = stop the loop completely
# continue = skip this round, go to the next one

for n in range(10):
    if n == 2:
        continue  # skip 2
    if n == 5:
        break     # stop at 5
    print(n)      # prints 0, 1, 3, 4
