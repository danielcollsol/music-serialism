#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import shuffle
import numpy as np
import string

def get_input():

    """
    Ask user to write input
    :return: string
    """
    # Ask for input
    inputString = ''
    while not inputString.isalpha():
        print('Introduce your name:')
        inputString = input()

    print('it passed', inputString)
    return inputString

def convert_string_to_serie(string):
    """
        :param string: input to convert to numerical serie
        :return: list of notes
    """
    # Convert string to notes
    map_letter_note = {'a':'A', 'b': 'B', 'c':'C', 'd': 'D', 'e': 'E', 'f':'F' , 'g': 'G', 'h': 'A#','i': 'C#','j': 'D#','k': 'F#','l': 'G#','m': 'A','n': 'G',
                        'o': 'D','p': 'E','q': 'F','r': 'G','s': 'A#','t': 'C#','u': 'D#','v': 'F#','w': 'G#','x': 'C','y': 'D#','z': 'D'}

    alphabet = string.ascii_lowercase

    # Convert notes to numerical serie
    map_note_number = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7,
                'G#': 8, 'A': 9, 'A#': 10, 'B': 11}


def create_random_serie():

    """
    :return: list of integers from 0 to 11 in random order
    """

    # Get random 12 non repeated notes list starting by the note 0
    random_serie = list(range(1, 12))
    shuffle(random_serie)
    random_serie.insert(0, 0)

    return random_serie


def construct_matrix(serie):

    """
    
    :param serie: list of integers from 0 to 11
    :return: 12x12 row tone matrix
    """"


        # Create ones 12x12 matrix with 0s in the diagonal
        matrix = np.ones((12,12), dtype=int)
        for index in list(range(0,12)):
                matrix[index,index] = 0

        # Add random serie in first row
        for index, note in enumerate(serie):
            matrix[0,index] = note

        # Fill next row
        i = 0
        previous_row = 0
        next_row = matrix[previous_row].tolist().index(11)
        while i < 12:
            print(matrix)
            for index in list(range(0,12)):
                if matrix[next_row,index] != 0:
                    matrix[next_row,index] = matrix[previous_row,index] + 1
            previous_row = next_row
            next_row = matrix[previous_row].tolist().index(11)
            i += 1

        return matrix


def main():
    """ Main program """
    
    # Get input
    input = get_input()

    # Generate random serie
    serie = create_random_serie()

    # Create matrix
    matrix = construct_matrix(serie)




if __name__ == "__main__":
    main()