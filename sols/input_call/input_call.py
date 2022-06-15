#!/usr/bin/env python3

import random


def guess_func(anum):
    while True:
        guess = input('Enter your guess: ')
        int_guess = int(guess)
        if(int_guess > anum):
            print('...it is smaller...')
        elif(int_guess < anum):
            print('...it is bigger...')
        else:
            print('Well done!!')
            break


def input_min_max():
    min = input('Enter a min number: ')
    max = input('Enter a max number: ')
    return {int(min), int(max)}


def main():
    while True:
        min, max = input_min_max()
        num_to_guess = random.randint(min, max)
        guess_func(num_to_guess)
        want_continue = input('Want to continue? (Y/N): ')
        if (want_continue.lower() == 'n'):
            break


main()
