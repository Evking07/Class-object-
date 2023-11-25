#ex 2


class CompteBancaire:
    def __init__(self, nom='Dupont', solde=1000):
        self.nom = nom
        self.solde = solde

    def depot(self,somme):
        self.solde  += somme
    def retrait(self,somme):
        self.solde -= somme

    #affichage de tout
    def affiche(self):
        print("Le solde du compte bancaire de",self.nom,"est de","$", self.solde,"CDN.")

# méthodes __repr__ et __eq__
    def __repr__(self):
        return f'CompteBancaile({self.nom}, {self.solde})'
    def __eq__(self, other):
        return (self.nom == other.nom and
                self.solde == other.solde)

#affichage des attributs
#compte1
compte1=CompteBancaire('Duchmol',800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()

#compte2
compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()

#add monthly reiteration later!
class CompteEpargne(CompteBancaire):
    def __init__(self, taux=0.3//100):
        self.taux = taux

    def changeTaux(self,valeur):
        self.taux = valeur

    def capitalisation(nombreMois):
        for i in range(nombreMois):
            nombreMois+1


