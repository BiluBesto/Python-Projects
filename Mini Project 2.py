import random
x=random.randint(1,100);
while True:
    d=int(input("Guess a number from 1 - 100:"))
    if x==d:
        print("You guessed right!")
        break;
    elif x>d:
        print("Guess Higher!")
    else:
        print("Guess Lower!")
