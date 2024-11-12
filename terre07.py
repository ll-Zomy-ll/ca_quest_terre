import sys


def ca_len(arg) -> int:
    '''Return the length of the argument.'''
    length: int = 0
    for i in arg:
        length += 1
    return length

def ca_isdigit(arg: str) -> bool:
    '''Return True if the argument is a whole number.'''
    comma: int = 0
    point: int = 0
    if ((arg[0] == '-' and ca_len(arg) > 1) or (ord(arg[0]) >= 48
         and ord(arg[0]) <= 57)):
        for i in arg[1:]:
            if (ord(i) < 44 or ord(i) > 57 or ord(i) == 47 or ord(i) == 45):
                return False
            if ord(i) == 44:
                comma += 1
                if comma > 1:
                    return False
            if ord(i) == 46:
                point += 1
                if point > 1:
                    return False
        return True
    else:
        return False


def main(arg: str) -> None:
    print(ca_len(arg))


if __name__ == '__main__':
    if (ca_len(sys.argv) == 2 and ca_len(sys.argv[1]) > 0 
        and not ca_isdigit(sys.argv[1])):
        main(sys.argv[1])
    else:
        print("erreur.")
