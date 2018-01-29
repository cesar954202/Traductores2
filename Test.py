print "Bienvenido a mi traductor".center(80,"=")

estados = [[00,01,02],
           [10,11,13],
           [20,21,22]
           ]

salida = 1
while salida !=0:
    
    #Se abre el archivo y se guarda en variable
    entrada = raw_input("Escribe el nombre de archivo: ")
    archivo = open(entrada, "r")
    contenido = archivo.read()
    print contenido

    #Pruebas de impresion de posision
    #pos = int(input("Imprimir pos: "))
    #pos2 = int(input("Imprimir pos2: "))
    
    #aux = estados[pos][pos2]
    #print aux

    for caracter in contenido:
        print caracter
        if caracter.isdigit():
            print "Es numero"
        else:
            if 'a' <= caracter <= 'z':
                print "Es un caracter de la a-z"
                #Validar no sea una palabra reservada                
            else:
                if caracter.isspace():
                    print "Es un espacio"
                else:
                    if 'A' <= caracter <= 'Z':
                        print "Es una mayuscula"
                    else:
                        if (caracter == '+' or caracter == '-'):
                            print "Es un operador de adicion"
                        else:
                            if (caracter == '*' or caracter == '/'):
                                print "Es operador de multiplicacion"
                            else:
                                if (caracter == '<' or caracter == '>'):
                                    print "Es un operador relacional"
                                else:
                                    if (caracter == '='):
                                        print "asignacion"
                                    else:
                                        if (caracter == '!'):
                                            print "Operador relacional !"
                                        else:
                                            if (caracter == '&'):
                                                print "Es un operador and"
                                            else:
                                                if (caracter == '|'):
                                                    print "Es un operador OR"
                                                else:
                                                    if (caracter == '(' or caracter == ')'):
                                                        print "Parentesis"
                                                    else:
                                                        if (caracter == '{' or caracter == '}'):
                                                            print "Llaves"
                                                        else:
                                                            if (caracter == ';'):
                                                                print "Punto y coma"
                                                            else:
                                                                if (caracter == '.'):
                                                                    print "Es un punto"
                                                                else:
                                                                    print "Caracter Invalido"
                                        
                        
            
    
    salida = int(input("Desea salir presione 0: "))

    

