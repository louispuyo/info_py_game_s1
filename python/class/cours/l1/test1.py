

def testCovid():
    print("saisir age 1 \n")
    print("saisir age 2 \n")
    print("saisir age 3 \n")
    
    age = int(input()) # LIRE
    if age > 100: # SI
        print("covid")
    else: # SINON
        print("tele..")



# testCovid()

def Test():
    somme_age = 0
    for compteur in range(1,10):
        age = int(input(f"saisir age {compteur} : "))
        somme_age = somme_age + age

    if somme_age > 100:
        print("t as le covid frere")
    else:
        print("okml telechomage tu connais on est la")




# Test()


def f(x):
    reste = x % 2
    if reste == 0:
        print(x, "est paire le reste est 0")
    
    else:
        print(x, "est impaire", "et le reste est 1")

f(7)


ALGORTMIQUE: PAIRE

    ENTREE:
        entier: x

    SORTIE:
        entier: reste


    DEBUT





