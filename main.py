def append(x, y):
    fh = open(y, "a")
    fh.write("\n" + "# " + "Made by: " + x)
    fh.close()
    print("Done.")


def start():
    global x
    global y
    x = input("Please enter your name: ")
    y = input("Please enter the file name: ")
    append(x, y)
    x = input("Do you want to comment another file? (y/N)")
    if x == "y":
        start()
    else:
        exit()


print("Python Commenter.")
input("Press <--/ to start.")
start()

# Made by: callum
