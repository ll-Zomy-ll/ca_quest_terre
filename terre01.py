import sys


def ca_len(arg) -> int:
    '''Return the length of the argument.'''
    length: int = 0
    for i in arg:
        length += 1
    return length


def main(name: str) -> None:
    '''Print the program's name.'''
    print(name)


if __name__ == '__main__':
    if ca_len(sys.argv) == 1:
        main(sys.argv[0])
    else:
        print("Please, just turn on the program")
