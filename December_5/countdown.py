from digits_array import DIGITS
import random
import os
import time


MESSAGES = [
    "Santa is preparing…",
    "Reindeer are buckling up…",
    "Sleigh warming up…"
]

def clear_screen():
    # Windows - "cls" | Mac/Linux - "clear"
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

for num in range(10, -1, -1):
    clear_screen()

    if num == 10:
        digit1 = DIGITS[1]
        digit0 = DIGITS[0]
        for row in range(len(digit1)):
            print(digit1[row] + "  " + digit0[row])

    else:
        for row in DIGITS[num]:
            print(row)

    print()
    if num > 0:
        print(random.choice(MESSAGES))
    else:
        print("SANTA’S SLEIGH IS LAUNCHING!")
    time.sleep(1)




