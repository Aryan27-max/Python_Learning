# "with" handles setup and cleanup for you.
# Classic example: files. It closes the file automatically, even if something breaks.

with open("notes.txt", "w") as file:
    file.write("Hello from Python!")

with open("notes.txt", "r") as file:
    print(file.read())

# No need to call file.close() - "with" did it for us.
