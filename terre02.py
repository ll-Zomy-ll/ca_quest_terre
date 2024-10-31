import sys


def main(av: tuple) -> None:
    '''Print the arguments from the command line.'''
    for arg in av:
        print(arg)
        

if __name__ == '__main__':
    main(sys.argv[1:])
