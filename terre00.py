import sys


def ca_len(arg) -> int:
    '''Return the length of the argument.'''
    length: int = 0
    for i in arg:
        length += 1
    return length


def main() -> None:
    '''Print the alphabet.'''
    for letter in range(97, 123):
        print(chr(letter), end='')
    print()


if __name__ == '__main__':
    if ca_len(sys.argv) == 1:
        main()
    else:
        print("Please, just turn on the program")
