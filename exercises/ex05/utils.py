__author__ : "730470607"

def only_evens(numbers: list[int]) -> bool:
    """searching for even numbers in list input"""
    length: int = len(numbers)
    x: int = numbers
    count: str = 0
    while count <= length:
        if numbers[count] % 2 != 0:
            return False
    count = count + 1

    return True
         
simple_numbs: list[str] = [1, 2, 3, 4, 5]
print (only_evens(simple_numbs))

def concat(first: list[int], last: list[int]):
    """creating a new list that combines two separate lists"""
    count: str = 0
    while count <= len(first):
        first.extend(last)
        return True
    count = count + 1

def sub(allnumbs: list[int], start: int, end: int) -> bool:
    """Subsetting lists of numbers to pick out individuals"""
    count: str = 0
    length: int = len(allnumbs)
    while count < len(allnumbs):
