import os
container = {}

# entree = "mustache gringo"
# while entree not in["stop", "", "arrete"]:
#     entree = input("definir un element : ")
#     valeur = input(f"definir une valeur pour {entree} : ")
#     container[entree] = valeur

# print(container)


TCP_SERVER = {"rooter":"0.0.0.0", "port":8888, "broadcast":"255.255.255.255"}
# print(TCP_SERVER["rooter"])

def save():
    with open("save.log", "a+") as File: # a+ creer si il exite pas / si il exite tu va le completer 
        File.write((TCP_SERVER["rooter"]))
        File.close()

def read(File_name:str):
    with open(File_name, "r") as File:
        content = File.read()
        print(content)
        File.close()


List = [1,2,2,3,4]
Str = list("louis")
print(Str)

print(Str[0])



