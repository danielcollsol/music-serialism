#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    """ Main program """
    # Ask for input
    inputString = ''
    while not inputString.isalpha():
        print('Introduce your name:')
        inputString = input()


    print('it passed', inputString)
    return inputString

if __name__ == "__main__":
    main()