while True:
    number = input("Enter a 4-digit number: ")

    if len(number) == 4 and number.isdigit():
        break
    else:
        print("Wrong format!")

magic_number = number[0] + number[3]
print(int(magic_number))



