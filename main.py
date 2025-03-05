import time
'''Game where two cats can fight each other by doing 3 moves. 
Scratch: random amount of attack. 
Shield: reducing the amount of damage from the next attack (negative will just negate). 
Rage: powerful big attack that can be used once every few moves.'''

class Cat:
    def __init__(self, name, colour, type):
        self.name = name
        self.colour = colour
        self.__type = type
    
    def set_type(self):
        print("There are three types of cat mastery:\n1) Clawstrike\n   ↑ Deal more damage per scratch\n   ↓ 'Rage' used once every 5 moves.\n2) Thunderpurr\n  ↑ 'Rage' used once every 2 moves\n  ↓ 'Shield' effectiveness reduced\n3) Guardtail\n  ↑ 'Shield' effectiveness increased\n  ↓ Decreased overall damage (from both Scratch and Rage)\n\n Please select type: Clawstrike, Thunderpurr or Guardtail.")
        type = input()
        while type.lower().strip() != 'clawstrike' and type.lower().strip() != 'thunderpurr' and type.lower().strip() != 'guardtail':
            print("Sorry, input was invalid. Please type either Clawstrike, Thunderpurr or Guardtail.")
            type = input()
        if type.lower().strip() == 'clawstrike':
            self.__type = 'clawstrike'
        elif type.lower().strip() == 'thunderpurr':
            self.__type = 'thunderpurr'
        elif type.lower().strip() == 'guardtail':
            self.__type = 'guardtail'

    def get_type(self):
        return self.__type
    
def attack(number):
    ...


def make_cat(name, colour):
    return Cat(name, colour, None)

    

def main():
    print("Welcome to battle cats - a game where two cats can battle each other. The aim of the game is to deplete your opponent's HP.\nThere are 3 moves for each turn: scratch, rage and shield.\nScratch deals a random amount of damage.\nRage deals a significant amount of damage but can be used once every few turns only.\nShield reduces the amount of damage recieved by a random amount (can build up).\n\nWith that said, please enjoy!")
    #first player
    print("Please input the first player's name.")
    name = input()
    print("Please input the first player's choice of colour.")
    colour = input()
    cat1 = make_cat(name, colour)
    print("Moving onto cat type...")
    time.sleep(0.5)
    cat1.set_type()
    print(f"{cat1.name.title()}'s mastery type is {cat1.get_type()}")

    #second player
    print("Please input the second player's name.")
    name = input()
    print("Please input the second player's choice of colour.")
    colour = input()
    cat2 = make_cat(name, colour)
    print("Moving onto cat type...")
    time.sleep(0.5)
    cat2.set_type()
    print(f"{cat2.name.title()}'s mastery type is {cat2.get_type()}")
    

if __name__ == "__main__":
    main()