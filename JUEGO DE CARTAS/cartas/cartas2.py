import random
from tkinter import messagebox
print("En caso de no tener carta alguna escribe el numero 100 y conseguirás una carta")

class Carta():
    def __init__(self, palo, numero):
        self.palo = palo
        self.numero = numero

class Baraja():
    def __init__(self):
        self.baraja = []
        self.crear_baraja()


    def crear_baraja(self):
        self.palos = ["Diamantes", "picas", "corazones", "treboles"]
        self.num = [1,2,3,4,5,6,7,10,11,12]
        for p in self.palos:
            
            for n in self.num:
                self.carta = p,n
                self.baraja.append(self.carta)
        random.shuffle(self.baraja)
    def eliminar_carta(self,posicion):
        carta = self.baraja.pop(posicion)
        
        return carta
        
    def enseñar_baraja(self):
        print(self.baraja)
    def baraja(self):
        return self.baraja
    def largo(self):
        return len(self.baraja)
        


class Jugador():
    def __init__(self, nombre):
        self.mano = []
        self.nombre = nombre
        
    def añadir(self,carta):
        if carta != 100:
            self.mano.append(carta)
    def enseñar(self):
        print(f"Cartas {self.nombre}")
        con = 0
        for c in self.mano:
            print(con, c)
            con += 1
    def echar_carta(self):
        posicion = int(input(f"¿En que posción se encuentra la carta que quieres echar {self.nombre}?"))
        if posicion == 100:
            return 100
            pass
            
        c = self.mano[posicion]
        return c
        del c
    def mano(self):
        return self.mano
    def largo_mano(self):
        return len(self.mano)
    
    

class Juego():
    def __init__(self):
        self.baraja_vacía = "no"
        self.baraja = Baraja()
        self.mesa = []
        self.j1 = Jugador("j1")
        self.contrincante = Jugador("Enemigo")
        self.jugar()
        self.ganador = "nadie"
        
        
        
    def añadir_a_mesa(self, carta, jugador):
        if str(carta) != "100":
        
            self.mesa.append(carta[1])
            self.mesa.append(jugador)
        else:
            pass
        print(self.mesa)
    def borrar_mesa(self):
        self.messa.clear()
    def jugar(self):
        no_carta = False
        self.detectar = "si"
        
        print("cartas j1")
        for x in range(0,10):
             
             c = self.baraja.eliminar_carta(x)
             self.j1.añadir(c)
       
        
        self.j1.enseñar()
        print("Cartas contrincante")
        for x in range(0,10):
             
             c = self.baraja.eliminar_carta(x)
             self.contrincante.añadir(c)
        
        
        self.contrincante.enseñar()

        #Caso de turno j1

        e = random.randint(0,2)
        if e == 1:
        
            c = self.j1.echar_carta()
            self.añadir_a_mesa(c, "j1")
                
            c1 = self.contrincante.echar_carta()
            print(c1)
            self.añadir_a_mesa(c,"j1")

            #Detección de ninguna carta
            while c1 == 100:
                print("Pasando")
                if self.baraja.largo() == 0:
                    print("La baraja está vacía")
                    self.baraja_vacía == "sí"
                    self.detectar == "no"

                    
                   
                    
                if c1 != 100:
                    
                        self.añadir_a_mesa(c1, "contrincante")
                        
                elif c1 == 100 and self.baraja_vacía == "no":
                        print("Aquí va una carta")
                        self.mesa.clear()
                        self.añadir_a_mesa(c, "j1")
                        self.contrincante.añadir(c1)
                        self.contrincante.añadir(self.baraja.eliminar_carta(0))
                        self.contrincante.enseñar()
                        c1 = self.contrincante.echar_carta()
                no_carta == True
                        
                    
               
                print(self.mesa)
                print(self.mesa[0])
                #Detección de si la carta es menor que la que echó el rival
                while self.mesa[2] < self.mesa[0] and self.detectar == "si" and no_carta == False:
                    
                    print("Ese número es menor que el del rival")
                    self.mesa.clear()
                    self.añadir_a_mesa(c, "j1")
                    self.contrincante.añadir(c1)
                    c1 = self.contrincante.echar_carta()
                    self.añadir_a_mesa(c1, "contrincante")
                self.ganador = "contrincante"
        #Caso rival
        else:
            
            c = self.contrincante.echar_carta()
            self.añadir_a_mesa(c, "contrincante")
                
            c1 = self.j1.echar_carta()
            print(c1)
            self.añadir_a_mesa(c, "j1")

            #Detección de ninguna carta
            while c1 == 100:
               print("Pasando")
               if self.baraja.largo() == 0:
                    print("La baraja está vacía")
                    self.baraja_vacía = "sí"
                    self.detectar = "no"

               
               if c1 != 100:
                    
                        self.añadir_a_mesa(c1, "j1")
               elif c1 == 100 and self.baraja_vacía == "no":
                        print("Aquí va una carta")
                        self.mesa.clear()
                        self.añadir_a_mesa(c, "contrincante")
                        self.j1.añadir(c1)
                        self.j1.añadir(self.baraja.eliminar_carta(0))
                        self.j1.enseñar()
                        c1 = self.j1.echar_carta()

                        no_carta = True
               while self.mesa[2] < self.mesa[0] and no_carta == False and self.detectar == "si":
                        
                        
                        print("Ese número es menor que el del rival")
                        self.mesa.clear()
                        self.añadir_a_mesa(c, "contrincante")
                        self.j1.añadir(c1)
                        c1 = self.j1.echar_carta()
                        self.añadir_a_mesa(c1, "j1")
                        self.ganador = "j1"
                        
                    
               
               print(self.mesa)
               #Detección de si la carta es menor que la que echó el rival

            while self.mesa[2] < self.mesa[0] and no_carta == False and self.detectar == "si":
                        
                        print("Ese número es menor que el del rival")
                        self.mesa.clear()
                        self.añadir_a_mesa(c, "contrincante")
                        self.j1.añadir(c1)
                        c1 = self.j1.echar_carta()
                        self.añadir_a_mesa(c1, "j1")
            self.ganador = "j1"

            while True:
                self.ronda()
    def ronda(self):
            no_carta = False
            if self.ganador == "j1":
                print("J1 ha ganado ahora le toca a el echar carta")
                self.j1.enseñar()
                self.contrincante.enseñar()
                c = self.j1.echar_carta()
                self.añadir_a_mesa(c, "j1")
                    
                c1 = self.contrincante.echar_carta()
                print(c1)
                self.añadir_a_mesa(c,"j1")

                #Caso de turno j1



                #Detección de ninguna carta
                while c1 == 100:
                    print("Pasando")
                    if self.baraja.largo() == 0:
                        print("La baraja está vacía")
                        self.baraja_vacía == "sí"
                        self.detectar == "no"
                    
                    if self.baraja_vacía != "sí":
                            
                            print("Aquí va una carta")
                            self.mesa.clear()
                            self.añadir_a_mesa(c, "j1")
                            self.contrincante.añadir(self.baraja.eliminar_carta(0))
                            self.contrincante.enseñar()
                            c1 = self.contrincante.echar_carta()
                        
                    if c1 != 100:
                        
                            self.añadir_a_mesa(c1, "contrincante")
                            
                    elif c1 == 100:
                            print("Aquí va una carta")
                            self.mesa.clear()
                            self.añadir_a_mesa(c, "j1")
                            self.contrincante.añadir(c1)
                            self.contrincante.añadir(self.baraja.eliminar_carta(0))
                            self.contrincante.enseñar()
                            c1 = self.contrincante.echar_carta()
                            self.ganador = "contrincante"
                    no_carta == True
                        
                            
                        
                   
                    print(self.mesa)
                    print(self.mesa[0])
                    #Detección de si la carta es menor que la que echó el rival
                while self.mesa[2] < self.mesa[0] and self.detectar == "si" and no_carta == False:
                        
                        print("Ese número es menor que el del rival")
                        self.mesa.clear()
                        self.añadir_a_mesa(c, "j1")
                        self.contrincante.añadir(c1)
                        c1 = self.contrincante.echar_carta()
                        self.añadir_a_mesa(c1, "contrincante")
                        self.ganador = "contrincante"
        #Caso rival
            else:
                print("El contrincante ha ganado le toca echar carta")
                self.j1.enseñar()
                self.contrincante.enseñar()
            
                c = self.contrincante.echar_carta()
                self.añadir_a_mesa(c, "contrincante")
                    
                c1 = self.j1.echar_carta()
                print(c1)
                self.añadir_a_mesa(c, "j1")

                #Detección de ninguna carta
                while c1 == 100:
                   print("Pasando")
                   if self.baraja.largo() == 0:
                        print("La baraja está vacía")
                        self.baraja_vacía = "sí"
                        self.detectar = "no"

                   if self.baraja_vacía != "sí":
                            print("Aquí va una carta")
                            self.mesa.clear()
                            self.añadir_a_mesa(c, "contrincante")
                            self.j1.añadir(self.baraja.eliminar_carta(0))
                            self.j1.enseñar()
                            c1 = self.j1.echar_carta()
                   if c1 != 100:
                        
                            self.añadir_a_mesa(c1, "j1")
                   elif c1 == 100:
                            print("Aquí va una carta")
                            self.mesa.clear()
                            self.añadir_a_mesa(c, "contrincante")
                            self.j1.añadir(c1)
                            self.j1.añadir(self.baraja.eliminar_carta(0))
                            self.j1.enseñar()
                            c1 = self.j1.echar_carta()
                   no_carta = True
                            
                        
                   
                   print(self.mesa)
                   #Detección de si la carta es menor que la que echó el rival

                while self.mesa[2] < self.mesa[0] and no_carta == False and self.detectar == "si":
                            
                            print("Ese número es menor que el del rival")
                            self.mesa.clear()
                            self.añadir_a_mesa(c, "contrincante")
                            self.j1.añadir(c1)
                            c1 = self.j1.echar_carta()
                            self.añadir_a_mesa(c1, "j1")
                self.ganador = "j1"
            self.comprobar()
    def comprobar(self):
        if self.j1.largo_mano() == 0:
            messagebox.showinfo("Ganador", "El jugador j1 ha ganado")
        elif self.contrincante.largo_mano() == 0:
            messagebox.showinfo("Ganador", "El contrincante ha ganado")
        

juego = Juego()
#daniel alanes caceres.
