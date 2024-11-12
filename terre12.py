import sys


def ca_len(arg) -> int:
    '''Return the length of the argument.'''
    length: int = 0
    for i in arg:
        length += 1
    return length

def ca_ishours(arg: str) -> bool:
    '''Return True if the argument is a valid hour.'''
    fmt: str = arg[5:7]
    hour: str = arg[0:2]
    mins: str = arg[3:5]
    for i in hour:
        if (ord(i) < 48 or ord(i) > 57):
            return False
    for i in mins:
        if (ord(i) < 48 or ord(i) > 57):
            return False
    if (fmt == 'AM' and (int(hour) < 12 and int(mins) < 60)):
            return True
    if (fmt == 'PM' and (int(hour) > 0 and int(hour) < 13 and int(mins) < 60)):
            return True
    return False

def verify_args(av: tuple) -> bool:
    '''Return True if the arguments are valid.'''
    if (ca_len(av) != 2):
        return False
    if (ca_len(av[1]) == 7 and ca_ishours(av[1])):
        if av[1][2] == ':':
            return True
    return False


def main(av: str) -> None:
    hr: str = av[0:2]
    fmt: str = av[5:7]
    if ((int(hr) < 12 and fmt == 'AM') or int(hr) == 12):
        print(av[0:5])
    else:
        hours: dict = {'01': '13', '02': '14', '03': '15', '04': '16',
                       '05': '17', '06': '18', '07': '19', '08': '20',
                       '09': '21', '10': '22', '11': '23'}
        for i, j in hours.items():
            if (av[0:2] == i and fmt == 'PM'):
                hr = j
        print(f"{hr}{av[2:5]}")


if __name__ == '__main__':
    if verify_args(sys.argv):
        main(sys.argv[1])
    else:
        print("This program needs an entry in HH:MMAM/PM format to operate")
