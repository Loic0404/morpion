
grille = {
"A" : ["-" , "-", "-"],
"B" : ["-" , "-" , "-"],
"C" : ["-" , "-" , "-"]
}

tour = 0
dernier_joueur = ""
joueur = ""
symbole = ""

#MESSAGES
message_egalite = "Egalité ! Personne n'a gagné cette fois ci ! "
message_gagnant = "Félicitation {} tu gagne la partie ! "
message_error = "Veuillez renseigner une case correct ! "
message_fill = "Cette case est déjà utilisé ! Veuillez en choisir une autre."
message_play = "{} veuillez choisir une case : "

#

def afficher_grille():
    for ligne in grille:
        for case in ligne:
            print(case)

def verifier_gagant():
    if grille["A"][0] == grille["A"][1] and grille["A"][0] == grille["A"][2]:
        if grille["A"][0] == "-" and grille["A"][1] == "-" and grille["A"][2] == "-":
            return True
    if grille["B"][0] == grille["B"][1] and grille["B"][0] == grille["B"][2]:
        if grille["B"][0] == "-" and grille["B"][1] == "-" and grille["B"][2] == "-":
            return True
    if grille["C"][0] == grille["C"][1] and grille["C"][0] == grille["C"][2]:
        if grille["C"][0] == "-" and grille["C"][1] == "-" and grille["C"][2] == "-":
            return True
    if grille["A"][0] == grille["B"][0] and grille["A"][0] == grille["C"][0]:
        if grille["A"][0] == "-" and grille["B"][0] == "-" and grille["C"][0] == "-":
            return True
    if grille["A"][1] == grille["B"][1] and grille["A"][1] == grille["C"][1]:
        if grille["A"][1] == "-" and grille["B"][1] == "-" and grille["C"][1] == "-":
            return True
    if grille["A"][2] == grille["B"][2] and grille["A"][2] == grille["C"][2]:
        if grille["A"][2] == "-" and grille["B"][2] == "-" and grille["C"][2] == "-":
            return True
    if grille["A"][0] == grille["B"][1] and grille["A"][0] == grille["C"][2]:
        if grille["A"][0] == "-" and grille["B"][1] == "-" and grille["C"][2] == "-":
            return True
    if grille["A"][2] == grille["B"][1] and grille["A"][2] == grille["C"][0]:
        if grille["A"][2] == "-" and grille["B"][1] == "-" and grille["C"][0] == "-":
            return True

def switch_joueur():
    if dernier_joueur == "J1":
        return "J2"
    else :
        return"J1"


while True:

    #AFFICHE GRILLE
    for element in grille:
        print(grille[element])

    if dernier_joueur == "J1":
        symbole = "O"
        joueur = "Joueur n°2"
    else:
        symbole = "X"
        joueur = "Joueur n°1"

    son_choix = input(message_play.format(joueur))

    if len(son_choix) > 2 or len(son_choix) < 2:
        print(message_error)
    elif son_choix[1] != "1" and son_choix[1] != "2" and son_choix[1] != "3":
        print(message_error)
    elif int(son_choix[1]) > 3:
        print(message_error)
    elif son_choix[0] == "A":
        if grille["A"][int(son_choix[1]) -1] == "-":
            grille["A"][int(son_choix[1]) -1] = symbole
            tour += 1
            dernier_joueur = switch_joueur()
        else:
            print(message_fill)
    elif son_choix[0] == "B":
        if grille["B"][int(son_choix[1]) -1] == "-":
            grille["B"][int(son_choix[1]) -1] = symbole
            tour += 1
            dernier_joueur = switch_joueur()
        else:
            print(message_fill)
    elif son_choix[0] == "C":
        if grille["C"][int(son_choix[1]) -1] == "-":
            grille["C"][int(son_choix[1]) -1] = symbole
            tour += 1
            dernier_joueur = switch_joueur()
        else:
            print(message_fill)
    else:
        print(message_error)

    if tour >= 5:
        if verifier_gagant():
            print(message_gagnant.format(joueur))
            break
    if tour == 9:
        print(message_egalite)
        break