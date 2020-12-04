import numpy as np
import random
import webbrowser
from replit import db
import time

#Link to run
#https://repl.it/@Firerubies/Quadratics-Solver?embed=1&output=1#.replit

# print(np.linalg.solve(str(input("Enter equation: ")), 0))

# Add the following featues:
# Add a shop
# Factoring
# Translating between forms (Specifically translating to Vertex Form)
# Completing the square difficult
# Convert to EXE when you're done using Nuitka remember to attch the required modules to it py nuitka --follow-imports chatbot.py --show-progress
# Fix code always being 1 higher than it should be

form = ""
cliptotwodecimalplaces = True
coefficients = []
password = ""
name = ""
points = 0
netpoints = 0
global vpFirstTime, code


def findRoots():
    for i in range(int(input("How many coefficients are there? "))):
        coefficients.append(
            int(input("Enter coefficient " + str(i + 1) + ": ")))
    results = np.roots(coefficients)
    if (cliptotwodecimalplaces):
        results = np.around(results, 2)
    results = results.tolist()
    for i, *_ in enumerate(results):
        print("X" + str(i + 1) + ": " + str(results[i]))


def convertFormsExplanation():
    if (form == "stv"):
        webbrowser.open(
            'https://virtualnerd.com/algebra-2/quadratics/solve-by-completing-square-roots/complete-square/completing-square-convert-standard-to-vertex',
            new=2)
    elif (form == "vts"):
        webbrowser.open(
            'https://mathbitsnotebook.com/Algebra1/Quadratics/QDVertexForm.html',
            new=2)
    elif (form == "factora1"):
        webbrowser.open(
            'https://www.mathsisfun.com/algebra/factoring-quadratics.html',
            new=2)
    elif (form == "factoranot1"):
        webbrowser.open(
            'https://www.mesacc.edu/~scotz47781/mat120/notes/factoring/trinomials/a_is_not_1/trinomials_a_is_not_1.html',
            new=2)
    addPoints(1)


def generateProblem():
    mode = ""
    while True:
        mode = input("Would you like a to always be 1? Y or N: ").upper()
        if (mode == "N" or mode == "Y"):
            while True:
                while True:
                    if (mode == "N"):
                        rint1 = random.randint(-100, 100)
                    else:
                        rint1 = 1
                    rint2 = random.randint(-100, 100)
                    rint3 = random.randint(-100, 100)
                    results = np.roots([rint1, rint2, rint3])
                    results = np.around(results, 2)
                    results = results.tolist()
                    for i, *_ in enumerate(results):
                        if (str(results[i]).find("j") != -1):
                            break
                        else:
                            while True:
                                while True:
                                    toprint = str(rint1) + "x²+" + str(
                                        rint2) + "x+" + str(rint3)
                                    print(toprint.replace("+-", "-"))
                                    answer = input(
                                        "Enter the roots (e.g -2.1 5.4: ")
                                    if (answer == "menu"):
                                        return
                                    print(
                                        str(results[0]) + " " +
                                        str(results[1]))
                                    if (answer == str(results[0]) + " " + str(
                                            results[1])):
                                        addPoints(10)
                                        print("Correct!")
                                        print("")
                                        generateProblem()
                                    else:
                                        print("Incorrect!")
                                        print("")


def addPoints(i):
    global points, netpoints
    points += i
    netpoints += i
    if (i > 1):
        print("+" + str(i) + " Points")
    else:
        print("+1 Point")
    updateDatabase()


def removePoints(i):
    global points
    points -= i
    if (i > 1):
        print("-" + str(i) + " Points")
    else:
        print("-1 Point")
    updateDatabase()


def deleteAllUsers():
    users = db.prefix("")
    for i in range(0, len(users)):
        del db[users[i]]
        print("Successfully deleted user: " + users[i])
    db["NumberOfUsers"] = "-1"


def Menu():
    #options = ["Generate Problem", "View Points", "Leaderboard", "Shop"]
    options = ["Generate Problem", "View Points", "Leaderboard", "Pet Sim"]
    print("")
    while True:
        for i in range(0, len(options)):
            print(str(i + 1) + ". " + options[i])
        print("")
        while True:
            choice = input("")
            if (choice.isdigit() == True and int(choice) > 0
                    and int(choice) % 1 == 0 and int(choice) <= len(options)):
                if (choice == "1"):
                    generateProblem()
                if (choice == "2"):
                    showPoints()
                if (choice == "3"):
                    leaderboard()
                if (choice == "4"):
                    playPetSimulator()
                else:
                    pass
                Menu()


def updateDatabase():
    global health, energy, hunger, training, pet_food, done_choosing, choice, animal, vpFirstTime
    db[code] = [
        password, name, [points, netpoints],
        [health, energy, hunger, training, pet_food, done_choosing, animal]
    ]


def showPoints():
    print("Points: " + str(points) + "/" + str(netpoints))


def leaderboard_sort(user):
    return user[1]

def playPetSimulator():
    global health, energy, hunger, training, pet_food, things_at_store, done_choosing, animal, vpFirstTime

    if (animal == "" or animal == "None"):
        health = 'good'
        energy = 8
        hunger = 0
        training = 0
        pet_food = 10
        things_at_store = ('bone', 'yarn', 'sunken boat', 'mini cave',
                           'fake tree')
        done_choosing = False
        choice = ""
        addPoints(25)
        animal = 'None'
        print('Welcome to Virtual Pet!')
        print('')
        print('Here are a few pets to choose from.')
        print('')
        print('1. Dog')
        print('2. Cat')
        print('3. Fish')
        print('4. Iguana')
        print('5. Parrot')

        while done_choosing == False:
            print("")
            choice = input('Which do you choose? (enter the number)')
            if choice == '1':
                animal = 'dog'
                done_choosing = True
            elif choice == '2':
                animal = 'cat'
                done_choosing = True
            elif choice == '3':
                animal = 'fish'
                done_choosing = True
            elif choice == '4':
                animal = 'iguana'
                done_choosing = True
            elif choice == '5':
                animal = 'parrot'
                done_choosing = True
            else:
                print(
                    'Sorry, that is not a choice. Please enter something else.'
                )

        pet_name = input("What do you want to name your pet?")
        print('Okay, you now have a', animal, 'named', pet_name + '.')
        print('')
        print('Your', animal, 'is at', health,
              'health right now. You can check it at any time.')

    while True:
        updateDatabase()
        time.sleep(3)
        print("")
        print('1. Feed your pet')
        print('2. Buy more food')
        print('3. Take your pet for a walk')
        print('4. Play a game with your pet')
        print('5. Train your pet')
        print('6. Rest and check stats (pet health, points, etc.)')
        print('7. Buy a toy for your pet')
        choice = input('What would you like to do: ')
        print("")
        if (choice == "menu"):
            return
        if choice == '1':
            if pet_food > 5:
                if hunger > 0:
                    pet_food -= 5
                    hunger -= 1
                    print('Your pet has been fed!')
                    print('You now have ', pet_food,
                          ' pet food, and your pets hunger is at ', hunger,
                          '.')
                else:
                    print(pet_name, 'waits next to the food, not eating.')
            else:
                print("You'll need to get some more food first...")

        elif choice == '2':
            if points > 9:
                removePoints(10)
                pet_food += 5
                print('Food bought! Points = ', points, 'Pet food = ',
                      pet_food)
            else:
                print("You need atleast 10 points to buy some food!")

        elif choice == '3':
            if animal == 'dog' or animal == 'cat':
                if energy > 5:
                    energy -= 3
                    hunger += 1
                    print('You go for a nice walk with your', animal,
                          '. Your pet now has', energy, 'energy and', hunger,
                          'hunger.')
                else:
                    print('Your', animal,
                          'seems a bit too tired to go for a walk today.')
            else:
                print('Your', animal, 'stares at you like you are crazy.')

        elif choice == '4':
            print("You play Unimplemented Feature with your", animal, "!")
        elif choice == '5':
            print("You train your", animal,
                  "in the ways of Unimplemented Feature", "!")

        elif choice == '6':
            print('')
            print('Okay, here are the stats.')
            print('Health:', health)
            print(
                'Pet energy (0-10):',
                energy,
            )
            print(
                'Hunger (0 = full 5 = starving):',
                hunger,
            )
            print(
                'Training (max 10):',
                training,
            )
            print('Pet food:', pet_food)
            print(
                'Points:',
                points,
            )
            energy += 2

        elif choice == '7':
            print('Here are the items at the store:', things_at_store)

        else:
            print('Sorry, that is not a choice. Please enter something else.')


# def shop():
#   pass

# def buy():
#   pass


def leaderboard():
    global users
    users = []
    for i in range(1, int(db["NumberOfUsers"]) + 2):
        users.append([db[str(i)][1], db[str(i)][2][1]])
    users.sort(key=leaderboard_sort, reverse=True)
    for iii in range(len(users)):
        print(str(iii + 1) + ". " + str(users[iii][0]) + " - " + str(users[iii][1]))


eusr = input("Do you already have an account? Y or N: ").upper()
while eusr != "Y" and eusr != "N":
    eusr = input("Do you already have an account? Y or N: ").upper()
if eusr == "Y":
    while True:
        code = int(input("What is your code: "))
        if (
                True
        ):  #Figure out whats wrong with code < int(db["NumberOfUsers"]) and code > 0 and code % 1 == 0 later on
            password = db[str(code)][0]
            name = db[str(code)][1]
            points = db[str(code)][2][0]
            netpoints = db[str(code)][2][1]
            health = db[code][3][0]
            energy = db[code][3][1]
            hunger = db[code][3][2]
            training = db[code][3][3]
            pet_food = db[code][3][4]
            things_at_store = ('bone', 'yarn', 'sunken boat', 'mini cave',
                               'fake tree')
            done_choosing = db[code][3][5]
            choice = ""
            animal = db[code][3][6]
            while True:
                inpassword = input("What is your password: ")
                if (inpassword == password):
                    print("Welcome back, " + name + "!")
                    addPoints(1)
                    Menu()
                print("Incorrect!")
else:
    db["NumberOfUsers"] = str(int(db["NumberOfUsers"]) + 1)
    print("An account has been created for you!")
    print("Your code is: " + str(int(db["NumberOfUsers"]) + 1))
    #                                  ["Password", "Name", ["Points", "NetPoints"]]
    ipassword = input("What would you like your password to be: ")
    while len(ipassword) > 10:
        ipassword = input(
            "Please try to keep your password under 10 characters!")
    iname = input("What is your first name?")
    while iname.isalnum() == False:
        iname = input("Only letters please!")
    code = int(db["NumberOfUsers"]) + 1
    db[int(db["NumberOfUsers"]) + 1] = [
        ipassword, iname, [0, 0], ["None", 0, 0, 0, 0, False, ""]
    ]
    password = db[str(code)][0]
    name = db[str(code)][1]
    points = db[str(code)][2][0]
    netpoints = db[str(code)][2][1]
    health = db[code][3][0]
    energy = db[code][3][1]
    hunger = db[code][3][2]
    training = db[code][3][3]
    pet_food = db[code][3][4]
    done_choosing = db[code][3][5]
    animal = db[code][3][6]
    Menu()