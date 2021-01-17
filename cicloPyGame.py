'''
Ciclo básico de Pygame

-crear pantalla
-rellenar pantalla con un color >> se usan los valores hexadecimales equivalentes a esos colores
-ponemos titulo al programa
>>en este estado aún no funciona porque el programa no está inicializado

-ahora habría que hacer el pygame.init()
-ahora se montaría el ciclo de pintar pantalla> manejar eventos> modificar pantalla (y volver a pintar pantalla)
    >>Para montarlo, primero hay que crear una condición (game over) y metemos un bucle
    >>Gestionar eventos: con un while not game over, cogemos cada evento del buffer/almacen de eventos de pygame, cada uno los procesamos
        Siempre hay un evento que hay que usar por comodidad > .QUIT -para salir-
         (esto serviría para permitir cerrar el juego con la x de la ventana)
        -Salimos del bucle con pygame.quit()
    -Ahora habría que refrescar la pantalla >> dentro del bucle ponemos un pygame.display.flip()/update()
    >>Así saldría la pantalla naranja
    
-sys.exit() # esto cierra pantalla y phyton >> para evitar posibles atascos en el bucle de comprobación


'''

import pygame, sys

width = 640
height = 480

screen = pygame.display.set_mode((width,height)) # esto crea la pantalla con estas medidas
screen.fill((246,147,48)) #esto sería el color naranja
pygame.display.set_caption('Ciclo básico de pygame')

pygame.init()

gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #si el evento es este, se sale del bucle
            gameOver = True
    pygame.display.flip()
pygame.quit()
sys.exit() # esto cierra pantalla y phyton >> para evitar posibles atascos en el bucle de comprobación
