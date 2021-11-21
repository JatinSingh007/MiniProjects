from random import choice
from os import system
from time import sleep
#choice for random element from list

list_dealer =["<HIDDEN CARD>"]
list_player=[]
dealer_sum=0
player_sum=0

class Player_Balance():

    def __init__(self,owner,balance=500):
        self.owner=owner
        self.balance=balance

    def profit(self,amount):
        self.balance +=(2*amount)
        print("New Balance UPDATED : {}".format(self.balance))

    def bet(self):
        """ Deduct bet amount from players balance """
        while True:
            try:
                amount = int(input(f"How many chips would you like to bet?Your current balance is {self.balance} chips :"))
            except:
                    print("\nBet value should be an intiger")
                    continue
            else:
                if amount <= self.balance:
                    self.balance -= amount
                    print("\nBet Placed : {} chips\n".format(amount))
                    return amount
                else :
                    print("\nBet value is higher than Balance")
                    continue

class Deck():
    cards=52
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    availaible=[]
    def __init__(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.availaible.append((suit,rank))

    def new_card(self,varlist):
        self.cards-=1
        y,x=choice(self.availaible)
        self.availaible.remove((y,x))
        if self.cards==51:
            pass
        else:
            varlist.append(f"{x} of {y} ")
        if x in ['Jack', 'Queen', 'King']:
            return 10
        elif x=='Ace':
            if len(varlist)>2:
                new_value=int(input(f"Since its A of {y} .What value do u want 1 or 11?"))
                return new_value
            else:
                return 1
        else :
            return Deck.values[x]

def ask_bet():
    name=input("Please enter your name bro :")
    ins=Player_Balance(name)
    amount=ins.bet()
    return name,ins,amount

def check_win(player_sum,dealer_sum,name,ins,amount):
    if player_sum>21:
        print(f"{name} You are BUSTED")
        return 1
    elif dealer_sum > 21:
        print(f"{name} you WON!!!")
        ins.profit(amount)
        return 1
    if 17<dealer_sum<21:
        if dealer_sum>player_sum :
             print("Dealer won as sum of his cards is more than you {name} and his total sum is still less than 21 ")
             return 1
        elif dealer_sum < player_sum:
            print("{name} you won as sum of your cards is more than dealer and yout total sum is still less than 21 ")
            return 1
        else:
            print("EVERYONE WON AND GAME IS DRAWED")
            return 1
        return 0


def hit_stay():
    x="Run"
    while True:
        x = input("Do you want to Hit or stay :").upper()
        if x not in ["HIT", "STAY"]:
            print("INVALID INPUT")
            continue
        else:
            break
    if x=="HIT":
        return 1
    else :
        return 0

def show_some():
    print(f"\nHere is the deck of the dealer : {list_dealer}")
    print(f"Here is the deck of the player : {list_player}")



if __name__=="__main__":
        print("Welcome to BlackJack! Get as close to 21 as you can without going over!\nDealer hits until she reaches 17.")
        print("Aces count as 1 or 11.For the starting two cards Aces count as 1")
        new_instance=Deck()
        for i in range(0,2):
            dealer_sum+=new_instance.new_card(list_dealer)
            player_sum+=new_instance.new_card(list_player)
        game_on=True
        name,ins,amount=ask_bet()
        while game_on:
            show_some()
            player_turn=hit_stay()
            show_some()
            if player_turn:
                player_sum += new_instance.new_card(list_player)
            else:
                print("\nPlayer Stayed ")
                game_on=False
            if player_sum > 21:
                print(f"{name} You are BUSTED")
                break
        if player_sum <= 21:
            while dealer_sum < 17:
                dealer_sum += new_instance.new_card(list_dealer)
                show_some()
                # Test different winning scenarios
            if dealer_sum> 21:
                print(f"{name} you WON!!!")
                ins.profit(amount)
            elif dealer_sum > player_sum:
                print("Dealer won as sum of his cards is more than you {name} and his total sum is still less than 21 ")
            elif dealer_sum < player_sum:
                print(
                    "{name} you won as sum of your cards is more than dealer and yout total sum is still less than 21 ")
            else:
                print("EVERYONE WON AND GAME IS DRAWED")
