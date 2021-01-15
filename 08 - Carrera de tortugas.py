'''

Haremos una carrera de tortugas usando los objetos de Turtle.

-Hay que hacer un objeto Carrera/Circuito (contendrá cuatro objetos corredores y un objeto pantalla):
  -Atributos:
    *corredores [] cramos con una lista/array
        >> serán cuatro corredores que serán cautro instancias del mismo objeto Turtle()
        >>ponemos una lista donde meteremos a cada uno los corredores
        
        >>Hacerlo con un for i in range(4) para evitar tener que crearlas una a una
            > Esto crea 4 variables con el mismo nombre, pero al meterlas en un lista, se diferencian una de otra por su posicion (corredores[0],etc)
            >>Hay que darles forma con .shape('turtle')   
            >para evitar que pinte la linea que conecta las tortugas con el centro, usamos .penup()
        
        >>Hay que determinar la línea de salida y la línea de llegada.
            -tenemos siempre en cuenta el tamaño de la pantalla
            -será un atributo privado : .__startLine
            -hacemos que se posicione la línea de salida en -width/2 +20 (negativo porque es a la izquierda y partido de dos porque está en la mitad de la izquierda y + 20 para que no inice ne la liena justa)
            - al revés con la finishLine
            
        >>Posicionar las tortugas:
            >en default las pone en la posición 0,0
            >Hay que llevarlas a la linea de salida desdes posicioens diferentes
            > usamos .setpos(linea de inicio -que sería la x-, posicion y)
            > para centrarlas, creamos una tupla con las posiciones de la 'y' (__posStartY)
            
                
    *pantalla (será el recuadro donde se van a mover)
        >>para que pinte en pantalla, tomamos del módulo turtle el screen
        >>pantalla será entonces un objeto con el objeto turtle.Screen()
        >>el problema es que nos crea la pantalla, pero no al tamaño que queremos
        >>por eso hay que poner los parámetros de width, heigth en screen
        >Le ponemos color >> creando una tupla con los colores y luego llamándola segun posicion
 
 --- Diferenciamos el circuito de los corredores   
  
  -modulo:
    *competir()
        -Queremos que las tortugas avancen por turno, pero un poco aleatorio
        -Creamos un bucle y en cada bucle, cada uno de los objetos hace una acción
        -El bule terminará cuando una de ellas llegue a la linea de fin
        -Será un bule while
            -cada tortuga lanzará un dado y avance lo que salga
            -Con un For hacemos que recorra las lista de corredores y que cada tortuga lance y avance
            -la condición de salida será que una de ellas llegue al final    
        -Hacer un dado:
            -importar la librería random
            -usamos .randint(numero, numero) 
        -Para la carrera:
            -creamos la variable hayGanador, y lo ponemos False, para que cuando sea True, finalice el while
            -Para hacerlo True, hacemos un if dentro del for, para que si la posición X de tortuga llega, termine
                -usamos .position() > esto nos da la posicion en una tupla
                -para sacar la coordenada X, pedimos la tortuga.position()[0] 
                
                
'''
import turtle
import random

class Circuito():
    corredores = []
    __posStartY = (-30, -10, 10, 30) #este sería para la posición 'y' de las tortugas
    __colorTurtle = ('red', 'blue', 'green','orange')
    
    #Crear la pantalla, queremos que su tamaño lo podamos definir, con una anchura y altura a determinar)
    def __init__(self, width, height):      
        self.__screen = turtle.Screen() #nos interesa que sea privado, porque si es publico cualquiera puede cambiarlo mientras está en ejecucion
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 20
        
        self.__createRunners () #Hacemos esto para separar la parte de circuito de la de corredores
        
    def __createRunners(self):
        for i in range(4): # este bucle crea los cuatro corredores
            new_turtle = turtle.Turtle()
            new_turtle.color (self.__colorTurtle[i]) # esto es para pintar las tortugas desde su nacimiento, para que no se pongan en negro al principio
            new_turtle.shape('turtle') #esto es para darle forma de tortuga
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i]) # 
                              
            self.corredores.append(new_turtle) # para meter la neuva tortuga en la lista
            
    def competir(self):
        hayGanador = False #esto sería par la condición de salida
        
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1,6) # esta sería la variable para tirar un dado y luego hacer avanzar la tortuga
                tortuga.forward(avance) # esto para que avance el numero que salio en 'avance'
                
                if tortuga.position()[0] == self.__finishLine: #si la posicion X de alguna de las tortugas llega a la posicion de finsihLine, termina la carrera
                    hayGanador = True
                
            

#esto solo se ejecuta si el programa/modulo es main
if __name__ == '__main__': # si esta varaible de mi script es igual a main, es decir, está siendo ejecutada directamente desde la consola
    circuito = Circuito(640,480)
    circuito.competir()
    #Esto es por ejemplo, para evitar que si hacemos un import de circuito, esto ultimo no lo importaría
    # también nos sirve para probar si funciona correctamente    