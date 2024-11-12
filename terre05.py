import sys


def ca_len(arg) -> int:
    '''Return the length of the argument.'''
    length: int = 0
    for i in arg:
        length += 1
    return length

def ca_isdigit(arg: str) -> bool:
    '''Return True if the argument is a whole number.'''
    if ((arg[0] == '-' and ca_len(arg) > 1) or (ord(arg[0]) >= 48
         and ord(arg[0]) <= 57)):
        for i in arg[1:]:
            if (ord(i) < 48 or ord(i) > 57):
                return False
        return True
    else:
        return False
    
    
def main(dividend: int, divisor: int) -> None:
    if (divisor != 0 and abs(dividend) > abs(divisor)):
        print(f"résultat: {int(dividend / divisor)}")
        print(f"reste: {dividend % divisor}")
    else:
        print("erreur.")


if __name__ == '__main__':
    if (ca_len(sys.argv) == 3 and ca_isdigit(sys.argv[1])
        and ca_isdigit(sys.argv[2])):
        main(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print("This program needs two whole numbers to operate")
