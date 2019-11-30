import random

from time import sleep

import sys


unused_cards = [2, 3, 4, 5, 6, 7,\
               8, 9, 10, 11, 12,\
               13, 14,\
               2, 3, 4, 5, 6, 7,\
               8, 9, 10, 11, 12,\
               13, 14,\
               2, 3, 4, 5, 6, 7,\
               8, 9, 10, 11, 12,\
               13, 14,\
               2, 3, 4, 5, 6, 7,\
               8, 9, 10, 11, 12,\
               13, 14]
               

used_cards = []



print('This is a game of snap!\n\nJack, Queen, King and Ace have been replaced with 11 - 14')

print("\nPress Ctrl + C when two of the same cards are dealt in a row to snap!")



def cards():
    """Initiates the card dealing and creates the used_cards list used by the key functions"""
    try:
        for card in range(52):
            card = random.choice(unused_cards.copy())
            used_cards.append(card)
            unused_cards.remove(card)
            print(card)
            sleep(0.01)
            computer_snap()
    except IndexError:
        print('\nCards did not generate a snap.\n\nTry again or press Ctrl + c to exit.')
        restart_game()


def computer_snap():
    """Computer detects when the cards make a snap and snaps unless the user does so first"""
    for i, j in enumerate(used_cards[:-1]):
        if j == used_cards[i+1]:
            print('\nComputer snaps!\nGame over!\nPlay again or press Ctrl + c to exit')
            restart_game()
            sys.exit()

            
def user_snap():
    """Allows the user to snap"""
    for i, j in enumerate(used_cards[:-1]):
        if j == used_cards[i+1]:
            print('\nValid snap! You win!\n\nPlay again or press Ctrl + c to exit')
            restart_game()
            break
    else:
        print('\nCards do not match! Game over!\nPlay again or press Ctrl + c to exit')
        restart_game()
        sys.exit()

        
def starting_condition():
    """Defines the conditions needed to start the program"""
    start_command = ' '
    while True:
        print("\nPress 't' and Enter to begin...")
        start_command = input()
        if start_command == 't':
            try:
                cards()
            except KeyboardInterrupt:
                user_snap()
                raise

            
def restart_game():
    """Re-populates the unused_cards list and clears used_cards, allowing the game to be re-played"""
    unused_cards.extend(used_cards)
    used_cards.clear()
    try:
        starting_condition()
    except KeyboardInterrupt:
        print('\nThanks for playing')
        sys.exit()


starting_condition()
