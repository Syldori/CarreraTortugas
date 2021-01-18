'''
Hacer carrera pero donde podamos mover corredor por la pantalla

Para que acepte  los comandos KEY hay que importar pygame.locals import * (todo)
-Comprobar si se ha pulsado una tecla
    elif event.type == KEYDOWN: #
    >> dentro de el iremos preguntando si la tecla es == POSICION DE LA CRUCETA, para cad auna de las teclas posibles que queramos
        -para hacer que se mueva arriba, por ejemplo, extraemos la posicon Y del corredor, le añado uno a ese valor, y luego vuelvo a poner ese valor en su posición y
        -.!!!En pygam 
-Hay que hacer que cargue la pantalla y jugador en cada refresco >> sino lo hacemos, no se actualizaría la imagen y quedaría una copia en la posición anterior
-Hacer que el juego se inicie con un click > 
'''

import pygame, sys
from pygame.locals import *
import random

class Runner():
    __customes = ('turtle','fish','prawn','moray','octopus')
    
    def __init__(self,x=0,y=0): # le ponemos las coordenadas para poder especifica donde ponerla, 
        
        ixCustome = random.randint(0,4) #esto es para asignar los disfraces de forma aleatoria
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome])) # lo ponemos así para ahorrarnos los .png en la lista de arriba
        self.position = [x,y]
        self.name = ""
        
class Game():
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480)) # le ponemos el valor en un tupla             
        self.__background = pygame.image.load('images/background.png') # aqui dentro se le metería la ruta de la imagen
        pygame.display.set_caption ('Carrera de bichos')
        
        self.runner = Runner(320, 240) #para que cree un corredor en el centro
        
    def start(self): #iniciar el juego
        gameOver = False
        
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                elif event.type == KEYDOWN:#comprobar si las teclas se han pulsado
                    
                    if event.key == K_DOWN: #si la tecla que pulsamos es abajo
                        runnerY = self.runner.position[1] #variable donde ponemos la posición y del corredor
                        runnerY += 5 #para que la poscion Y se mueva cinco arriba
                        self.runner.position[1] = runnerY #esto es para hacer que se mueva el corredor
                        # self.runner.position[1] += 5 >> esto es exactamente igual a los tres pasos anteriores                    
                   
                    elif event.key == K_UP:
                        self.runner.position[1] -= 5
                    elif event.key == K_LEFT:
                        self.runner.position[0] -= 5
                    elif event.key == K_RIGHT:
                        self.runner.position[0] += 5
                    else:
                        pass
                    
                #Cargar pantalla y la posicion del corredor
                self.__screen.blit(self.__background,(0,0))
                self.__screen.blit(self.runner.custome, self.runner.position) #le pones el disfraz de mi corredor en la posicion de runner
                
                pygame.display.flip() # esto refresca la pantalla

if __name__ == '__main__':
    game = Game()
    pygame.font.init()
    game.start()
    