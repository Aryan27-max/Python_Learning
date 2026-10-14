# You can put a function inside another function.
# Handy when a helper is only useful in one place.

def talk(phrase):
    def say(word):
        print(word)

    for word in phrase.split(" "):
        say(word)


talk("I am going to buy milk")


# To change an outer variable from the inner function, use nonlocal
def count():
    total = 0

    def increment():
        nonlocal total
        total += 1

    increment()
    increment()
    print(total)  # 2


count()
