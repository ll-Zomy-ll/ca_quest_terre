import sys


def ca_len(arg) -> int:
    '''Return the length of the argument.'''
    length: int = 0
    for i in arg:
        length += 1
    return length

def ca_ishours(arg: str) -> bool:
    '''Return True if the argument is a valid hour.'''
    hour: str = arg[0:2]
    mins: str = arg[3:5]
    for i in hour:
        if (ord(i) < 48 or ord(i) > 57):
            return False
    for i in mins:
        if (ord(i) < 48 or ord(i) > 57):
            return False
    if (int(hour) < 24 and int(mins) < 60):
        return True
    return False

def verify_args(av: tuple) -> bool:
    '''Return True if the arguments are valid.'''
    if (ca_len(av) != 2):
        return False
    if (ca_len(av[1]) == 5 and ca_ishours(av[1])):
        if av[1][2] == ':':
            return True
    return False


def main(av: str) -> None:
    hr: str = av[0:2]
    if int(hr) < 12:
        print(f"{av}AM")
    elif int(hr) == 12:
        print(f"{av}PM")
    else:
        hours: dict = {'13': '01', '14': '02', '15': '03', '16': '04',
                       '17': '05','18': '06', '19': '07', '20': '08',
                       '21': '09', '22': '10', '23': '11'}
        for i, j in hours.items():
            if av[0:2] == i:
                hr = j
        print(f"{hr}{av[2:5]}PM")
    

if __name__ == '__main__':
    if verify_args(sys.argv):
        main(sys.argv[1])
    else:
        print("This program needs an entry in the format HH:MM to operate")
