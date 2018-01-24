print "Bienvenido a mi traductor".center(70,"=")

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


    pos = int(input("Imprimir pos: "))
    pos2 = int(input("Imprimir pos2: "))
    aux = estados[pos][pos2]
    print aux
    
    salida = int(input("Desea salir presione 0: "))

    

