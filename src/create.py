import os
import search

class create:
    """
    Classe permettant de créer une fiche
    >>> fiche=create("Bataille de Marignan","1515","Histoire")
    >>> fiche.createfiche()
    """
    def __init__(self,key, value,theme):
        """
        Constructeur de la classe create
        :param key: (str) clé de la fiche
        :param value: (str) valeur/réponse de la fiche
        :param theme: (str) le thème de la fiche
        :return: None
        :CU: Le thème doit déjà être créé pour y ajouter une fiche
        """
        self.key=key
        self.value=value
        self.theme=theme
        
    def exists(self):
        """
        Retourne si la fiche existe déjà
        :return: (bool) True si elle existe sinon False
        """
        s=search.search(self.key,True,self.theme)
        if s.start()[:6]=="Théme:":
            return True
        else:
            s=search.search(self.value,True,self.theme)
            if s.start()[:6]=="Théme:":
                return True
        return False
    
    def createfiche(self):
        """
        Fonction ajoutant la fiche au theme
        """
        os.system("clear")
        path="theme/"+self.theme
        e=self.exists()
        if (os.path.exists(path))and not e:
            with open(path, 'a') as f:
                ligne=self.key+':'+self.value+'\n'
                f.write(ligne)
                print("La fiche a bien été créée")
        else:
            if e:
                print("Cette fiche existe déjà\n")
            else:
                print("Ce thème n'existe pas\n")
                print(os.listdir("theme/"))