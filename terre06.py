import sys


def ca_len(arg) -> int:
    '''Return the length of the argument.'''
    length: int = 0
    for i in arg:
        length += 1
    return length


def main(arg: str) -> None:
    if ca_len(arg) > 0:
        for i in range(ca_len(arg) - 1, -1, -1):
            print(arg[i], end='')
        print()
    else:
        print("Put something into the quotes")


if __name__ == '__main__':
    if ca_len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("You just need to put something into double quotes :)")
