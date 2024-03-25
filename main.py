class Source(): #penser à préciser ou va la source 
    def __init__(self):
        pass

    def genere_paquets(self):
        return #paquet

class Paquet():
    def __init__(self):
        pass

    def get_donnees(self):
        pass

    def set_donnees(self):
        pass

class Buffer(): #file d'attente
    def __init__(self):
        pass
        #taux d'arrivee
        #taux de transmission B
        #capacité C
    
    def reception(self, paquet):
        #paramètre de poisson à utiliser
        return #paquet

    def transmission(self):
        return True or False #si taux de transmission < taux d'arrivée
    
    def plein(self): #si le buffer est plein 
        return True

    def perte(self, paquet): #si le paquet est perdu
        return True 