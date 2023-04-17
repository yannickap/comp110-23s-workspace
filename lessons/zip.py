"""Dict Function Writing"""


# define function
def zip(first: list[str], second: list[int]) -> dict[str, int]:
    keys = first
    values = second
    empty = {}
    none = []
    result: dict(zip(first, second))
    while len(first) != len(second):
        return empty
    
    if first == none:
        return empty
    if second == none:
        return empty
    
    # iterate for matching keys and values
    for key in values:
        keys[key] = values[key]
    
    return result()

