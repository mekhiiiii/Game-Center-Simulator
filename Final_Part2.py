# Mekhi Palmer
# 1/22/2026

import random

#This function will randomly pick a side from a two-sided coin
def flip_coin():
    # TODO: implement this function
    # get a random int between 0 and 1
    coin_choice = random.randint(0, 1)
    # if the number is 0, return "Coin flip: Tails"
    if coin_choice == 0:
        return "Coin flip: Tails"
    # if the number is 1, return "Coin flip: Heads"
    if coin_choice == 1:
        return "Coin flip: Heads"


#This function will randomly choose a side from a six-sided dice
def roll_d6():
    # TODO: implement this function
    # get a random int between 1 and 6
    dice_choice = random.randint(1, 6)
    # return "D6 roll: [that number]"
    return "D6 roll: " + str(dice_choice)


#This function wll randomly choose a side from a twenty-sided dice
def roll_d20():
    # TODO: implement this function
    # get a random int between 1 and 20
    dice_choice2 = random.randint(1, 20)
    # return "D20 roll: [that number]"
    return "D20 roll: " + str(dice_choice2)

#This function will randomly pick a card from a deck of cards
def pick_card():
    # get a random number between 0 and 3
    suit = random.randint(0, 3)
    # initialize list
    card_suit = ["spades", "hearts", "diamonds", "Clubs"]
        
    # then get a random number between 1 and 13
    value = random.randint(1, 13)
    # [card value]: 1=Ace, 11=Jack, 12=Queen, 13=King, 2-10 are normal (no translation)
    if value == 1:
        card_value = "Ace"
    elif value == 11:
        card_value = "Jack"
    elif value == 12:
        card_value = "Queen"
    elif value == 13:
        card_value = "King"
    else:
        card_value = str(value)
    # return "Your card: [card value] of [card suit]"
    return "Your card is: " + str(card_value) + " of " + card_suit[suit]

#This displays all of the game choices and allows user to pick a game, and asks user if they would like to play again
def main():
    run_again = "y"
    while run_again == "y" or run_again == "Y":
        print('Welcome to the game center!\nHere are your options:')
        print('\t1) Flip a coin\n\t2) Pick a random playing card')
        print('\t3) Roll a 6-sided dice\n\t4) Roll a 20-sided dice')
        choice = input('What would you like to do? ')
        if choice == "1":
            print(flip_coin())
        if choice == "2":
            print(pick_card())
        if choice == "3":
            print(roll_d6())
        if choice == "4":
            print(roll_d20())
        run_again = input("Do you want to play again (y/n)?: ")

main()