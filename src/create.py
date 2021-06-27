import os

class create:
    """
    Classe permettant de créer une fiche
    >>> fiche=create("Bataille de Marignan","1515","Histoire")
    >>> fiche.createfiche()
    """
    def __init__(self,key, value,theme):
        """
        :param key: (str) clé de la fiche
        :param value: (str) valeur/réponse de la fiche
        :param theme: (str) le thème de la fiche
        :return: None
        :CU: Le thème doit déjà être créé pour y ajouter une fiche
        """
        self.key=key
        self.value=value
        self.theme=theme
        
    def createfiche(self):
        """
        Fonction ajoutant la fiche au theme
        """
        path="theme/"+self.theme
        if (os.path.exists(path)):
            with open(path, 'a') as f:
                ligne=self.key+':'+self.value+'\n'
                f.write(ligne)
        else:
            print("Ce thème n'existe pas\n")
            print(os.listdir("theme/"))