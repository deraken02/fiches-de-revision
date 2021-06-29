import search
import create
import challenge
import theme

def main():
    print("[r] Pour commencer à révision")
    print("[s] Rechercher une fiche")
    print("[t] Pour créer un thème")
    print("[f] Pour créer une fiche")
    print("[h] Pour accéder à l'aide")
    print("[q] Pour quitter le logiciel")
    choisi=True
    while(choisi):
        choix=input("Votre choix: ")
        if choix=='r':
            choisi=False
            revise()
        elif choix=='s':
            choisi=False
            recherche()
        elif choix=='t':
            choisi=False
            thème()
        elif choix=='f':
            choisi=False
            fiche()
        elif choix=='h':
            choisi=False
            aide()
        elif choix=="q":
            choisi=False
            end()
        else:
            print("Ce choix n'existe pas")
                
def revise():
    """
    Lance le module de challenge
    """
    ntheme=input("Thème: ")
    c=challenge.challenge(ntheme)
    print("Votre score total est de "+c.start())
    main()

def thème():
    """
    Lance la création d'un thème
    """
    ntheme=input("Thème: ")
    c=theme.theme(ntheme)
    c.createtheme()
    print("Le thème "+ntheme+" a été créé")
    main()

def fiche():
    """
    Lance la création d'une fiche
    """
    encore=True
    ntheme=input("Thème: ")
    while encore:
        face1=input("Première face: ")
        face2=input("Seconde face: ")
        c=create.create(face1,face2,ntheme)
        c.createfiche()
        print("Votre fiche à bien été créé")
        print("Voulez-vous recréer une carte oui [y] ou none [n]")
        if (input()=="n"):
            encore=False
    main()

def recherche():
    """
    Lance la recherche
    """
    clue=input("Terme recherché: ")
    entier=input("Le terme correspond-il à toute la face oui [o] ou non [n]: ")
    theme=input("Recherche dans un thème oui [o] ou non [n]? ")
    entier=entier=="o"
    if theme=="o":
        theme=input("Dans quel thème? ")
    else:
        theme=""
    s=search.search(clue,entier,theme)
    print(s.start())
    main()
    
def aide():
    """
    Affiche l'aide
    """
    print("Cette section est en cours de construction")
    main()

def end():
    """
    Ferme le programme
    """
    return 0
    

print("Bienvenue sur le logiciel de révision")
main()