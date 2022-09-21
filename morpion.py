grille = {
"A" : ["A1" , "A2", "A3"],
"B" : ["B1" , "B2" , "B3"],
"C" : ["C1" , "C2" , "C3"]
}

tour = 0
dernier_joueur = ""

def jouer(var_dernier_joueur):
    if var_dernier_joueur == "J1":
        var_dernier_joueur = "J2"
        print(var_dernier_joueur)
        return var_dernier_joueur
    else :
        var_dernier_joueur = "J1"
        print(var_dernier_joueur)
        return var_dernier_joueur

jouer(dernier_joueur)