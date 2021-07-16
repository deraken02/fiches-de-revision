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
        os.system("clear")
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
                if (len(tmp)==2) or (tmp[2]==0):
                    dic1[tmp[0]]=tmp[1]
                    dic2[tmp[1]]=tmp[0]
                else:
                    dic1[tmp[0]]=tmp[1]
        self.cle=dic1
        self.valeur=dic2
    
    def startchallenge(self):
        """
        Lance le challenge
        """
        questionsc=list(self.cle.keys())
        questionsv=list(self.valeur.keys())
        score=0
        i=0
        while((questionsv!=list()) or (questionsc!=list())):
            
            i+=1
            q=list()
            if questionsv!=list():
                q.append(randint(0,len(questionsv)-1))
            else:
                q.append(0)
            if questionsc!=list():
                q.append(randint(0,len(questionsc)-1))
            else:
                q.append(0)
            if questionsv==list():
                sens=1
            elif questionsc==list():
                sens=0
            else:
                sens=randint(0,1)
            if sens==0:
                question=questionsv[q[sens]]
                reponse=input(question+" : ")
                correction=self.valeur[question]
                if correction==reponse:
                    os.system("clear")
                    print("Bonne réponse")
                    score+=1
                else:
                    os.system("clear")
                    print("Mauvaise réponse : "+correction)
                    score-=1
                questionsv.remove(question)
            else:
                question=questionsc[q[sens]]
                reponse=input(question+" : ")
                correction=self.cle[question]
                if correction==reponse:
                    os.system("clear")
                    print("Bonne réponse")
                    score+=1
                else:
                    os.system("clear")
                    print("Mauvaise réponse : "+correction)
                    score-=1
                questionsc.remove(question)
        return str(score)+"/"+str(i)