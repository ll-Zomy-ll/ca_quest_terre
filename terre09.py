import sys


def ca_len(arg) -> int:
    '''Return the length of the argument.'''
    length: int = 0
    for i in arg:
        length += 1
    return length

def ca_isdigit(arg: str) -> bool:
    '''Return True if the argument is a whole number.'''
    for i in arg:
        if (ord(i) < 48 or ord(i) > 57):
            return False
    return True


def main(square: int) -> None:
    if square > 1000000000000:
        print("The number is too long.")
        return
    i: int = 0
    while i <= square / 2 + 1:
        if i * i == square:
            print(i)
            return
        elif i * i > square:
            print("This square root is not a int.")
            return
        i += 1


if __name__ == '__main__':
    if (ca_len(sys.argv) == 2 and ca_isdigit(sys.argv[1])):
        main(int(sys.argv[1]))
    else:
        print("This program needs only one positif whole number to operate")
