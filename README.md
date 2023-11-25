# Class-object-


Classes et objets
Objectifs
•Concepts principaux de la conception orientée objets
•Exemple 1: la classe Temps
•Exemple 2: Modifier la classe Temps
•Exercice 1: La classe Voiture
•Exercice 2: La classe Banque

Concepts principaux de la conception orientée objets
•Classe
• Une classe contient des variables (attributs avec des valeurs) et des méthodes 
(opérations qui s’exécutent sur les variables).
• Pensez à la classe come un type de variable complexe qui sert de gabarit pour la 
création d’objets
• L’objet contient des données complexes (plusieurs variable de types différents) ainsi 
que les opérations possibles avec ces variables (les méthodes).
•Objets
• La variable de référence contient l’adresse (la référence) de l’objet.
obj1 = NomDeLaClasse()
obj2 = NomDeLaClasse()
3
Concepts principaux de la conception orientée objets
•La création de l’objet utilise le constructeur qui existe par défaut sans paramètre. 
•Ou on peut définir le constructeur __init__
  obj1 = NomDeLaClasse(arg list)
La fonction du constructeur est d’initialiser les variables de chaque objet.
• Variables d’instance: les variables définies dans la classe et créées à l’intérieur de l’objet.
• Méthodes d’instance: le code qui offre des opérations avec les variables d’objets.
4
Exemple 1: Une classe “Temps” 
•Supposons que nous voulions être capables de travailler avec des valeurs 
représentant le temps avec une seconde de précision.
• Quelles informations avons-nous pour représenter le temps? Comment pouvons-nous les 
garder?
• Quelles seraient les opérations utilisant des valeurs du type « Temps »?
5
Que garder dans “Temps” ?
• Deux entiers:• heure:  le nombre d’heures (0  heure  23)
• minute:  le nombre de minutes (0  minute  59)
• seconde:  le nombre de secondes (0  seconde  59)
class Temps:
   def __init__(self, hh=12, mm=0, s=0):
    '''(Temps)-> None'''
    self.heure = hh
    self.minute = mm
    self.seconde = s
• Y aurait-il d’autres façons?
• Uniquement le nombre de minutes (ou de secondes) depuis minuit?
6
Création d’objets de la classe Temps
(utlise le constructeur __init__)
>>> temps1 = Temps(17,45) # Maintenant nous avons un 
                 # objet Temps qui
                 # contient ? comme valeurs
>>> temps2 = Temps(14, 30, 5) # temps2 est ? 
Le constructeur est utilisé une seule fois pour 
chaque objet, quand on crée l’objet !!!
7
Qu’avons-nous maintenant?
temps1 17
45
heure
minute
temps2 14
30
heure
minute
0
5
seconde
seconde
8
Valeurs pas défaut
9
temps3
17
45
heure
minute
temps4 12
0
heure
minute
0
0
seconde
seconde
>>> temps3 = Temps() 
>>> temps4 = Temps(mm=8)
Changer le temps
>>> temp1.heure = 13   #accès direct
>>> temp1.minute = 20
# ajoute dans la classe Temps
 def setTemps(self, hh=12, mm=0, s=0):
    '''(Temps)-> None'''
    self.heure = hh
    self.minute = mm
    self.seconde = s
>>> temps1.setTemps(19, 45, 3)
10
