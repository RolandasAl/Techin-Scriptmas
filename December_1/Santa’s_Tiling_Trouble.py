print("Welcome to Santa's Tile Cost Calculator!")
print("----------------------------------------")
while True:
    try:
        length = int(input("What's the length of the room in meters? "))
        if length <= 0:
            print("Length must be a positive whole number.")
            continue
        break
    except ValueError:
        print("Please enter a valid whole number.")

while True:
    try:
        width = int(input("What's the width of the room in meters? "))
        if width <= 0:
            print("Width must be a positive whole number.")
            continue
        break
    except ValueError:
        print("Please enter a valid whole number.")

while True:
    try:
        m2price = float(input("What's the price per m² in EUR? "))
        if m2price <= 0:
            print("Price must be greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

total_price = (length * width) * m2price * 1.05
print(f"Total price for tiles is: {total_price:.2f} EUR.")
