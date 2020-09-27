
nom_de_variable <- var1

# s(ALGORITHME) :  nom_du_programme
    ENTREE:
           type: nom_de_variable # type parmis : [entier, reel, ...]
    SORTIE:
           type: nom_de_variable_de_sortie
           text: issue_1
    
    CONSTANTES:
           type: nom_de_la_constante
    
    DEBUT
        issue_1 <- 'vous etes officilement admis'
        ECRIRE('vous ...')

            [...]

    FIN
    


1) STRUCTURE DE SELECTION SIMPLE : 
    SI condition ALORS
        ...
    SINON
        ...
    FINSI


2) OPERATEURS:
    % | modulo
    / | diviser
    ^ | puissance


ex: 
    10 = 3*3 + [1]   # modulo 3 => 10 % 3
    12 = 4*3 + [0]   # modulo 4


3) #! ATTENTION CONDITION D ARRET
    a) TANT QUE n>0 FAIRE
        ...
        n <- n-1

       FINTANTQUE
    
    b) REPETEZ

        LIRE(var)

       TANT QUE condition var < 10
    
var1 <- 1 
var2 <- 4
resultat <- 0
4) POUR compteur DE var1 A var2 FAIRE
    1 resultat <- resulat + 2*compteur = 2
    2 resultat <- 2 + 2*(2) = 6
    3 resultat <- 6 + 3*(2) = 12
    4 resultat <- 12 + 4*(2) = 20

   FINPOUR

# ---- MEME CHOSE

compteur <- var1
TANT QUE compteur < var2
    compteur <- compteur+1
    ...
FINTANTQUE

# ---------------

# CONSIGNE:
3 personnes dans une salle d attentes et tu veux savoir 
si la somme des 3 ages est superieur a 100, si c est le cas afficher 
"ca sens la mort via covid", sinon "ca sens le telechomage"

# =======================================================

s(ALGORITHME): jugement_dernier
    ENTREE:
        reel : age
        reel : compteur
        reel : somme_age


    SORTIE:
        reel : moyenne


    DEBUT:
        somme_age <- 0 # IMPORTANT

        POUR compteur DE 1 A 3 FAIRE
            ECRIRE('saisir age ', compteur)
            LIRE(age)

            somme_age <- somme_age + age # 1 => somme_age = 0
                                         # 2 => somme_age = age

        SI somme_age > 100 ALORS

            ECRIRE('ca sens la mort via covid')
        SINON
            ECRIRE('ca sens le telechomage')

        FINSI


        moyenne <- somme_age/compteur 
        ECRIRE('la moyenne d age est : ', moyenne)

    FIN:


Ex: (REPETEZ
        ...
    TANT QUE condition)


    DEBUT:
        compteur <- 0  # compteur <- 1


        REPETEZ 
            ECRIRE('SALUT')

        TANT QUE compteur < 10 # compteur <= 10




#Consigne:
Algorithme qui me calcul une vitesse en km/h a partir d une vitesse en ms.
si la vitesse en km/h depasse "200 km/h" ecrire "tu va trop vite", sinon ecrire "ca vaaa".

m/s -> km/h il faut faire x3.6


s(ALGORITHME): radar
    ENTREE:
        reel: vitesse
    
    DEBUT
        ECRIRE('entrer la vitesse en m/s : ')
        LIRE(vitesse)
        vitesse <- vitesse * 3.6

        SI vitesse > 200 ALORS
            ECRIRE('tu va trop vite')
        SINON
            ECRIRE('ca vaaaa')
        FINSI
        
    
    FIN


Ecrire un Algorithme qui permet d ajouter (ou de retirer) un certain nombre 
entrer par l utilisateur, tant que le stock est > 0, continuer a demander quel nombre
on veut ajouter (ou retirer)


Algorithme: stock
    ENTREE:
        entier: valeur 
        entier: stock
        
    DEBUT
        stock <- 0

        REPETEZ
            ECRIRE('entrer valeur')
            LIRE(valeur)
            stock <- stock+valeur

        TANT QUE stock >= 0  
    
    FIN


il y a 20 lots dans un boutique, a chaque iteration la boutique
vend 2 lots , afficher l evolution des lots au fils des iterations
nombre_de_lot <= 0