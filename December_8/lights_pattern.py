"""
###############
# . T . . S T #
# T . . S T . #
# . . S T . . #
# . S T . . T #
# S T . . T S #
# T . . T S . #
###############

The given output example in the task is wrong!

"""
while True:
    try:
        n = int(input("Enter grid size N: "))
        if n > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")


print("#" * (2 * n + 3))
for row in range(1, n + 1):
    print("# ", end="")
    for col in range(1, n + 1):
        symbol = None
        value = row + col
        if value % 5 == 0 and value % 3 == 0:
            symbol = "G"
        elif value % 3 == 0:
            symbol = "T"
        elif value % 5 == 0:
            symbol = "S"
        else:
            symbol = "."
        print(symbol + " ", end="")
    print("#")
print("#" * (2 * n + 3))
