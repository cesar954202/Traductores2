print "Bienvenido a mi traductor".center(80,"=")

test = [[0,1,2],
           [10,11,13],
           [20,21,22]
           ]

estado = 0
entrada = 0

salida = 1
while salida !=0:
    
    #Se abre el archivo y se guarda en variable
    entrada = raw_input("Escribe el nombre de archivo: ")
    archivo = open(entrada, "r")
    contenido = archivo.read()
    print contenido

    #Pruebas de impresion de posision
#    pos = int(input("Imprimir pos: "))
#    pos2 = int(input("Imprimir pos2: "))
    
#    aux = estados[pos][pos2]
#    print estado

    #for contenido[indice] in contenido:
    indice = 0
    while indice < len(contenido):
        print contenido[indice]
        if contenido[indice].isdigit():
            print "Es numero"
            entrada = 0
        elif 'a' <= contenido[indice] <= 'z':
            print "Es un caracter de la a-z"
            #Validar no sea una palabra reservada if,while,return,else,int,float
            if(contenido[indice] == 'i'):
                print "Es una i"
                entrada = 1
            elif(contenido[indice] == 'f'):
                print "Es una f"
                entrada = 2
            elif(contenido[indice] == 'w'):
                print "Es una w"
                entrada = 3
            elif(contenido[indice] == 'h'):
                print "Es una h"
                entrada = 4
            elif(contenido[indice] == 'l'):
                print "Es una l"
                entrada = 5
            elif(contenido[indice] == 'e'):
                print "Es una e"
                entrada = 6
            elif(contenido[indice] == 'r'):
                print "Es una r"
                entrada = 7
            elif(contenido[indice] == 't'):
                print "Es una t"
                entrada = 8
            elif(contenido[indice] == 'u'):
                print "Es una u"
                entrada = 9
            elif(contenido[indice] == 'n'):
                print "Es una n"
                entrada = 10
            elif(contenido[indice] == 'l'):
                print "Es una l"
                entrada = 11
            elif(contenido[indice] == 's'):
                print "Es una s"
                entrada = 12
            elif(contenido[indice] == 'o'):
                print "Es una o"
                entrada = 13
            elif(contenido[indice] == 'a'):
                print "Es una a"
                entrada = 14
            else:
                print "Cualquier contenido[indice] de a-z"
                entrada = 15
        elif contenido[indice].isspace():
            print "Es un espacio"
            entrada = 16
        elif 'A' <= contenido[indice] <= 'Z':
            print "Es una mayuscula"
            entrada = 17
        elif (contenido[indice] == '+' or contenido[indice] == '-'):
            print "Es un operador de adicion"
            entrada = 18
        elif (contenido[indice] == '*' or contenido[indice] == '/'):
            print "Es operador de multiplicacion"
            entrada = 19
        elif (contenido[indice] == '<' or contenido[indice] == '>'):
            print "Es un operador relacional"
            entrada = 20
        elif (contenido[indice] == '='):
            print "asignacion"
            entrada = 21
        elif (contenido[indice] == '!'):
            print "Operador relacional opNot"
            entrada = 22
        elif (contenido[indice] == '&'):
            print "Es un operador and"
            entrada = 23
        elif (contenido[indice] == '|'):
            print "Es un operador OR"
            entrada = 24
        elif (contenido[indice] == '(' or contenido[indice] == ')'):
            print "Parentesis"
            entrada = 25
        elif (contenido[indice] == '{' or contenido[indice] == '}'):
            print "Llaves"
            entrada = 26
        elif (contenido[indice] == ';'):
            print "Punto y coma"
            entrada = 27
        elif (contenido[indice] == '.'):
            print "Es un punto"
            entrada = 28
        elif(contenido[indice] == ','):
	    print "Coma"
	    entrada = 29
	else:
            print "contenido[indice] Invalido"
            entrada = 30
            
        print "Entrada : ", entrada
        print " "
        indice += 1
        print "Indice es " , indice , "largo" , len(contenido)
    salida = int(input("Desea salir presione 0: "))
