grille = {
"A" : ["" , "", ""],
"B" : ["" , "" , ""],
"C" : ["" , "" , ""]
}

tour = 0
dernier_joueur = ""
dernier_choix = ""
symbole = "X"

def partie_gagner():
    if grille["A"][0]== grille["A"][1] and grille["A"][0]==grille["A"][2]:
        if len(grille["A"][0]) == 1 and len(grille["A"][1]) == 1 and len(grille["A"][2]) == 1:
            return True
    if grille["B"][0]== grille["B"][1] and grille["B"][0]==grille["B"][2]:
        if len(grille["B"][0]) == 1 and len(grille["B"][1]) == 1 and len(grille["B"][2]) == 1:
            return True
    if grille["C"][0]== grille["C"][1] and grille["C"][0]==grille["C"][2]:
        if len(grille["C"][0]) == 1 and len(grille["C"][1]) == 1 and len(grille["C"][2]) == 1:
            return True
    if grille["A"][0]== grille["B"][0] and grille["A"][0]==grille["C"][0]:
        if len(grille["A"][0]) == 1 and len(grille["B"][0]) == 1 and len(grille["C"][0]) == 1:
            return True
    if grille["A"][1]== grille["B"][1] and grille["A"][1]==grille["C"][1]:
        if len(grille["A"][1]) == 1 and len(grille["B"][1]) == 1 and len(grille["C"][1]) == 1:
            return True
    if grille["A"][2]== grille["B"][2] and grille["A"][2]==grille["C"][2]:
        if len(grille["A"][2]) == 1 and len(grille["B"][2]) == 1 and len(grille["C"][2]) == 1:
            return True
    if grille["A"][0]== grille["B"][1] and grille["A"][0]==grille["C"][2]:
        if len(grille["A"][0]) == 1 and len(grille["B"][1]) == 1 and len(grille["C"][2]) == 1:
            return True
    if grille["A"][2]== grille["B"][1] and grille["A"][2]==grille["C"][0]:
        if len(grille["A"][2]) == 1 and len(grille["B"][1]) == 1 and len(grille["C"][0]) == 1:
            return True



while True:

    #AFFICHE GRILLE
    for element in grille:
        print(grille[element])

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
            tour += 1
        else:
            print("Veuillez choisir une autre case ! ")
    elif son_choix[0] == "B":
        if grille["B"][int(son_choix[1]) -1] == "":
            grille["B"][int(son_choix[1]) -1] += symbole
            tour += 1
        else:
            print("Veuillez choisir une autre case ! ")
    elif son_choix[0] == "C":
        if grille["C"][int(son_choix[1]) -1] == "":
            grille["C"][int(son_choix[1]) -1] += symbole
            tour += 1
        else:
            print("Veuillez choisir une autre case ! ")
    else:
        print("Veuillez choisis une case correct ! (??)")
    
    if tour >= 5:
        if partie_gagner():
            print ("Partie Gagnée! ")
            break

