import numpy as np
import random
import webbrowser
from replit import db

# print(np.linalg.solve(str(input("Enter equation: ")), 0))

# Add the following featues:
# Add menu
# Factoring
# Translating between forms (Specifically translating to Vertex Form)
# Completing the square difficult
# Convert to EXE when you're done using Nuitka remember to attch the required modules to it py nuitka --follow-imports chatbot.py --show-progress

form = ""
cliptotwodecimalplaces = True
coefficients = []
global password, name, points, netpoints

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
                                  answer = input("Enter the roots (e.g -2.1 5.4: ")
                                  print(str(results[0]) + " " + str(results[1]))
                                  if (answer == str(results[0]) + " " + str(results[1])):
                                      addPoints(10)
                                      print("Correct!")
                                      print("")
                                      generateProblem()
                                  else:
                                      print("Incorrect!")
                                      print("")


def addPoints(i):
    points += i
    if (i > 1):
        print("+" + str(i) + " Points")
    else:
        print("+1 Point")
    print(points)
    updateDatabase()


def removePoints(i):
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
    db["NumberOfUsers"] = "0"

def Menu():
    while True:
        generateProblem()

def updateDatabase():
  db[code] = [password, name, [points, netpoints]]
  
print(db)
print(db.prefix(""))
eusr = input("Do you already have an account? Y or N: ").upper()
while eusr != "Y" and eusr != "N":
    eusr = input("Do you already have an account? Y or N: ").upper()
if eusr == "Y":
    while True:
        code = int(input("What is your code: "))
        if (True): #Figure out whats wrong with code < int(db["NumberOfUsers"]) and code > 0 and code % 1 == 0 later on
          password = db[str(code)][0]
          name = db[str(code)][1]
          points = db[str(code)][2][0]
          netpoints = db[str(code)][2][1]
          while True:
              inpassword = input("What is your password: ")
              if (inpassword == password):
                  print("Successfully logged in!")
                  print("Points: " + str(points) + "/" + str(netpoints))
                  Menu()
              print("Incorrect!")
else:
    db["NumberOfUsers"] = str(int(db["NumberOfUsers"]) + 1)
    print("An account has been created for you!")
    print("Your code is: " + db["NumberOfUsers"])
    #                                  ["Password", "Name", ["Points", "NetPoints"]]
    db[int(db["NumberOfUsers"]) + 1] = [
        input("What would you like your password to be: "),
        input("What is your first name?"), [0, 0]
    ]
    #Add function that goes to menu here

name = db[code][1]
if (int(db["NumberOfUsers"] <= code)):
    print("Welcome back, " + name + "!")
else:
    db[name] = "0"
    print("Welcome to EZMath, " + name + "!")
    print(db[name])