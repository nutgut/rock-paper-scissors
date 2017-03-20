#!/usr/bin/python
# coding=utf-8
import random


# Class for 'Rock, paper, scissors'
class Thing:
    def __init__(self):
        self.__what = ''

    # Method for creating rock, paper or scissors (randomly)
    def randoms(self):
        digit = random.randint(0, 2)
        if digit == 0:
            self.__what = 'rock'
        elif digit == 1:
            self.__what = 'paper'
        else:
            self.__what = 'scissors'

    # Method returning the value for __what variable
    def get_what(self):
        return self.__what
