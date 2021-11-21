from random import randint
Randomnum=randint(1,100)
print(("WELCOME TO GUESS ME!") )
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
guess=0
last=-1
lst1=[]
while 1:
    num=int(input("Please Enter your guess : "))
    lst1.append(num)
    guess+=1
    if (num==Randomnum):
        print(f"\nYou Guessed it right in {guess} chances")
        break
    elif (num>100) or num<1:
        print("OUT OF BOUND")
    elif abs(num - Randomnum) <= abs(lst1[guess-2]-Randomnum) and last==0:
        print("WARMER")
    elif abs(num - Randomnum) >= abs(lst1[guess-2] - Randomnum) and last == 1:
        print("COLDER")
    elif abs(num-Randomnum)<=10:
        last=0
        print("WARM")
    elif abs(num - Randomnum)>10:
        last=1
        print("COLD")
