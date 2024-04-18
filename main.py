import time

class Source(): #penser à préciser ou va la source 
    def __init__(self):
        pass

    def genere_paquets(self):
        self.paquet = Paquet()

class Paquet():
    def __init__(self):
        self.donnees = []

    def get_donnees(self):
        return self.donnees

    def add_donnees(self, value):
        self.donnees.append(value)
    
    def del_donnees(self,value):
        self.donnees.remove(value)

    

class Buffer(): #file d'attente
    def __init__(self):
        Buffer.creation_file(self)
        self.taux_arrivee = 2 #nombre de paquets/secondes
        #taux de transmission B
        #capacité C
    
    def creation_file(self) -> None: #fifo
        """
        Création d'une file (FIFO) vide et sauvegarde dans le self\n
        Ne retourne rien
        """
        self.file = []

    def file_vide(self) -> bool:
        """
        Indique si la file de buffer est elle vide ou non\n
        Retourne Vrai si elle vide et Faux sinon
        """
        return True if self.file == [] else False

    def enfiler(self, elm):
        self.file.append(elm)

    def defiler(self):
        if Buffer.file_vide(self):
            return("Il n'y a rien à défiler")
        elm = self.file[0]
        self.file = self.file[1::]
        return elm
        
    def affiche(self):
        b = Buffer
        print(b.file_vide(self))
        print(b.enfiler(self, 100))
        print(b.file_vide(self))
        print(b.defiler(self))
        print(b.defiler(self))
        print(b.file_vide(self))

    def reception(self, paquet):
        time.sleep(1/self.taux_arrivee)
        Buffer.enfiler(self, paquet)
        print(self.file)
        #paramètre de poisson à utiliser

    def transmission(self):
        return True or False #si taux de transmission < taux d'arrivée
    
    """
    def plein(self): #si le buffer est plein 
        return True

    def perte(self, paquet): #si le paquet est perdu
        return True 
    """
buffer1 = Buffer()
buffer1.affiche()