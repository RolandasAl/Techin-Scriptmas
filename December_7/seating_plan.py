
while True:
    try:
        n = int(input("Enter number of rows: "))
        k = int(input("Enter number of seats in the first row: "))

        if n > 0 and k > 0:
            break
        else:
            print("Values must be positive whole numbers.")

    except ValueError:
        print("Invalid input. Please start again and enter whole numbers.")

total_seats = 0

for i in range(n):
    total_seats += k + 2 * i

print(f"Total number of seats: {total_seats}")
