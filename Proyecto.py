print "Bienvenido a mi traductor".center(70,"=")

#Se abre el archivo y se guarda en variable

entrada = raw_input("Escribe el nombre de archivo: ")
archivo = open(entrada, "r")
contenido = archivo.read()

