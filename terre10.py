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


def main(nbr: int) -> None:
    if nbr > 1:
        i: int = 1
        while i < nbr:
            if (i != nbr and i != 1 and nbr % i == 0):
                print(f"Non, {nbr} n'est pas un nombre premier.")
                return
            i += 1
        print(f"Oui, {nbr} est un nombre premier.")
    else:
        print(f"Non, {nbr} n'est pas un nombre premier.")


if __name__ == '__main__':
    if (ca_len(sys.argv) == 2 and ca_isdigit(sys.argv[1])):
        main(int(sys.argv[1]))
    else:
        print("This program needs one positif whole number to operate")
