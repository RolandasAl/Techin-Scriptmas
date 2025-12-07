gift_bag = []
total_price = 0
magic_toys = 0

while True:
    try:
        toy_price = float(input("Enter toy price (0 to end Santa's list): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if toy_price < 0:
        print("Toy price cannot be negative!")
        continue

    if toy_price == 0:
        break

    gift_bag.append(toy_price)

for price in gift_bag:
    if price > 10:
        total_price += price
        magic_toys += 1

print(f"Total price of magical toys: {total_price:.2f} EUR")
print(f"Number of magical toys: {magic_toys}")
