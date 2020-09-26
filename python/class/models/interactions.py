import pygame
import sys 
pygame.init()
FONT_SIZE = 30


tools = ["wallet","book", "light", "pen", "water", "ration"]
data = [{"c":"dump", "q":"are you real ? ", "ch":["yes", "no", "dont know", "depends"]},
{"c":"intuitive", "q":"a man come do you open the door ?", "ch":["yes", "no", "yes with a gun", "yes but ask before"]}]


class Personality:
    def __init__(self):
        self.dumb = 0
        self.lie = 0
        self.real = 0
        self.coward = 0
        self.intuitive = 0
        self.positive = 0
        self.negative = 0
        self.creative = 0
        self.protector = 0


Mental = Personality() # add the load version


class Destiny:
    def __init__(self, luck=0.45):
        self.luck = luck
        self.choices_history = [] # load a other party

Event = {1:Destiny(), 2:Destiny()}

class Question():
    def __init__(self, text:"", choices:list):
        self.text = text
        self.choices = choices
        self.choices_number = len(choices)
    
    def answer(self, key):
        if key in self.choices:
            return Event[key]



class Answer():
    def __init__(self, Class:str, question:str, choices:list, i:int):
        self.myfont = pygame.font.Font(None, FONT_SIZE)
        self.Class = Class
        self.q = Question(question, choices)
        # self.display(i)
        self.screen = pygame.display.set_mode((1000, 500))
        # self.rep = self.reponse()
        # self.choice = self.purcent()
        # self.fill = Mental.__setattr__(self.Class, Mental.dumb+self.choice)
        self.running = True


    def reponse(self):
        c = int(input())
        return c


    def str_(self, i):
        return f"{self.q.text}"

    def str_1(self):
        return f"1:{data[i]['ch'][0]}"

    def str_2(self):
        return f"2: {data[i]['ch'][1]}"


    def str_3(self):
        return f"3: {data[i]['ch'][2]}"


    def str_4(self):
        return f"4: {data[i]['ch'][3]}"


    def display(self, i):
        print(f"{self.q.text} : \n \n 1: {data[i]['ch'][0]} \n 2: {data[i]['ch'][1]} \n 3: {data[i]['ch'][2]} \n 4: {data[i]['ch'][3]} \n")

    def display_pygame(self):
        """ import pygame ... """
        # while self.running:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             self.running = False
        #             sys.exit()
                
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_1:
        #                 self.purcent(1)

                    
        #             if event.key == pygame.K_2:
        #                 self.purcent(2)

        #             if event.key == pygame.K_3:
        #                 self.purcent(3)

        #             if event.key == pygame.K_4:
        #                 self.purcent(4)
                    
                    
                    


        content = self.myfont.render(self.str_(i), True, (244,244,244), (0, 0, 100))

        rep_1 = self.myfont.render(self.str_1(), True, (255, 233, 190), (0, 0, 100))
        rep_2 = self.myfont.render(self.str_2(), True, (255, 233, 190), (0, 0, 100))
        rep_3 = self.myfont.render(self.str_3(), True, (255, 233, 190), (0, 0, 100))
        rep_4 = self.myfont.render(self.str_4(), True, (255, 233, 190), (0, 0, 100))

        self.screen.blit(content, (50, 50))
        self.screen.blit(rep_1, (50, 80))
        self.screen.blit(rep_2, (50, 110))
        self.screen.blit(rep_3, (50, 140))
        self.screen.blit(rep_4, (50, 170))

        pygame.display.update()
        
        

    def purcent(self, rep):
        if rep == 1:
            return 0.3
        elif rep == 2:
            return 0.6
        elif rep == 3:
            return -0.3
        else:
            return -0.6
        

i = 0
running = True
while i < len(data):
    Answer(f"{data[i]['c']}", f"{data[i]['q']}", f"{data[i]['ch']}", i).display_pygame()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print("1")
                i+=1

            
            if event.key == pygame.K_2:
                print("2")
                i+=1

            if event.key == pygame.K_3:
                print("3")
                i+=1

            if event.key == pygame.K_4:
                print("4")
                i+=1
                
            
            
                        
