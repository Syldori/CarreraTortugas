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
    >le ponemos su imagen/disfraz
    >le damos un atriuto que será su posición
    >otro atributo que será su nombre
    
    >>Método: moverse/avanzar
        -importar random > para importar el simulador de un dado aleatorio
        -para hacerelo avanzar, antes de colocarlo en def competir, en el bucle de while not ganador
            -self.runners[0].avanzar() >> solo con poner esto hace 
            
   >>Se crea el jugador llamándo a la clase en el __init__ de Game()
       -lo inicializamos en la línea inicial como X y en la mitad para Y -por ejemplo)
       -luego lo metemos en la lista de runners
       
    >Hacer varios jugadores:
        -creamos un atributo que se llama lista de dsifraces, sera una tupla con las imagenes de los runners
        -en el init, tras las posiciones x,y
        -creamos una variable para que ponga de forma aleatoria los trajes
        -en el self.custome lo ponemos con formato para que poonga el traje en base a la posción aleatoria en la lista que salió en la variable anterior
        -creamos atributo en Game() con las posiciones Y de los runners
        -creamos atributo en Game() con los nombres
        -para crear los 4, lo hacemos ocn una iteración for i in range(4)
            -itera para que todos empiecen la misma línea X y se ponga en la posición i para la Y
            -les pone el nombre segun la posción i
            -añadir a la lista vacía
        -En la parte de refrescar pantalla en competir, se puede hacer poniendo 4 veces  self.__screen.blit(self.runners[0].custome, self.runners[0].position)
            o con una iteración for runner/item in self.__runners: (no lo hacemos con un in range para evitar problemas por si nos meten un nº de jugadores diferente que el range que hemos pueesto
    
    >Hacer correr a varios personajes
         -crear uan iteración con for runner/item in self.runners:
             poner el metodo avanza()
      >> NO PONEMOS SELF. porque estas son variables que solo existen en competir (no son variables que forman parte de la clase/Game()
          -son variables de usar y tirar, no están siempre presentes
        
-Crear condición de salida/fin para el bucle de competir dentro del for de avanzar()
    >creamos un if de si la posición x del corredor  es mayoro o igual que la linea de meta (finishline)
        haga un print del ganador
        poner a True la condicion de salida
            
--Si queremos que no se acabe abruptamente, se crea un método close(self)
    >lo metemos fuera del while con un for >> cuando salga del while sigo comprobando lso eventos y si el event es QUIT, en vez de hayGanador True, llamamos a close()
'''

import pygame
import sys
import random

class Runner():
    __customes = ('turtle','fish','prawn','moray','octopus')
    
    def __init__(self,x=0,y=0): # le ponemos las coordenadas para poder especifica donde ponerla, 
        
        ixCustome = random.randint(0,4) #esto es para asignar los disfraces de forma aleatoria
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome])) # lo ponemos así para ahorrarnos los .png en la lista de arriba
        self.position = [x,y] # lo dfinimos como una lista para despues poder pedir su posicion y poder cambiarla para que avance
        self.name = "Tortuga"
        
    def avanzar(self): #para que corran las torutgas
        self.position[0] += random.randint(1,6) #modifica la posición de x sumándole un numero aleatorio
        
class Game():
    runners = []
    __posY = (160,200,240,280) # esto será para las posiciones de los runners
    __names = ('A','B','C','D')
    __startLine = 5 
    __finishLine = 620
    
    def __init__(self):
        
        #cargar la imagen de fondo de la pantalla
        self.__screen = pygame.display.set_mode((640,480)) # le ponemos el valor en un tupla             
        self.__background = pygame.image.load('images/background.png') # aqui dentro se le metería la ruta de la imagen
        pygame.display.set_caption ('Carrera de bichos')
        
        for i in range(4): # iteración para crear los jugadores
            theRunner = Runner(self.__startLine,self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner) # esto es para meterlo dentro de la lista runners
        
        #runners.append(Runner(self.__startLine,240)) >> esto hace lo mismo que lo anterior, aunque sin nombre
                
    def close(self): #esto para que no cierre abruptamente
        pygame.quit()
        sys.exit()
        
    def competir(self):
        x = 0
        hayGanador = False
        
        while not hayGanador:            
            #comprobación de eventos
            for event in pygame.event.get(): #para cada evento en la lista de pygame de eventos. Usamos el get y me deuvuel un iterable con todos los eventos uqe se han producido desde el ultimo get/comprobacion realizada
                if event.type == pygame.QUIT: #este es el evento de salida
                    hayGanador = True
                    
            for runner in self.runners:
                runner.avanzar()
                #condicion de salida
                if runner.position[0] >= self.__finishLine: #si la posición x del runner es mayoro o igual que la linea de meta (finishline)
                   print('{} ha ganado'.format(runner.name))
                   hayGanador = True
                      
                      
            #refrescar/renderizar la pantalla
            self.__screen.blit(self.__background,(0,0))
             
            
            for item in self.runners: #lo hacemos así para que recorrar todos los runners en la lista de runners
                self.__screen.blit(item.custome, item.position) #para que aparezca en posición
            
            pygame.display.flip()
        
        #Hay que hacer un bucle infinito de comprobación para evitar que el programa pete por acumular muchos recursos >> el while va sacando los eventos innecesarios
        while True: #ponemos esto es un while para poder usar la X roja para cerrar el juego
            for event in pygame.event.get(): #Cuando llegue al final del while, seguirá comprobando eventos y cerraré solo cuando pulse el QUIT
                if event.type == pygame.QUIT:
                    self.close()
            

            
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()