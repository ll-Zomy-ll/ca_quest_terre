import sys


def ca_len(arg) -> int:
    length: int = 0
    for i in arg:
        length += 1
    return length


def main(av: tuple) -> None:
    '''Print the arguments from the command line.'''
    for arg in av:
        print(arg)
        

if __name__ == '__main__':
    if ca_len(sys.argv) != 1:
        main(sys.argv[1:])
    else:
        print("The program needs some arguments to operate")
