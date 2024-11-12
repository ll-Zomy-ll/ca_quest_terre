import sys


def ca_len(arg) -> int:
    '''Return the length of the argument.'''
    length: int = 0
    for i in arg:
        length += 1
    return length

def ca_isdigit(av: tuple) -> bool:
    '''Return True if the argument is a whole number.'''
    for arg in av:
        if ((arg[0] == '-' and ca_len(arg) > 1) or (ord(arg[0]) >= 48
             and ord(arg[0]) <= 57)):
            for i in arg[1:]:
                if (ord(i) < 48 or ord(i) > 57):
                    return False
        else:
            return False
    return True

def verify_args(av: tuple) -> bool:
    '''Return True if the arguments are valid.'''
    if ca_len(av) != 4:
        return False
    if not ca_isdigit(av[1:4]):
        return False
    if (int(av[1]) == int(av[2]) or int(av[1]) == int(av[3])
        or int(av[2]) == int(av[3])):
        return False
    return True


def sorting(f: int, s: int) -> tuple:
    if f < s:
        small: int = f
        big: int = s
    else:
        small = s
        big = f
    return (small, big)


def main(first: int, second: int, third: int) -> None:
    small, big = sorting(first, second)
    if (small < third and big > third):
        print(third)
    elif small > third:
        print(small)
    else:
        print(big)


if __name__ == '__main__':
    if verify_args(sys.argv):
        main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    else:
        print("This program needs three different whole numbers to operate")
