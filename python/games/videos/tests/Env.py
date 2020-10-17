import pygame
pygame.init()

image_path = "/Users/snowden/Documents/COURS_L1S1/option_info/python/games/videos/tests/img"
data = {"arbre1":{"position":(30, 30), "size":(50, 50), "image":f"{image_path}/arbre1.jpg"}, "arbre2": {"position":(200, 130), "size":(50, 50), "image":f"{image_path}/arbre2.jpg"}}

class Env(object):
    def __init__(self, elements:dict):
        self.elements = elements

        for key in self.elements.keys():
            self.__setattr__("E"+f"_{key}", self.elements[key])


class Image(Env):
    def __init__(self, elements_of_the_env:dict):
        self.Environement = Env(elements_of_the_env) 
        
        for img_key in elements_of_the_env.keys():
            root = elements_of_the_env[f"{img_key}"]
            self.Environement.__setattr__(f"image_{img_key}", 
            self.loader(root["image"], root["size"], root["position"]))
            self.Environement.__setattr__(f"position_{img_key}", root["position"])

    
    def loader(self, image_path:str, size:tuple, position:tuple):
        image = pygame.image.load(image_path).convert().convert_alpha()
        image = pygame.transform.scale(image, size)
        return image




