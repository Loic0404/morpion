grille = {
"A" : ["" , "", ""],
"B" : ["" , "" , ""],
"C" : ["" , "" , ""]
}

tour = 0
dernier_joueur = ""
dernier_choix = ""
symbole = "X"

def est_vide(case):
    if case == "":
        case += symbole
        return
    else: 
        print("Veuillez choisir une autre case ! ")

while True:
    if dernier_joueur == "J1":
        dernier_joueur = "J2"
    else :
        dernier_joueur = "J1"

    son_choix = input("Choisir une case : ")

    if dernier_joueur != "J1":
        symbole = "O"
    else:
        symbole = "X"

    if len(son_choix[1]) > 2 and len(son_choix[1]) < 2:
        print("Veuillez choisis une case correct ! (long)")
    elif int(son_choix[1]) > 3:
        print("Veuillez choisis une case correct ! (height)")
    elif son_choix[0] == "A":
        if grille["A"][int(son_choix[1]) -1] == "":
            grille["A"][int(son_choix[1]) -1] += symbole
        else:
            print("Veuillez choisir une autre case ! ")
    elif son_choix[0] == "B":
        if grille["B"][int(son_choix[1]) -1] == "":
            grille["B"][int(son_choix[1]) -1] += symbole
        else:
            print("Veuillez choisir une autre case ! ")
    elif son_choix[0] == "C":
        if grille["C"][int(son_choix[1]) -1] == "":
            grille["C"][int(son_choix[1]) -1] += symbole
        else:
            print("Veuillez choisir une autre case ! ")
    else:
        print("Veuillez choisis une case correct ! (??)")

    tour += 1

    print(grille)