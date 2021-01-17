'''
PyGame:
Hay dos elemtos clave y necesarios en pygame:
-Primer ciclo: crear pantall, refrescar pantalla y los objetos en ella
-Segundo ciclo: comprobación de eventos > refrescar pantalla; ver si el jugador ha hecho algo
-volvemos a actualizar la pantalla de acueerdo a los eventos/acciones realizadas > objetos cambian según lo que haga el usuario
-luego volveríamos a pintar/refrescar la pantalla

- En pygames el punto 0,0 no se encuentra en el medio, si no que está en la esquina izquierda superior


-en el init tendremos que hacere un bucle 'while not game over' y hay que hacer 2 cosas:
    -comprobar los eventos (si no hacemos este, se bloquea) >> nada más inicir con init, el juego se pondrá a comprobar lo que hace/evento el jugador
        >>tb hay que salir de la comprobación de eventos porque si no se queda en un bucle ya que el sistema se queda escuchando continuamente a que se produzcan eventos
            y acaba llenándose el buffer de eventos y se peta
    -refrescar/renderizar la pantalla

-Crear el competir
    -comprobador de eventos con el for event
    -renderizado/escribir la pantalla
        >le pedimos que nos pinte la imagen del fondo y con que coordenadas de la pantalla (con .blit)
            -en pygame la coordenada 0,0 es la esquina arriba izquierda
        >tras pintar, tiene que refrescar la pantalla con .flip()

-Crear un atributo que sea runner(tortuga) que sea una imagen
    -cargamos la imagen con .image.load

-Queda crear una clase runner que tenga como atributo la imagen, su posición y montarlo de forma que tenga 4 runners
    >su init incluye x,y para poder posicionarla
    >le ponemos su imagen
    >le damos un atriuto que será su posición
    >otro atributo que será su nombre
    
    >>Método: moverse/avanzar
        -importar random > para importar el simulador de un dado aleatorio
        -para hacerelo avanzar, antes de colocarlo en def competir, en el bucle de while not ganador
            -self.runners[0].avanzar() >> solo con poner esto hace 
            
   >>Se crea el jugador llamándo a la clase en el __init__ de Game()
       -lo inicializamos en la línea inicial como X y en la mitad para Y -por ejemplo)
       -luego lo metemos en la lista de runners
       
    
        
-Crear condición de salida/fin para el bucle de competir:
    >creamos un if de si la posición x del corredor 1 es mayoro o igual que la linea de meta (finishline)
        haga un print del ganador
        poner a True la condicion de salida
            

'''

import pygame
import sys
import random

class Runner():
    def __init__(self,x=0,y=0): # le ponemos las coordenadas para poder especifica donde ponerla 
        self.custom = pygame.image.load("images/turtle.png")
        self.position = [x,y] # lo dfinimos como una lista para despues poder pedir su posicion y poder cambiarla para que avance
        self.name = "Tortuga"
        
    def avanzar(self): #para que corran las torutgas
        self.position[0] += random.randint(1,6) #modifica la posición de x sumándole un numero aleatorio
        
class Game():
    runners = []
    __startLine = 5 
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480)) # le ponemos el valor en un tupla        
                
        #cargar la imagen de fondo de la pantalla
#         self.__screen.fill((0,255,0)) # esto sería para poner el fondo de pantalla de un color
        self.__background = pygame.image.load('images/background.png') # aqui dentro se le metería la ruta de la imagen
        pygame.display.set_caption ('Carrera de bichos')
        
        firstRunner = Runner(self.__startLine,240,)
        firstRunner.name = "S"
        self.runners.append(firstRunner) # esto es para meterlo dentro de la lista runners
        
        #runners.append(Runner(self.__startLine,240)) >> esto hace lo mismo que lo anterior, aunque sin nombre
                
 
    def competir(self):
        x = 0
        hayGanador = False
        
        while not hayGanador:            
            #comprobación de eventos
            for event in pygame.event.get(): #para cada evento en la lista de pygame de eventos. Usamos el get y me deuvuel un iterable con todos los eventos uqe se han producido desde el ultimo get/comprobacion realizada
                if event.type == pygame.QUIT: #este es el evento de salida
                    pygame.quit() # esto es salir a lo bruto. Hay veces que no termina de salir aun ocn esto, importamos sistema y usamos un quit del sistema (no se puede usar normalmente)
                    sys.exit()
                    
            self.runners[0].avanzar()
            
            if self.runners[0].position[0] >= self.__finishLine: #si la posición x del corredor 1 es mayoro o igual que la linea de meta (finishline)
                print('{} ha ganado'.format(self.runners[0].name))
                hayGanador = True
                      
                      
            #refrescar/renderizar la pantalla
            self.__screen.blit(self.__background,(0,0))
            self.__screen.blit(self.runners[0].custom, self.runners[0].position) #para que aparezca en posición 
            
            pygame.display.flip()
            

            
        pygame.quit()
        sys.exit()
            
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()