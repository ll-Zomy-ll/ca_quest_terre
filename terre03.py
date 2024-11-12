import sys


def ca_len(arg) -> int:
    '''Return the length of the argument.'''
    length: int = 0
    for i in arg:
        length += 1
    return length


def main(av: str) -> None:
    '''Print the alphabet from the letter in the command line.'''
    letter_cmd: int = ord(av)
    if (letter_cmd >= 97 and letter_cmd <= 122):
        for letter in range(letter_cmd, 123):
            print(chr(letter), end='')
        print()
    else:
        print("This program is not what you are looking for..")        


if __name__ == '__main__':
    if (ca_len(sys.argv) == 2 and ca_len(sys.argv[1]) == 1):
        main(sys.argv[1])
    else:
        print("This program needs ONE lowercase letter to function")
