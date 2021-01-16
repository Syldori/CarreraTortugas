'''
PyGame:
Hay dos elemtos clave y necesarios en pygame:
-Primer ciclo: crear pantall, refrescar pantalla y los objetos en ella
-Segundo ciclo: comprobación de eventos > refrescar pantalla; ver si el jugador ha hecho algo
-volvemos a actualizar la pantalla de acueerdo a los eventos/acciones realizadas > objetos cambian según lo que haga el usuario
-luego volveríamos a pintar/refrescar la pantalla


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

-Queda crear una clase runner que tenga como atributo la image, su posición y montarlo de forma que tenga 4 runners

'''

import pygame
import sys

class Game():
    corredores = []
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480)) # le ponemos el valor en un tupla
        pygame.display.set_caption ('Carrera de bichos')
        #cargar la imagen de fondo de la pantalla
        self.background = pygame.image.load('images/background.png') # aqui dentro se le metería la ruta de la imagen
         
        self.runner = pygame.image.load("images/smallball.png")
        
 
    def competir(self):
        x = 0
        hayGanador = False
        
        while not hayGanador:            
            #comprobación de eventos
            for event in pygame.event.get(): #para cada evento en la lista de pygame de eventos. Usamos el get y me deuvuel un iterable con todos los eventos uqe se han producido desde el ultimo get/comprobacion realizada
                if event.type == pygame.QUIT: #este es el evento de salida
                    pygame.quit() # esto es salir a lo bruto. Hay veces que no termina de salir aun ocn esto, importamos sistema y usamos un quit del sistema (no se puede usar normalmente)
                    sys.exit()
        
            #refrescar/renderizar la pantalla
            self.__screen .blit(self.background, (0,0))
            self.__screen.blit(self.runner, (x,240)) #para que aparezca en posición 
            pygame.display.flip()
            
            x += 3
            if x >= 250: #esto es para que si alguna llega a la linea de fin 
                hayGanador = True
            
        pygame.quit()
        sys.exit()
            
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()