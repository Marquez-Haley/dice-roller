from dice import Dice

def main():
    print("Welcome to Dice Roller!")
    print("************************")
    print("1. 6 Sided Dice")
    print("2. 20 Sided Dice")
    print("3. Custom dice")
    print("Press any other key to exit.")
    userChoice = input("Select an option to start: ")
   
    if userChoice == '1':
        new_dice = Dice(6)
    elif userChoice == '2':
        new_dice = Dice(20)
    elif userChoice == '3':
       customSides = input("Please input an even number of sides")
       new_dice = Dice(customSides)
    else:
        return()



    while(True):
        print("1. Roll")
        print("2. Clear")
        print("3. Undo Last Roll")
        print("4. Exit")
        diceChoice = input()

        if diceChoice == '1':
            rolledNum = new_dice.roll()
            if(rolledNum == 0):
                print("Dice must be an even number to roll!")
            else:
                print("You rolled: ", rolledNum)
                print("Total: ", new_dice.get_total())
        elif diceChoice == '2':
            new_dice.clear()
            print("Total: ", new_dice.get_total())
        elif diceChoice == '3':
            if new_dice.undo_last_roll():
                print("Total: ", new_dice.get_total())
            else:
                print("Nothing to undo! Try rolling first!")
        elif diceChoice == '4':
            return()
        else:
            print("Not a valid choice!")


if __name__ == "__main__":
    main()