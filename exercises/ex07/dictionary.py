"""Dictionary Functions"""
__author__ = "730480607"

def invert(ex: dict[str, str]) -> dict[str, str]:
    """Return a dictionary that inverts or reverses the keys and values"""
    entered_dict = {}
    for key, value in ex.items():
        entered_dict[value] = key
    return entered_dict

def favorite_color(fav: dict[str, str]) -> str:
    """Reading number of times individual color appears"""
    number = {}
    for color in fav.values():
        number[color] = number(color) + 1

    """Find most numerous color"""
    count = 0
    most_color = ""
    for color, num in number.items():
        if  num > count:
            count = num


def count(entered: list[str]) -> dict[str, int]:
    """key is unique value in given list and value is count of times"""
    empty = {}
    for i in entered:
        if (i in empty):
            empty[i] += 1
        else:
            empty[i] = 1

