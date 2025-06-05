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
        print("There will be a selection of dices to choose from. ")
        print("Will you acquire the highest score ?")
        print("")

        # Sicherstellen, dass wir im Skriptverzeichnis arbeiten
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        os.chdir(script_dir)

        #  Fehlerbehandlung: Datei "high.txt"
        try:
            with open("high.txt", "r") as f:
                old_score = f.read()
                high_score = int(old_score.strip())
        except (FileNotFoundError, ValueError):
            high_score = 0
            with open("high.txt", "w") as f:
                f.write("0")

        print("The highest score is", high_score)
        # Fehlerbehandlung: Datei "name.txt"
        try:
            with open("name.txt", "r") as r:
                old_name = r.read().strip()
        except FileNotFoundError:
            old_name = "nobody"
            with open("name.txt", "w") as r:
                r.write("nobody")

        print("by", old_name)
        print("")

        while goal < 21:
            dice = 0  # Initialisierung gegen Referenzfehler

            while turn:
                decide = input("Pick dice (1,2,3 or 4): ").strip()
                dice,counter=icydicing(decide,counter)
                break
            input("Press enter to roll dice")
            print("You rolled a", dice)

            goal += dice
            print("The total diced sum is", goal)

            if goal > 21:
                break  # raus bevor Punkte gezählt werden

            counter += 5
            print('your new score (not the diced sum) is ',counter)

            again = input("Keep playing? Y/N ").strip().upper()
            if again not in ["Y", "N"]:
                print("Invalid input, continuing...")
            if again == "N":
                break

        if goal > 21:
            print("Sorry, you went over 21.")
            input("Press enter to exit")
            break

        else:
            print("You scored", counter)

            if counter > high_score:
                print("Congratulations, you got the highest score!!")
                new_name = input("Enter your name: ").strip()

                with open("name.txt", "w") as name_file:
                    name_file.write(new_name)

                with open("high.txt", "w") as score_file:
                    score_file.write(str(counter))

                print("The new highest score is", counter)
                print("by:", new_name)
            else:
                print("You did not beat the previous highest score of", high_score, "by", old_name)

            again = input("Play again? Y/N ").strip().upper()
            if again != "Y":
                input("Press enter to exit")
                break


def randomNumber():
    a= randomRandomNumber()
    return a

def icydicing(decide,counter):
    
    if decide == "1":
        dice=randomDicing()
        return dice,counter
    elif decide == "2":
        dice = random.randint(1, 6)
        return dice,counter
    elif decide == "4":
        dice = random.choice(numberlist2)
        bob = random.randint(2, 4)
        counter -= bob
        print("You lose", bob, "points")
        print('The new score (not the diced sum) is ',counter)
        return dice,counter
    else:
        print("pfffff, stupid input man! Please choose 1, 2, or 4 next time. I assumed that you meant dice 1")
        dice=randomDicing()
        return dice,counter
    # dice 5 does not make any sense and is deleted

def randomRandomNumber():
    a= random.randint(2, 5)
    return a



if __name__ == "__main__":
    # Code to run when the script is executed directly
    main()