from division import divide as div
from addition import addition as add
from multiplication import multiplication as multi
from soustraction import soustraction as soustract
import bonus
import cli_interface

historique = []

def input_nombres():
    num1 = input("Nombre 1 ?")
    num2 = input("Nombre 2 ?")
    return [num1, num2]


def input_nombre():
    num1 = input("Nombre 1 ?")
    return [num1]

def affichage(operateur, num1, num2, resultat) -> str:
    # print(f"{num1} {operateur} {num2} = {resultat}")
    print(cli_interface.affichageCalulette(operateur, num1, num2, round(resultat,5)))

operation = ""

while operation != "Q":
    print("")
    
    operation = input("Quelle opération voulez-vous faire ?\n'+' => addition\n'-' => soustraction\n'*' => multiplication\n'/' => division\n'Q' => quitter\n\n")

    if operation == "+":
        nombres = input_nombres()
        affichage(operation, nombres[0], nombres[1], add(nombres[0], nombres[1]))
        historique.append("{} {} {} = {}".format(nombres[0],operation,nombres[1],add(nombres[0], nombres[1])))
    elif operation == "-":
        nombres = input_nombres()
        affichage(operation, nombres[0], nombres[1], soustract(nombres[0], nombres[1]))
        historique.append("{} {} {} = {}".format(nombres[0],operation,nombres[1],soustract(nombres[0], nombres[1])))
    elif operation == "*":
        nombres = input_nombres()
        affichage(operation, nombres[0], nombres[1], multi(nombres[0], nombres[1]))
        historique.append("{} {} {} = {}".format(nombres[0],operation,nombres[1],multi(nombres[0], nombres[1])))
    elif operation == "/":
        nombres = input_nombres()
        affichage(operation, nombres[0], nombres[1], div(nombres[0], nombres[1]))
        historique.append("{} {} {} = {}".format(nombres[0],operation,nombres[1],div(nombres[0], nombres[1])))
    elif operation == "%":
        nombres = input_nombres()
        affichage(operation, nombres[0], nombres[1], bonus.modulo(nombres[0], nombres[1]))
        historique.append("{} {} {} = {}".format(nombres[0],operation,nombres[1],bonus.modulo(nombres[0], nombres[1])))
    elif operation == "**":
        nombres = input_nombres()
        affichage(operation, nombres[0], nombres[1], bonus.exponentiel(nombres[0], nombres[1]))
        historique.append("{} {} {} = {}".format(nombres[0],operation,nombres[1],bonus.exponentiel(nombres[0], nombres[1])))
    elif operation == "log":
        nombres = input_nombre()
        affichage(operation, nombres[0], "", bonus.logarithm(nombres[0]))
        historique.append("{} {} = {}".format(operation,nombres[0],bonus.logarithm(nombres[0])))
    elif operation == "Q":
        print("Bye bye !")
    elif operation == "H":
        print(historique)
    else:
        print("Cette opération n'est pas conforme !")
