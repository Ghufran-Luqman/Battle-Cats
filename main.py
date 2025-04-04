import time
import random
'''Game where two cats can fight each other by doing 3 moves. 
Scratch: random amount of attack. 
Shield: reducing the amount of damage from the next attack (negative will just negate). 
Rage: powerful big attack that can be used once every few moves.'''

class Cat:
    hp = 100
    shield = 0
    def __init__(self, name, colour, type, turns):
        self.name = name
        self.colour = colour
        self.__type = type
        self.turns = 4
    
    def set_type(self):
        print("There are three types of cat mastery:\n1) Clawstrike\n   ↑ Deal more damage per scratch\n   ↓ 'Rage' used once every 5 moves.\n2) Thunderpurr\n  ↑ 'Rage' used once every 2 moves\n  ↓ 'Shield' effectiveness reduced\n3) Guardtail\n  ↑ 'Shield' effectiveness increased\n  ↑ Increased hp\n  ↓ Decreased overall damage (from both Scratch and Rage)\n\n Please select type: Clawstrike, Thunderpurr or Guardtail.")
        type = input()
        while type.lower().strip() != 'clawstrike' and type.lower().strip() != 'thunderpurr' and type.lower().strip() != 'guardtail':
            print("Sorry, input was invalid. Please type either Clawstrike, Thunderpurr or Guardtail.")
            type = input()
        if type.lower().strip() == 'clawstrike':
            self.__type = 'clawstrike'
            self.turns = 6
        elif type.lower().strip() == 'thunderpurr':
            self.__type = 'thunderpurr'
            self.turns = 3
        elif type.lower().strip() == 'guardtail':
            self.__type = 'guardtail'
            self.hp += 20

    def get_type(self):
        return self.__type

def deal_damage(cat2, lower_bound, upper_bound):
    damage = random.randint(lower_bound, upper_bound)
    print(f"total damage being dealt: {damage}")
    print(f"opponent's shield: {cat2.shield}")
    damage = damage - cat2.shield
    if damage < 0:
        cat2.shield = damage * -1
        damage = 0
    return damage

def add_shield(tempcat, lower_bound, higher_bound):
    shield = random.randint(lower_bound, higher_bound)
    tempcat.shield += shield

def claw(cat1, cat2):
    #check cat's type and adjust amount of damage dealt per type
    if cat1.get_type() == 'clawstrike':
        damage = deal_damage(cat2, 15, 17)#median is 16
    elif cat1.get_type() == 'thunderpurr':
        damage = deal_damage(cat2, 10, 16)#median is 13
    elif cat1.get_type() == 'guardtail':
        damage = deal_damage(cat2, 7, 12)#median is 10
    else:
        return "Error, something wrong with the mastery type."
    cat2.hp -= damage
    return f"{cat2.name.title()} took {damage} damage! Their HP is now {cat2.hp}."#need to redirect to hp checker function

def rage(cat1, cat2):
    #checks cat types
    if cat1.get_type() == 'clawstrike':
        damage = deal_damage(cat2, 15, 30)#median is 23
    elif cat1.get_type() == 'thunderpurr':
        damage = deal_damage(cat2, 15, 30)#median is 23
    elif cat1.get_type() == 'guardtail':
        damage = deal_damage(cat2, 10, 25)#median is 18
    else:
        return "Error, something wrong with the mastery type."
    cat2.hp -= damage#deals damage
    return f"{cat1.name.title()} is enraged! {cat2.name.title()} took {damage} damage! Their HP is now {cat2.hp}."

def shield(tempcat):
    if tempcat.get_type() == 'clawstrike':
        add_shield(tempcat, 5, 11)#median is 8
    elif tempcat.get_type() == 'thunderpurr':
        add_shield(tempcat, 2, 8)#median is 5
    elif tempcat.get_type() == 'guardtail':
        add_shield(tempcat, 10, 20)#median is 15
    else:
        return "Error, something wrong with the mastery type."
    return f"{tempcat.name.title()}'s shield is now {tempcat.shield}."

def make_cat(name, colour):
    return Cat(name, colour, None, 3)

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
    print("\n\n\nPlease input the second player's name.")
    name = input()
    print("Please input the second player's choice of colour.")
    colour = input()
    cat2 = make_cat(name, colour)
    print("Moving onto cat type...")
    time.sleep(0.5)
    cat2.set_type()
    print(f"{cat2.name.title()}'s mastery type is {cat2.get_type()}")

    #battle
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    while cat1.hp > 0 or cat2.hp > 0:
        #first player's turn
        canChooseRage = False
        cat1.turns -= 1
        if cat1.turns > 0:
            print(f"\n\n\n\n\n\nIt's {cat1.name.title()}'s turn.\nHP: *{cat1.hp}*\nShield: *{cat1.shield}*\nTurns until you can use rage: {cat1.turns}.\nMoves available: claw, shield.\n(type 'info' to see opponent's information)\n")
        elif cat1.turns <= 0:
            canChooseRage = True
            print(f"\n\n\n\n\n\nIt's {cat1.name.title()}'s turn.\nHP: *{cat1.hp}*\nShield: *{cat1.shield}*\nMoves available: claw, rage and shield.\n(type 'info' to see opponent's information)\n")
        choice = input()
        choice = choice.lower().strip()
        while choice != 'claw' and choice != 'rage' and choice != 'shield' or choice == 'rage' and canChooseRage == False or choice == 'info':
            if choice == 'info':
                if cat2.turns > 0:
                    print(f"\nOpponent HP: *{cat2.hp}*\nOpponent shield: *{cat2.shield}*\nTurns left until they can use their rage: *{cat2.turns}*")
                else:
                    print(f"\nOpponent HP: *{cat2.hp}*\nOpponent shield: *{cat2.shield}*\nThey can use their *rage*!")
            elif canChooseRage == False:
                print("Sorry, that input was invalid. Please pick from either claw or shield.")
            else:
                print("Sorry, that input was invalid. Please pick from either claw, rage or shield.")
            choice = input()
        if choice == 'claw':
            message = claw(cat1, cat2)
            print(message)
        elif choice == 'rage':
            usedRage = True
            message = rage(cat1, cat2)
            print(message)
            if cat1.get_type() == 'guardtail':#reset turns till next rage
                cat1.turns = 4
            elif cat1.get_type() == 'clawstrike':
                cat1.turns = 6
            elif cat1.get_type() == 'thunderpurr':
                cat1.turns = 3
            else:
                return "Error, something wrong with the mastery type."
        elif choice == 'shield':
            message = shield(cat1)
            print(message)
        time.sleep(0.4)

        if cat1.hp <= 0 or cat2.hp <=0:
            break

        #second player's turn
        canChooseRage = False
        cat2.turns -= 1
        if cat2.turns > 0:
            print(f"\n\n\n\n\n\nIt's {cat2.name.title()}'s turn.\nHP: *{cat2.hp}*\nShield: *{cat2.shield}*\nTurns until you can use rage: {cat2.turns}.\nMoves available: claw, shield.\n(type 'info' to see opponent's information)\n")
        elif cat2.turns <= 0:
            canChooseRage = True
            print(f"\n\n\n\n\n\nIt's {cat2.name.title()}'s turn.\nHP: *{cat2.hp}*\nShield: *{cat2.shield}*\nMoves available: claw, rage and shield.\n(type 'info' to see opponent's information)\n")
        choice = input()
        choice = choice.lower().strip()
        while choice != 'claw' and choice != 'rage' and choice != 'shield' and choice != 'info' or choice == 'rage' and canChooseRage == False or choice == 'info':
            if choice == 'info':
                if cat1.turns > 0:
                    print(f"\nOpponent HP: *{cat1.hp}*\nOpponent shield: *{cat1.shield}*\nTurns left until they can use their rage: *{cat1.turns}*")
                else:
                    print(f"\nOpponent HP: *{cat1.hp}*\nOpponent shield: *{cat1.shield}*\nThey can use their *rage*!")
            elif canChooseRage == False:
                print("Sorry, that input was invalid. Please pick from either claw or shield.")
            else:
                print("Sorry, that input was invalid. Please pick from either claw, rage or shield.")
            choice = input()
        if choice == 'claw':
            message = claw(cat2, cat1)
            print(message)
        elif choice == 'rage':
            usedRage = True
            message = rage(cat2, cat1)
            print(message)
            if cat2.get_type() == 'guardtail':#reset turns till next rage
                cat2.turns = 4
            elif cat2.get_type() == 'clawstrike':
                cat2.turns = 6
            elif cat2.get_type() == 'thunderpurr':
                cat2.turns = 3
            else:
                return "Error, something wrong with the mastery type."
        elif choice == 'shield':
            message = shield(cat2)
            print(message)
        time.sleep(0.4)

    if cat1.hp <= 0:
        print(f"GAME OVER. {cat2.name.title()} WINS!!")
    elif cat2.hp <= 0:
        print(f"GAME OVER. {cat1.name.title()} WINS!!")
    else:
        print("error, exited while loop unexpectedly")

if __name__ == "__main__":
    main()