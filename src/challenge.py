import os
from random import randint
class challenge:
    """
    Classe permettant la création d'une interrogation
    >>> c=challenge("Test")
    >>> c.start()
    clé:
    """
    
    def __init__(self, theme):
        """
        Fonction de création du challenge
        :param theme: (str) Le thème du challenge
        :CU: Le thème doit exister
        """
        self.theme=theme
        self.cle={}
        self.valeur={}
        
    def start(self):
        """
        Lance le challenge
        :return: (int) le score
        """
        path="theme/"+self.theme
        if (os.path.exists(path)):
            self.creerdico(path)
            return self.startchallenge()
        else:
            print("Ce thème n'existe pas\n")
            print("La liste des thèmes existant:\n"+os.listdir("theme/"))
        
        
    def creerdico(self,path):
        """
        Créer les deux dictionnaires d'interrogation l'un avec les clés en clés l'autre avec les valeurs en clés
        :param path: (str) le chemin vers le theme
        :return: None
        :CU: Le theme doit exister
        """
        dic1={}
        dic2={}
        with open(path,"r") as f:
            lignes=f.readlines()
            for i in lignes:
                i=i[:-1]
                tmp=i.split(':')
                dic1[tmp[0]]=tmp[1]
                dic2[tmp[1]]=tmp[0]
        self.cle=dic1
        self.valeur=dic2
    
    def startchallenge(self):
        """
        Lance le challenge
        """
        questionsc=list(self.cle.keys())
        questionsv=list(self.cle.values())
        score=0
        while((questionsv!=list()) or (questionsc!=list())):
            questionsrestante=len(questionsv)+len(questionsc)
            q=randint(0,questionsrestante)-1
            if ((q<len(questionsv))and (questionsv!=list())):
                question=questionsv[q]
                reponse=input(question+': ')
                correction=self.valeur[question]
                if reponse==correction:
                    score+=1
                    print("Bonne réponse")
                else:
                    score-=1
                    print("Mauvaise réponse : "+correction)
                questionsv.remove(question)
            else:
                if(questionsv!=list()):
                    q=q-len(questionsv)
                else:
                    q-=1
                question=questionsc[q]
                reponse=input(question+': ')
                correction=str(self.cle[question])
                if reponse==correction:
                    score+=1
                    print("Bonne réponse")
                else:
                    score-=1
                    print("Mauvaise réponse : "+correction)
                questionsc.remove(question)
            
        return score