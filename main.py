from dice import Dice

def main():
    print("Welcome to Dice Roller!")
    print("************************")
    print("1. 6 Sided Dice")
    print("2. 20 Sided Dice")
    print("3. Custom dice")
    userChoice = input("Select an option to start: ")
   
    if userChoice == '1':
        new_dice = Dice(6)
    elif userChoice == '2':
        new_dice = Dice(20)
    else:
       customSides = input("Please input an even number of sides")
       new_dice = Dice(customSides)


    while(True):
        print("1. Roll")
        print("2. Clear")
        print("3. Exit")
        diceChoice = input()

        if diceChoice == '1':
            rolledNum = new_dice.roll()
            if(rolledNum == 0):
                print("Dice must be an even number to roll!")
            else:
                print("You rolled: ", rolledNum)
                print("Total: ", new_dice.total)
        elif diceChoice == '2':
            new_dice.clear()
        else:
            break


if __name__ == "__main__":
    main()