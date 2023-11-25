#Classes et objets

#ex1
class Voiture:
    def __init__(self, marque='Ford', couleur='rouge'):
        self.marque = marque
        self.couleur = couleur
        self.pilote = 'personne'
        self.vitesse = 0

    def choix_conducteur(self, nom):
        self.pilote = nom

    
    def accelerer(self, taux, duree):
        if self.pilote != 'personne':

            varvit = taux * duree
            self.vitesse += varvit

  
    def affiche_tout(self):
        print(self.marque, self.couleur, "pilotée par",self.pilote, ",","vitesse= ",self.vitesse,"m/s.")

    # méthodes __repr__ et __eq__
    def __repr__(self):
        return f'Voiture({self.marque}, {self.couleur}, {self.pilote}, {self.vitesse})'
    def __eq__(self, other):
        return (self.marque == other.marque and
                self.couleur == other.couleur and
                self.pilote == other.pilote and
                self.vitesse == other.vitesse)

#Affichage des attributs
a1 = Voiture('Peugot', 'Bleue')
a2 = Voiture(couleur='verte')
a3= Voiture('Mercedes')
a1.choix_conducteur('Roméo')
a2.choix_conducteur('Juliette')
a2.accelerer(1.8, 12)
a3.accelerer(1.9, 11)

a2.affiche_tout()
a3.affiche_tout()



