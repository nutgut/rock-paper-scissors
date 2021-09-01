#!/usr/bin/python
# coding=utf-8
"""""
This is a simple game of 'rock, paper, scissors'.
The code contains only one custom class 'Thing'.
Thing only generates random digits and return the value to the main function.
Feel free to edit, copy my code :)
Written in Python 2.7.
2017-03-20, by: nutgut
"""
import Motor
from sys import exit

def main():
    # Create object from the class Thing
    my_game = Motor.Thing()

    # Variable holding counted profits
    score=[0,0]
    print('Welcome to the game: Rock, Paper, Scissors!')
    print('Best out of three, wins.')
    print('Be my guest, start (rock, paper or scissors):')

    # First who get's profit 3 times wins the game
    while score[0]<3 and score[1]<3:
        # My value
        game = input('> ')
        # One random digit (value) is created
        my_game.randoms()
        # Get the random value
        game2 = my_game.get_what()
        print(game2)
        
        if (game in ["rock", "paper", "scissors"]):
            print('You picked: %s' % game)
            result = race([game, game2])
        else:
            print('Wrong input, bye bye.')
            exit()

        # Depending on the result, profit is distributed to player or computer
        score[0]+=result[0]
        score[1]+=result[1]
    
        print('Game score: You %d Me %d' % (score[0], score[1]))

    # Prints out who won the game
    if score[0] > score[1]:
        print('\nYou won.....')
    elif score[1] < score[0]:
        print('\nI won!!!')
    else:
        print("\nIt's even.")

# This is the setup for the game rules

def race(args):
    if ''.join(args) in ('rockrock', 'paperpaper', 'scissorsscissors'):
        print('Even!')
        return [1,1]
    elif ''.join(args) in ('rockpaper', 'paperscissors', 'scissorsrock'):
        print('I won!')
        return [0,1]
    elif ''.join(args) in ('rockscissors', 'paperrock', 'scissorspaper'):
        print('You won...')
        return [1,0]
    else:
        exit(0)

main()
