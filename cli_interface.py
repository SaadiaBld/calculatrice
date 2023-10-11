def affichageCalulette(operateur, num1, num2, resultat) -> str:
    num1 = str(num1)
    num2 = str(num2)
    resultat = str(resultat)

    texte = ""

    artAscii = []
    artAscii.append(" ________________________")
    artAscii.append("/ ,--------------------. \\")
    artAscii.append("| |")
    artAscii.append("| `--------------------' |")
    artAscii.append("|                        |")
    artAscii.append("|                        |")
    artAscii.append("| [7] [8] [9] [C]   [AC] |")
    artAscii.append("|                        |")
    artAscii.append("| [4] [5] [6] [X]    [%] |")
    artAscii.append("|                        |")
    artAscii.append("| [1] [2] [3] [+]    [-] |")
    artAscii.append("|                        |")
    artAscii.append("| [0] [.]  [EXP]     [=] |")
    artAscii.append("\________________________/")

    # HAUT
    for numLigne in range(2):
        texte += "\n" + artAscii[numLigne]

    # NUM1
    strLigne = artAscii[2]
    for colonne in range(19 - len(num1)):
        strLigne += " "
    texte += "\n" + strLigne + num1 + " " + artAscii[2]
    # OPERATEUR
    strLigne = artAscii[2]
    for colonne in range(19 - len(operateur)):
        strLigne += " "
    texte += "\n" + strLigne + operateur + " " + artAscii[2]
    # NUM2
    strLigne = artAscii[2]
    for colonne in range(19 - len(num2)):
        strLigne += " "
    texte += "\n" + strLigne + num2 + " " + artAscii[2]
    # =
    texte += "\n| | ━━━━━━━━━━━━━━━━━━ | |"
    # RESULTAT
    strLigne = artAscii[2]
    for colonne in range(19 - len(resultat)):
        strLigne += " "
    texte += "\n" + strLigne + resultat + " " + artAscii[2]

    # BAS
    for numLigne in range(3, len(artAscii)):
        texte += "\n" + artAscii[numLigne]
    

    return texte