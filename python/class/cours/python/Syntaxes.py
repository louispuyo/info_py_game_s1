from random import random, randint

class Enfant:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        self.taille = 190
        self.meteo = "pluie"
        self.vie = 100


class Famille(Enfant):
    def __init__(self):
        self.enfant_1 = Enfant("Carlos", 12)
        self.enfant_2 = Enfant("Pablito", 17)

    def afficher_le_plus_ager(self):
        if self.enfant_1.age > self.enfant_2.age:
            enfantGrand = self.enfant_1

        elif self.enfant_1.age < self.enfant_2.age:
            enfantGrand = self.enfant_2


        else:
            enfantGrand = self.enfant_1

        return(f"l enfant le plus grand est {enfantGrand.name} et il a {enfantGrand.age} ans")
        

class Ville(Famille):
    def __init__(self):
        self.Famille_1 = Famille()



def HeavySide(x:float):
    """
    | si x < 0.5 -> 0
    | sinon -> 1
    |
    """
    x = x * random()
    if x < 0.5:
        return 0
    else:
        return 1
    
print(HeavySide(3))

for i in range(10):
    print(randint(1, 30)*"-")
    print()