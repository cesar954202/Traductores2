
class token:
    def __init__(self,dato,tipo):
        self.dato = dato
        self.tipo = tipo
        
    def mostrar(self):
        print "Dato: "  , self.dato  , " Tipo: " , self.tipo
        

aux = token("1.1" , 0)

aux.dato = aux.dato + "2"

aux.dato = float(aux.dato)

aux.dato = aux.dato + 1

tokens = []

tokens.append(aux)

for pos in tokens:
    pos.mostrar()
    #aux.dato += 1
    #tokens.append(aux)
    
entrada = 20
estado = 25
if (estado == 25) and (20 != entrada != 21):
    print "Si se valido"


#test = [[0,1,2],
#           [10,11,13],
#           [20,21,22]
#           ]

#estado = 0
#entrada = 0

#salida = 1
#while salida !=0:
    
#Se abre el archivo y se guarda en variable
#entrada = raw_input("Escribe el nombre de archivo: ")
#archivo = open(entrada, "r")
#contenido = archivo.read()
#print contenido

#Pruebas de impresion de posision
#pos = int(input("Imprimir pos: "))
#pos2 = int(input("Imprimir pos2: "))

#imprimir variables
#print "Entrada : ", entrada
#print "Indice es " , indice , "largo" , len(contenido)


