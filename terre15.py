import sys


def ca_len(arg) -> int:
    length: int = 0
    for i in arg:
        length += 1
    return length


def main() -> None:
    print("J'ai terminé l'Epreuve de la Terre et c'était stimulant :)")


if __name__ == '__main__':
    if ca_len(sys.argv) == 1:
        main()
    else:
        print("Just turn on the program")
