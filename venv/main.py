from colorama import Fore, Back, Style
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    print(Fore.RED + 'some red text')
    print(Back.GREEN + 'and with a green background')
    print(Style.RESET_ALL)
    print('back to normal now')
    r = Rectangle("синий", 3, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()