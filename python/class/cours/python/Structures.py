
class Joueur:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

j1 = Joueur("gringo", 10, 50)
j2 = Joueur("pablito", 13, 40)

def attack(j1, j2):
    j2.defense = (j2.defense - j1.attack)
    return j2

while (j2.defense > 0):
    print(vars(j2))
    function = {"j1 attack j2":attack}

    function["j1 attack j2"](j1, j2)