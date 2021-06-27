import os

class theme:
    """
    Classe permettant de créer des thèmes spéciaux
    >>> t=theme("Anglais")
    >>> t.createtheme()
    """
    
    def __init__(self, theme):
        """
        Fonction d'initialisation de la classe
        :param theme: (str) nom du thème
        :return: None
        :CU: Le thème ne doit pas exister
        """
        self.theme=theme
        
    def createtheme(self):
        """
        Fonction qui créé un thème ssi il n'existe pas déjà
        """
        path="theme/"+self.theme
        if (os.path.exists(path)):
            print("Ce thème existe déjà choisissez un autre nom ou ajoutez y des cartes")
        else:
            with open (path,"x") as f:
                pass
        