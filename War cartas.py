from random import shuffle

# declaramos variables, para ser utilizados en listas
tipo = '♥ ♠ ♣ ♦'.split()
valor = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

# Clase con las funciones que separan y reordenan la baraja
class Baraja:

    def __init__(self):
        print("Creando nueva baraja...")                               #Crea la baraja
        self.allcards = [(r,s) for s in tipo for r in valor ]

    def shuffle(self):
        print("Mezclando baraja...")                                     #Mezclas la baraja con la funcion suffle de random
        shuffle(self.allcards)

    def dividir_baraja(self):
        return(self.allcards[:26],self.allcards[26:])

# Funciones que repartiran o escojeran las cartas que se jugaran en la mesa, y mantiene un conteo de las cartas
class Mano:

    def __init__(self,cartas):
        self.cartas = cartas

    def __str__(self):
        return "Contaron {} cartas".format(len(self.cartas))

    def add(self,add_cartas):
        self.cartas.extend(add_cartas)            #Añade carta al final de la mano del jugador

    def quitar_cartas(self):
        return self.cartas.pop(0)                 #Extrae la primera carta de la mano del jugador

# Mantiene actulaizado la informacion de cada jugada, con la cantidad actualizada de la mano de cartas de cada jugador
class Jugador:

    def __init__(self,nombre,Mano):
        self.nombre = nombre
        self.Mano = Mano

    def jugada(self):
        carta_seleccionada = self.Mano.quitar_cartas()
        print("{} juega la carta {}".format(self.nombre,carta_seleccionada[0]+' de '+carta_seleccionada[1]))
        print('\n')
        return carta_seleccionada

    def cartas_restantes(self):                    #conteo sencillo de la cantidad de cada maso de cartas
        return len(self.Mano.cartas) != 0

print (" ¡ Que comience el juego ! ")

# declaramos cada baraja o mano de jugador
d = Baraja()
d.shuffle()
half1,half2 = d.dividir_baraja()

# registramos un nombre para competir en el prgrama y reparte su baraja a cada uno
print("Jugara contra el asistente virtual Jarvis")
comp = Jugador("Jarvis",Mano(half1))
nombre = input("¿Cual es su nombre?: ")
user = Jugador(nombre,Mano(half2))

#inicializamos conteo de todas las jugadas
total_rounds = 0
conteo_guerra = 0
cartas_Guerra = []

# el bucle que estara realizando las fucniones de acuerdo a la carta que aparezca
while user.cartas_restantes() and comp.cartas_restantes():

    total_rounds += 1
    #pregunta para decidir si avanzar con el juego, ya que podria ser bastante largo
    salida = input("¿Realizar siguiente jugada? (si/no): ").upper()

   #con un if determinamos la condicion tomada por el usuario de seguir o finalizar el juego

    if salida == "SI":
        print("¡Es hora de una nueva ronda!")
        print("El puntaje actual es: ")
        print(user.nombre + " tiene: " + str(len(user.Mano.cartas)))
        print(comp.nombre + " tiene: " + str(len(comp.Mano.cartas)))
        print("Ambos jugadores juegan una carta")
        print('\n')

        cartas_en_mesa = []

        c_card = comp.jugada()
        p_card = user.jugada()                     #se estan agregando listas para que la cantidad de la mano
                                                   #varie constantemente cada bucle

        cartas_en_mesa.append(c_card)
        cartas_en_mesa.append(p_card)

        if c_card[0] == p_card[0]:
            conteo_guerra += 1

            cartas_Guerra.append(cartas_en_mesa)

        else:
            if valor.index(c_card[0]) < valor.index(p_card[0]):
                print(user.nombre + " Obtuvo la carta mas alta !, se suma a su mano.")
                user.Mano.add(cartas_en_mesa)
            else:
                print(comp.nombre + " Obtuvo la carta mas alta !, se suma a su mano.")
                comp.Mano.add(cartas_en_mesa)
    else:
        print("Gracias por jugar, lo importante es divertirse :,)")
        break                                                               # finalizamos el proceso y saldria del bucle,

#Mensaje para finalizar el juego
print("Excelente Juego, se realizaron "+str(total_rounds) + " jugadas.")
print("hubo "+str(conteo_guerra)+" Guerras.")
