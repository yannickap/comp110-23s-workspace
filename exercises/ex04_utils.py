""" 'list'Utility Functions."""
__author__ : 730480607

def all(numbers: list[str], value: int) -> bool:
    """Searching for value in list of numbers"""
    length: int = len(numbers)
    count: str = 0
    while count < length:
        if numbers[count] != value:
            print("False")
            return False
        count = count + 1

    print("True")
    return True

def max(input: list[int]) -> int:
    """Searching for max or largest value in list"""
    length_ag: int = len(input)
    count: str = 0   
    res: int = input[0]
    if len(input) == 0:
        raise ValueError("max () is an empty list")
    while count < length_ag:
        if input[count] > res:
            res = input[count]
        count = count + 1

    return res

def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Searching for list of numbers"""
    count: str = 0
    if len(list_one)!= len(list_two):
        print("False")
        return False
    while count < len(list_one):
        if list_one[count] != list_two[count]:
            print("False")
            return False
        count = count + 1

    print("True")
    return True

