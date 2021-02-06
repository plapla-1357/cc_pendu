# coding club 
import random 

list_mot = ["coding club", "manger", "coder", "programe", "bug"]


lettres_trouvés = []
tour = 0

def mot_random():
    nb = random.randint(0,len(list_mot)-1)
    return list_mot[nb]


def mot_j(mot): # crée un mot visble pour le joueur
    motj = ""
    for i in range(len(mot)):
        if not " " in mot[i]:
            motj += "_ "
        else :
            motj += "   "
    return motj

def ajouter_letre(lettre,solution,motj):
    # motj = ""
    for l in range(len(solution)):
        if lettre in solution[l]:
            motj[l] = lettre 

        else:
            motj[l]=  "_ "
    if lettre in solution : 
        lettres_trouvés.append(lettre)      
    return motj
            



def main():#deroulement du jeu
    finis = False
    solution = mot_random() 
    mot_joueur = mot_j(solution)
    print(mot_joueur)
    while not finis:
        letre = input("quelle letre voulez vous mettre :")
        mot_joueur = ajouter_letre(letre,solution,mot_joueur)
        print(mot_joueur)
        


main()

