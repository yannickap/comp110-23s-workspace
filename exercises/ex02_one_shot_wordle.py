"""EX02 - One Shot Wordle."""
__author__ = "730480607"

SECRET: str = "python"
six_letter_word : str = (input("What is your 6-letter guess? "))
letter_length : int = 6
playing: bool = True
not_it: bool = False
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
j: int = 0
box = ""

#beginning of code
while len(six_letter_word) != len(SECRET):
    six_letter_word = input("That was not 6 letters! Try again: ")

if len(six_letter_word) == len(SECRET):
    while (i < 6):
        if (six_letter_word[i] == SECRET[i]):
            box += (GREEN_BOX)
        else:
            j: int = 0
            exist: bool = False
            while (j < 6):
                if six_letter_word[i] == SECRET[j]:
                    box += (YELLOW_BOX)            
                else:
                    box += (WHITE_BOX)
                j = j + 1   
        i = i + 1
print(box)

if six_letter_word != SECRET:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")