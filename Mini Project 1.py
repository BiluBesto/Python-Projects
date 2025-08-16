#Simple Dice Rolling Game
import random
while True:
    choice = input("Roll Dice?(y/n): ").lower();
    if choice == "y":
        d1=random.randint(1,6);
        d2=random.randint(1, 6)
        print(f"({d1},{d2})")
    elif choice == "n":
        print("Thank you for playing!")
        break
    else:
        print("Invalid Choice!");

