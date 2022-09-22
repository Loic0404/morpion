import random  # Importation de random (générateur de nombre aléatoire)

# Messages
prix = random.randint (30 , 100)
nbr_utilisateur = ""
# Fonctions

def comparer_les_prix(): # Compare les chiffre
    if nbr_utilisateur == prix:
        print (" Vous avez le bon prix ")
        return True
    elif nbr_utilisateur < prix:
        print (" C'est plus ")
        return False
    elif nbr_utilisateur > prix:
        print (" C'est moins ")
        return False
# Création de la boucle

while True:
    nbr_utilisateur = int(input ("Veuillez choisir votre prix compris entre 30 et 100 : "))


    if comparer_les_prix():
        break