""""Wordle"""
__author__ = "730480607"

def contains_char(word_entered: str, sing_character: str) -> bool:
    """Search of the single character in the 1st word provided as true or false"""
    assert len(word_entered) == 1
    searching: int = 0
    while searching < len(word_entered): 
        if word_entered[searching] == sing_character:
            return True
        searching += 1
    return False

def emojified(PLAY_GUESS:str, SECRET:str) -> str:
    """Detect correct emoji color"""
    assert len(PLAY_GUESS) == len(SECRET)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    searching_2: int = 0
    box = ""
    while searching_2 < len(PLAY_GUESS):
        if PLAY_GUESS[searching_2] == SECRET[searching_2]:
            box += GREEN_BOX
       

