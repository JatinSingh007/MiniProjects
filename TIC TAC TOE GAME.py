#Imported random ,sleep,system from some libriaries to generate randomint,delay screen and clear screen resp
from os import system
from time import sleep
from random import randint

#FUNCTION FOR PRINT BOARD EACH TIME
def printgrid(l):
    print("      |       |       ")
    print(f"  {l[0]}   |   {l[1]}   |   {l[2]}   ")
    print("______|_______|_______")
    print("      |       |       ")
    print(f"  {l[3]}   |   {l[4]}   |   {l[5]}   ")
    print("______|_______|_______")
    print("      |       |       ")
    print(f"  {l[6]}   |   {l[7]}   |   {l[8]}   ")
    print("      |       |       ")

#Here is the DESCRIPTION about Game
def start():
    print("WELCOME TO TIC-TAC-TO GAME!! ")
    print("Here are the controls : Select a number to choose your Position")
    printgrid(l)
    input("SO LETS BEGIN!! Press Enter to Continue ")
    system("cls")

#Function FOR PLAYER INPUT OF SIGN X or O
def player_input():
    choice = '0'
    while choice not in ['X','O']:
        choice=input(f"PLAYER {x+1} please enter your Symbol X or O : ").upper()
        if choice not in ['X','O']:
            print("Please Enter Again as u have entered the wrong choice")
            sleep(0.5)
            system('cls')
            continue
        elif x==0 and choice=='X':
            p1,p2='X','O'
        elif x==1 and choice=='O':
            p2,p1='O','X'
        else:
            p2,p1='X','O'
        return p1, p2


#To mark position on board :takes input ,check if available and then mark 
def markin(x,turn):
    while True:
        if x==0:
            m=p1
        else:
            m=p2
        printgrid(l)
        pos = int(input(f"\nPlayer {x+1} enter {m} position :"))
        if (pos not in rem):
            print("OUT OF BOUND!! PLEASE TRY AGAIN")
            continue
        l[pos - 1] = m
        system("cls")
        rem.remove(pos)
        turn += 1
        x = (x + 1) % 2
        return x,turn
        break

#Return true when not winning and draw conditions
def anti_check():
    if True in [l[0]==l[1]==l[2],l[3]==l[4]==l[5],l[6]==l[7]==l[8],l[0]==l[3]==l[6],l[4]==l[1]==l[7],l[2]==l[5]==l[8],l[0]==l[4]==l[8],l[4]==l[6]==l[2]]:
        return False
    else :
        return True



game_ON = True
while game_ON:

    # ALL VARIABLES DECLARATION
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Very Important part of program
    turn = 0
    pos = 0
    draw = 0
    rem = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    p1 = 'player1'
    p2 = 'player2'
    x = randint(0, 1)
    play = 2

    start()  #INFO DISPLAY
    l = [1,2,3,4,5,6,7,8,9]      #for clear board
    print(f"So its decided by computer that {x+1} will go first .\n")
    p1,p2=player_input()            #SIGN ASSIGN
    print(f"\nSo Player 1 Symbol is {p1} and player 2 is symbol {p2}")

    #To itterate the turns
    while anti_check():
        x, turn = markin(x, turn) 
        if turn > 8 :
            if(anti_check()):
                draw = 1
            break

    #CONDITION CHECK
    if(draw):
        printgrid(l)
        print("Everybody is the winner because the Game is Drawed")
    elif True in [l[0]==l[1]==l[2]==p1,l[3]==l[4]==l[5]==p1,l[6]==l[7]==l[8]==p1,l[0]==l[3]==l[6]==p1,l[4]==l[1]==l[7]==p1,l[2]==l[5]==l[8]==p1,l[0]==l[4]==l[8]==p1,l[4]==l[6]==l[2]==p1]:
        printgrid(l)
        print("Congratulations Player 1 YOU WON!!!")
    else:
        printgrid(l)
        print("Congratulations Player 2 YOU WON!!!")
    game_ON=False
    #Do u want to play again
    while play not in [0,1]:
        play=int(input("\nDo u want to playe again!! Enter 1 for Yes and 0 for exit :)"))
    game_ON=bool(play)
    system("cls")
