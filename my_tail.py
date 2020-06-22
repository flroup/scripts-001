#!/usr/bin/env python3

'''
This scrip is similar with tail.
Script reads first 5 strings (counting the string
is not bigger 255 chars) from the file and after show actual
information from the file until interrupt
'''

from sys import argv

from os import stat


# Calculate start position for reading file
def calculate_start_position(filesize, number_of_strings):
    number_of_symbols = number_of_strings*255
    buffer = filesize - number_of_symbols
    return buffer if number_of_symbols < buffer < filesize else 0


# Read file from position and until the end
def read_file(filename, position):

    with open(filename) as f:
        f.seek(position)
        string_array = []

        for s in f:
            string_array.append(s)
        return string_array,  f.tell()


if __name__ == '__main__':

    try:
        filename = argv[1]
        filesize = stat(filename).st_size

    except IndexError:
        print("You should specify name of the file")

    except FileNotFoundError:
        print("There is no such file")

    else:
        print("My version of tail. Enjoy! For stop - press control + 'C'!")
        number_of_strings = -5
        start = calculate_start_position(filesize, number_of_strings)

        # Endless loop for checking and output the file modifications
        while True:

            try:
                if stat(filename).st_size >= start:
                    string_array, start = read_file(filename, start)
                    [print(s, end='') for s in
                     string_array[number_of_strings:]]
                    number_of_strings = 0

                elif stat(filename).st_size < start:
                    print("File size is reduced. Break.")
                    break
            except KeyboardInterrupt:
                print("\n\nGood luck! Have a good day!")
                break
