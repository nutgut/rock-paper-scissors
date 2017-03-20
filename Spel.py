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

    # Variables holding counted profits
    # Player
    your_profit = 0
    # Computer
    my_profit = 0
    print 'Welcome to the game: Rock, Paper, Scissors!'
    print 'Best out of three, wins.'
    print 'Be my guest, start (rock, paper or scissors):'

    # First who get's profit 3 times wins the game
    while your_profit < 3 and my_profit < 3:
        # My value
        game = raw_input('> ')
        # One random digit (value) is created
        my_game.randoms()
        # Get the random value
        game2 = my_game.get_what()

        if game == 'rock':
            print 'You picked: %s' % game
            print 'I picked: %s' % game2
            # Get who get's profit
            result = race(game, game2)

        elif game == 'paper':
            print 'You picked: %s' % game
            print 'I picked: %s' % game2
            result = race(game, game2)

        elif game == 'scissors':
            print 'You picked: %s' % game
            print 'I picked: %s' % game2
            result = race(game, game2)

        else:
            print 'Wrong input, bye bye.'
            exit()

        # Depending on the result, profit is distributed to player or computer
        if result == 'even':
            your_profit += 1
            my_profit += 1

        elif result == 'player':
            your_profit += 1

        else:
            my_profit += 1

        print 'Game score: You %d Me %d' % (your_profit, my_profit)

    # Prints out who won the game
    if your_profit > my_profit:
        print '\nYou won.....'
    elif your_profit < my_profit:
        print '\nI won!!!'
    else:
        print "\nIt's even."

# This is the setup for the game rules


def race(arg1, arg2):
    if arg1 == 'rock' and arg2 == 'rock':
        print 'Even!'
        return 'even'
    elif arg1 == 'rock' and arg2 == 'paper':
        print 'I won!'
        return 'computer'
    elif arg1 == 'rock' and arg2 == 'scissors':
        print 'You won...'
        return 'player'
    elif arg1 == 'paper' and arg2 == 'paper':
        print 'Even!'
        return 'even'
    elif arg1 == 'paper' and arg2 == 'scissors':
        print 'I won!'
        return 'computer'
    elif arg1 == 'paper' and arg2 == 'rock':
        print 'You won...'
        return 'player'
    elif arg1 == 'scissors' and arg2 == 'scissors':
        print 'Even!'
        return 'even'
    elif arg1 == 'scissors' and arg2 == 'rock':
        print 'I won!'
        return 'computer'
    elif arg1 == 'scissors' and arg2 == 'paper':
        print 'You won...'
        return 'player'
    else:
        exit(0)


main()
