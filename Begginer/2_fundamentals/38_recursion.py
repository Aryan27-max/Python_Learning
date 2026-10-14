# Recursion = a function that calls itself.
# Always needs a "stop" case or it goes forever.

def factorial(n):
    if n == 1:      # the stop case
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # 5*4*3*2*1 = 120
