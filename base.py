from division import divide as div
from addition import addition as add
from multiplication import multiplication as multi

# from addition import addition as addition
from soustraction import soustraction as soustraction
# from multiplication import multiplication as multiplication
# from division import division as division
import cli_interface

def input_nombres():
    num1 = input("Nombre 1 ?")
    num2 = input("Nombre 2 ?")
    return [num1, num2]

def affichage(operateur, num1, num2, resultat) -> str:
    # print(f"{num1} {operateur} {num2} = {resultat}")
    print(cli_interface.affichageCalulette(operateur, num1, num2, round(resultat,5)))

operation = ""

while operation != "Q":
    print("")
    
    operation = input("Quelle opération voulez-vous faire ?\n'+' => addition\n'-' => soustraction\n'*' => multiplication\n'/' => division\n'Q' => quitter\n\n")

    if operation == "+":
        print("")
    elif operation == "-":
        nombres = input_nombres()
        affichage(operation, nombres[0], nombres[1], soustraction(nombres[0], nombres[1]))
    elif operation == "*":
        print("")
    elif operation == "/":
        print("")
    elif operation == "Q":
        print("Bye bye !")
    else:
        print("Cette opération n'est pas conforme !")
