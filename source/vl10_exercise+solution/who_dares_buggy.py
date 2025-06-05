import os
import random
import sys

turn = True
game = True
counter = 0
goal = 0
numberlist1 = [0, 7]
numberlist2 = [1, 2]
def randomDicing():
    dice = randomNumber()
    return dice


def main():

    while game:
        os.system('cls' if os.name == 'nt' else 'clear')
        counter = 0
        goal = 0

        print("                       Who Dares Win")
        print("")
        print("The aim of the game is to roll the dice as many times as possible, ")
        print("without the total going over 21. Each successful roll you will gain 5 points")
        print("There will be a selection of dices to choose from. all, with different features")
        print("Will you acquire the highest score ?")
        print("")

        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        os.chdir(script_dir)

        with open("highscore.txt", "r") as f:
            
            old_score = f.read()
            print("The highest score is", old_score)
            high_score = int(old_score)

        print("by", oldname)

        while goal < 21:
            dice=0
            while turn:
                decide = input("Pick dice (1,2,3,4,5 or 6): ")
                dice,counter=icydicing(decide,counter)
                break                

            input("Press enter to roll dice")
            print("you rolled a", dice)

            goal += "dice"  # sollte goal += dice sein
            print("The total diced sum is", goal)

            print("The total is", goal)

            counter += 5
            print('your new score (not the diced sum) is ',counter)

            again = input("Keep playing? Y/N ")
            again = again.upper()

            if again == "N":
                break

        if goal > 21:
            print("Sorry you went over 21")
            input("Press enter to exit")
            break

        else:
            new_score = counter
            print("You score", new_score)

            if new_score > old_score:
                print("New record!")


def randomNumber():
    a= randomRandomNumber()
    return a

def randonDicing():
    dice= randonNumber()
    return dice

def randonNumber():
    a= randonRandomNumber()
    return a

def randonRandomNumber():
    a= random.randint(2, 5)
    return str(a)

def icydicing(decide,counter):
    
    if decide == "1":
        dice=randomDicing()
        
    elif decide == "2":
        dice=randonDicing()
        return dice,counter
            
    elif decide == "4":
        dice = random.choice(numberlist2)
        bob = random.randint(2, 4)
        counter -= bob
        print("You lose", bob, "points")
        print('The new score (not the diced sum) is ',counter)
        return dice
    elif decide == "5":
        dice = random.choice(numberlist2)
        bob = random.randint(21, 25)
        counter -= bob
        print("You lose", bob, "points")
        return dice,counter
    
    

def randomRandomNumber():
    a= random.randint(2, -5)
    return a

if __name__ == "__main__":
    main()