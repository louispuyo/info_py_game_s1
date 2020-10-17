# from random import random, randint

# class Enfant:
#     def __init__(self, name:str, age:int):
#         self.name = name
#         self.age = age
#         self.taille = 190
#         self.meteo = "pluie"
#         self.vie = 100


# class Famille(Enfant):
#     def __init__(self):
#         self.enfant_1 = Enfant("Carlos", 12)
#         self.enfant_2 = Enfant("Pablito", 17)

#     def afficher_le_plus_ager(self):
#         if self.enfant_1.age > self.enfant_2.age:
#             enfantGrand = self.enfant_1

#         elif self.enfant_1.age < self.enfant_2.age:
#             enfantGrand = self.enfant_2


#         else:
#             enfantGrand = self.enfant_1

#         return(f"l enfant le plus grand est {enfantGrand.name} et il a {enfantGrand.age} ans")
        

# class Ville(Famille):
#     def __init__(self):
#         self.Famille_1 = Famille()

    

# # def HeavySide(x:float):
# #     """
# #     | si x < 0.5 -> 0
# #     | sinon -> 1
# #     |
# #     """
# #     x = x * random()
# #     if x < 0.5:
# #         return 0
# #     else:
# #         return 1
    
# # print(HeavySide(3))

# # for i in range(10):
# #     print(randint(1, 30)*"-")
# #     print()

# allumettes = 10


# def retirer(nb_input):
#     return allumettes-nb_input

#     """
#     f : nom
#         entree
#         sortie (x, y) 
#     """


# class A:
#     def __init__(self, x):
#         self.x = x

#     def func(self):
#         return self.func2()
    
#     def func2(self):
#         print(self.x*".")





def moyenne(list_de_temp:list) -> float:
    acc = 0
    compteur = 0
    for t in list_de_temp:
        acc += t
        compteur += 1

    if compteur > 0:
        acc = acc/compteur

    return acc


def saisir_temperature() -> float:
    t = 0.0 # temperature
    list_de_temp = [] # 0
    c = 1
    saisie = True
    while saisie: # 'str'
        print(list_de_temp)
        t = input(f"temperature {c} :")
        try:
            t = float(t)
            c += 1
            if type(t) != str:
                list_de_temp.append(t)
        except:
            reponse = input("voulez vous arretez la saisis ? ")
            if reponse in ['yes', 'oui']:
                saisie = False
            else:
                print("on continue ... ")

           
    moyenne_des_notes = moyenne(list_de_temp)
    return moyenne_des_notes


print(saisir_temperature())


