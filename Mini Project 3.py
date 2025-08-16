#Project to do a rock paper scissors game
import random
cs=['r','s','p']
x=int(input("Enter no of trials: "))
csct=0;compct=0;d=0;
while d!=x:
    ch = input("Enter your choice(r/s/p):").lower()
    comp = random.choice(cs);
    print("Computer chose",comp)
    if ch==comp:
        print("Draw!")
    elif (ch=='r'and comp=='p')or (ch=='p' and comp=='s') or (ch=='s'and comp=='r'):
        print("Computer Win!")
        compct+=1;
    elif (ch=='p'and comp=='r')or (ch=='s' and comp=='p') or (ch=='r'and comp=='s'):
        print("You Win!")
        csct+=1;
    else:
        print("Invalid Choice!")
    d=d+1
print("Your score:",csct)
print("Computer score:",compct)