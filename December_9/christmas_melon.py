
while True:
    try:
        n = int(input("Enter the number of melons: "))
        if n <= 0:
            print("The number of melons must be a positive whole number.")
            continue
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue

    try:
        weight_input = input("Enter the melon weights separated by spaces (e.g. 5 6.7 9.5): ")
        weights = list(map(float, weight_input.split()))
    except ValueError:
        print("Invalid input! Please enter only numbers separated by spaces.")
        continue

    if len(weights) == n:
        break
    else:
        print("The number of weights does not match. Please try again.")

average = sum(weights) / n

closest = weights[0]
closest_index = 0

for i in range(n):
    if abs(weights[i] - average) < abs(closest - average):
        closest = weights[i]
        closest_index = i

print(f"Melon number: {closest_index + 1} | Average weight: {average:.2f}")







