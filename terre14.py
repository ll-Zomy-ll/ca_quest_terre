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


def main(av: tuple, nb_av: int) -> bool:
    i: int = 0
    while i < nb_av:
        small = int(av[i])
        for nbr in av[i + 1:]:
            if small > int(nbr):
                print("Pas triée !")
                return False
        i += 1
    print("Triée !")
    return True


if __name__ == '__main__':
    if  (ca_len(sys.argv) > 2 and ca_isdigit(sys.argv[1:])):
        main(sys.argv[1:], ca_len(sys.argv[1:]))
    else:
        print("This program needs a list of whole numbers to operate")
