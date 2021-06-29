import os

class search:
    """
    Classe qui permet de rechercher une fiche
    """
    def __init__(self,clue, entier="True", theme=""):
        """
        Constructeur de la classe
        :param clue: (str) indice de l'une des faces
        :param entier: (bool) si clue est la face entière à rechercher
        :param theme: (str) le thème où rechercher, si vide recherche dans tous les thèmes
        :CU: None
        """
        self.clue=clue
        self.entier=entier
        self.theme=theme
        
    def contenuTheme(self, path):
        """
        Fonction qui permet d'obtenir tout le contenu d'un thème sous forme de tableau
        :param path: (str) chemin vers le thème
        :return: (array of array) Tableau de chaque fiche
        :CU : Le thème doit exister
        >>> a=search('test')
        >>> a.contenuTheme('theme/Test')
        [['test', 'cle'], ['valeur', 'oui']]
        """
        res=list()
        if (os.path.exists(path)):
            with open(path,"r") as f:
                lignes=f.readlines()
                for i in lignes:
                    i=i[:-1]
                    res.append(i.split(':'))
        else:
            print("Ce thème n'existe pas\n")
        return res
        
    def rechercheDansContenu(self,contenu,theme):
        """
        Recherche la valeur de l'attribut clue dans le contenu
        :param contenu: (array of array) Liste des fiches, correspond au resultat de la fonction contenuTheme
        :param theme: (str) Nom du theme où l'on recherche
        :return: (str) le resultat de toutes les itérations de l'attribut clue
        :CU: NONE
        """
        res=""
        for fiche in contenu:
            if self.entier:
                if self.clue in fiche:
                    res+="Théme: "+theme+' | '+fiche[0]+' : '+fiche[1]+'\n'
            else:
                if (self.clue in fiche[0]) or (self.clue in fiche[1]):
                    res+="Théme: "+theme+' | '+fiche[0]+' : '+fiche[1]+'\n'
        return res
    
    def start(self):
        """
        Lancement de la recherche
        :return: (str) Retourne sous la forme grep (nom du theme resultat)
        """
        res=""
        if self.theme=="":
            themes=os.listdir("theme/")
            for theme in themes:
                contenu=self.contenuTheme("theme/"+theme)
                res+=self.rechercheDansContenu(contenu,theme)
        else:
            contenu=self.contenuTheme("theme/"+self.theme)
            res+=self.rechercheDansContenu(contenu,self.theme)
        if res=="" and self.entier:
                res+="Aucune fiche trouvée, essayer en cherchant des extraits"
        os.system("clear")
        return res