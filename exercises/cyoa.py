"""Choose your own adventure!"""
__author__ = "730480607"

points = 0
emoji: str = "\U00001F62"

def greet():
    player: str = input("Welcome! Please enter your name: ")
    print (f"Welcome to Build your Athlete: Road to an Olympian, {player}! ")

def option_one():
    global points
    print ("You have chosen to play basketball!")
    points += 5

def option_two():
    global points
    print ("You have chosen to play soccer!")
    points += 5

def option_three():
    global points
    print ("You have chosen to run track!")
    points += 5

def option_four():
    global points
    print ("You have chosen to competitively swim!")
    points += 5

def no_adventure_five():
    global points
    print(f"You accumulated {points} points. Play again soon!")

def nike():
    global points
    print("You have chosen Nike as your sponsor!")
    points += 20

def adidas():
    global points
    print("You have chosen Adidas as your sponsor!")
    points += 15

def puma():
    global points
    print("You have chosen Puma as your sponsor!")
    points += 15

def speedo():
    global points
    print("You have chosen Speedo as your sponsor!")
    points += 20

def tyr():
    global points
    print("You have chosen TYR as your sponsor!")
    points += 20

def continent():
    global points
    continent: str = input("Choose a continent to represent! North America, South America, Europe, Africa, Asia, or Oceania: ")
    print (f"You have chosen to represent {continent}!")
    points += 50


def main():
    greet()

    options: str = input("Choose one of the following options: 1, 2, 3, 4. Choose 5 to end the game. ")

    if options == "1":
        option_one()
    else:
        if options == "2":
            option_two()
        else:
            if options == "3":
                option_three()
            else:
                if options == "4":
                    option_four()
                else:
                    if options == "5":
                        no_adventure_five()
                        return points

    sponsor: str = input("Choose a company sponsor: Nike, Adidas, Puma. Choose between Speedo or TYR if you are a swimmer: ")

    if sponsor == "Nike":
        nike()
    else:
        if sponsor == "Adidas":
            adidas()
        else: 
            if sponsor == "Puma":
                puma()
            else:  
                if sponsor == "Speedo":
                    speedo()
                else: 
                    if sponsor == "TYR":
                        tyr()

                
    continent()

    injury: str = input(f"You have picked up an injury in training, and there is a chance you will miss the 2024 Olympics in 1 week!{emoji} Will you choose to sit out, or risk aggravating your injury? Choose sit or risk: ")
        
    if injury == "sit":
        print("You came a long way. Congrats on your journey!")
        return points
    else:
        if injury == "risk":
            print("Good luck on your journey! Go and win gold for your region!!!")
            
            return points
    again = input("Thank you playing! Play again? Choose Yes or No ")

    while True:
        if again == "Yes":
            greet()
    else:
        if again == "No":
            exit()

if __name__ == "__main__":
    main()