print "Bienvenido a mi traductor".center(80,"=")

estados = [[0,1,2],
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
    print estado

    for caracter in contenido:
        print caracter
        if caracter.isdigit():
            print "Es numero in=0"
        elif 'a' <= caracter <= 'z':
            print "Es un caracter de la a-z"
            #Validar no sea una palabra reservada
            if(caracter == 'i'):
            elif(caracter == 'w'):
            elif(caracter == 'r'):
            elif(caracter == 'e'):
        elif caracter.isspace():
            print "Es un espacio"
        elif 'A' <= caracter <= 'Z':
            print "Es una mayuscula"
        elif (caracter == '+' or caracter == '-'):
            print "Es un operador de adicion"
        elif (caracter == '*' or caracter == '/'):
            print "Es operador de multiplicacion"
        elif (caracter == '<' or caracter == '>'):
            print "Es un operador relacional"
        elif (caracter == '='):
            print "asignacion"
        elif (caracter == '!'):
            print "Operador relacional !"
        elif (caracter == '&'):
            print "Es un operador and"
        elif (caracter == '|'):
            print "Es un operador OR"
        elif (caracter == '(' or caracter == ')'):
            print "Parentesis"
        elif (caracter == '{' or caracter == '}'):
            print "Llaves"
        elif (caracter == ';'):
            print "Punto y coma"
        elif (caracter == '.'):
            print "Es un punto"
        elif(caracter == ','):
	    print "Coma"
        else:
            print "Caracter Invalido"
                                        
                        
            
    
    salida = int(input("Desea salir presione 0: "))
