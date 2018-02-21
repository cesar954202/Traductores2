class token:
    def __init__(self,dato,tipo):
        self.dato = dato
        self.tipo = tipo
        
    def mostrar(self):
        print "Dato: "  , self.dato  , " Tipo: " , self.tipo



estados = [[1,4,40,6,40,40,17,11,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[1,4,40,6,40,40,17,11,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,2,39,38],
[3,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38],
[3,4,40,40,40,40,17,11,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,40,5,40,40,40,40,40,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,40,40,40,7,40,40,40,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,8,40,40,40,40,40,40,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,40,40,40,40,9,40,40,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,40,40,40,40,40,10,40,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,40,40,40,40,40,12,40,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,40,40,40,40,40,40,40,13,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,40,40,40,40,40,40,40,40,14,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,40,40,40,40,40,40,15,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,40,40,40,40,40,40,40,40,40,16,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,40,40,40,40,18,40,40,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,40,40,40,40,40,40,40,40,40,40,40,19,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,40,40,40,40,40,20,40,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,4,40,6,40,40,17,11,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[1,4,40,6,40,40,17,11,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[1,4,40,6,40,40,17,11,40,40,40,40,40,40,40,40,0,40,23,24,25,26,31,29,27,36,37,34,39,35,38],
[1,4,40,6,40,40,17,11,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,28,38,38,38,38,38,38],
[1,4,40,6,40,40,17,11,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,30,38,38,38,38,38,38,38],
[1,4,40,6,40,40,17,11,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[1,4,40,6,40,40,17,11,40,40,40,40,40,40,40,40,0,40,23,24,25,32,31,29,27,36,37,34,39,35,38],
[1,4,40,6,40,40,17,11,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[1,4,40,6,40,40,17,11,40,40,40,40,40,40,40,40,0,40,23,24,25,32,31,29,27,36,37,34,39,35,38],
[1,4,40,6,40,40,17,11,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[1,4,40,6,40,40,17,11,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[1,4,40,6,40,40,17,11,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[1,4,40,6,40,40,17,11,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38],
[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,0,40,23,24,25,33,31,29,27,36,37,34,39,35,38]
]

estado = 0
nuevoEstado = 0
entrada = 0
salida = 1
tokens = []
datToken = ""

print "Bienvenido a mi traductor".center(80,"=")

while salida !=0:
    
    #Se abre el archivo y se guarda en variable
    entrada = raw_input("Escribe el nombre de archivo: ")
    archivo = open(entrada, "r")
    contenido = archivo.read()
    print contenido

    indice = 0
    while indice < len(contenido):
        print contenido[indice]
        if contenido[indice].isdigit():
            #print "Es numero"
            entrada = 0
        elif 'a' <= contenido[indice] <= 'z':
            print "Es un caracter de la a-z"
            #Validar no sea una palabra reservada if,while,return,else,int,float
            if(contenido[indice] == 'i'):
                #print "Es una i"
                entrada = 1
            elif(contenido[indice] == 'f'):
                #print "Es una f"
                entrada = 2
            elif(contenido[indice] == 'w'):
                #print "Es una w"
                entrada = 3
            elif(contenido[indice] == 'h'):
                #print "Es una h"
                entrada = 4
            elif(contenido[indice] == 'l'):
                #print "Es una l"
                entrada = 5
            elif(contenido[indice] == 'e'):
                #print "Es una e"
                entrada = 6
            elif(contenido[indice] == 'r'):
                #print "Es una r"
                entrada = 7
            elif(contenido[indice] == 't'):
                #print "Es una t"
                entrada = 8
            elif(contenido[indice] == 'u'):
                #print "Es una u"
                entrada = 9
            elif(contenido[indice] == 'n'):
                #print "Es una n"
                entrada = 10
            elif(contenido[indice] == 'l'):
                #print "Es una l"
                entrada = 11
            elif(contenido[indice] == 's'):
                #print "Es una s"
                entrada = 12
            elif(contenido[indice] == 'o'):
                #print "Es una o"
                entrada = 13
            elif(contenido[indice] == 'a'):
                #print "Es una a"
                entrada = 14
            else:
                #print "Cualquier contenido[indice] de a-z"
                entrada = 15
        elif contenido[indice].isspace():
            #print "Es un espacio"
            entrada = 16
        elif 'A' <= contenido[indice] <= 'Z':
            #print "Es una mayuscula"
            entrada = 17
        elif (contenido[indice] == '+' or contenido[indice] == '-'):
            #print "Es un operador de adicion"
            entrada = 18
        elif (contenido[indice] == '*' or contenido[indice] == '/'):
            #print "Es operador de multiplicacion"
            entrada = 19
        elif (contenido[indice] == '<' or contenido[indice] == '>'):
            #print "Es un operador relacional"
            entrada = 20
        elif (contenido[indice] == '='):
            #print "asignacion"
            entrada = 21
        elif (contenido[indice] == '!'):
            #print "Operador relacional opNot"
            entrada = 22
        elif (contenido[indice] == '&'):
            #print "Es un operador and"
            entrada = 23
        elif (contenido[indice] == '|'):
            #print "Es un operador OR"
            entrada = 24
        elif (contenido[indice] == '(' or contenido[indice] == ')'):
            #print "Parentesis"
            entrada = 25
        elif (contenido[indice] == '{' or contenido[indice] == '}'):
            print "Llaves"
            #entrada = 26
        elif (contenido[indice] == ';'):
            print "Punto y coma"
            #entrada = 27
        elif (contenido[indice] == '.'):
            print "Es un punto"
            #entrada = 28
        elif(contenido[indice] == ','):
	    print "Coma"
	    #entrada = 29
	else:
            #print "CARACTER Invalido"
            entrada = 30
            
        #print "Entrada : ", entrada

        datToken = datToken + contenido[indice]
        
        nuevoEstado = estados[estado][entrada]
        #print "Nuevo Estado : ", nuevoEstado
        #print " "

        #       agregar tipo de token y valor

        if (estado == 0) and (entrada == 0):
                              dataToken = ""
        elif (estado == 1) and (0 < entrada < 28 or entrada > 28):
            aux = token(datToken, 9)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 2) and (entrada < 0):
            aux = token(datToken, 7)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 3) and (entrada < 0):
            aux = token(datToken, 3)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 4) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 5)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 5) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 6)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 6) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 5)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 7) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 5)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 8) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 5)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 9) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 5)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 10) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 21)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 11) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 5)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 12) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 5)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 13) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 5)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 14) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 5)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 15) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 5)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 16) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 20)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 17) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 5)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 18) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 5)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 19) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 5)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 20) and (entrada == 16 or entrada > 17):
            aux = token(datToken, 4)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 23):
            aux = token(datToken, 10)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 24):
            aux = token(datToken, 15)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 25) and (20 != entrada != 21):
            aux = token(datToken, 12)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 26):
            aux = token(datToken, 13)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 27):
            aux = token(datToken, 7)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 28):
            aux = token(datToken, 17)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 29):
            aux = token(datToken, 7)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 30):
            aux = token(datToken, 11)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 31) and (entrada != 21):
            aux = token(datToken, 16)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 32):
            aux = token(datToken, 14)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 33) and (entrada != 21):
            aux = token(datToken, 1)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 34):
            aux = token(datToken, 19)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 35):
            aux = token(datToken, 2)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 36):
            aux = token(datToken, 18)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 37):
            aux = token(datToken, 8)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 38):
            aux = token(datToken, 7)
            tokens.append(aux)
            dataToken = ""
        elif (estado == 40):
            aux = token(datToken, 5)
            tokens.append(aux)
            dataToken = ""

        #####Terminana if else para guardar tokens

        estado  = nuevoEstado
        indice += 1


    for i in tokens:
        i.mostrar()


    salida = int(input("Desea salir presione 0: "))
    estado = 0
