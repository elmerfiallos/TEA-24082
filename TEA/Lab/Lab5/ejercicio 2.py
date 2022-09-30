try:
    entrada =input ("Ingrese el nombre del archivo")
    archivo = open (entrada , "r", encoding ="UTF-8")
    for linea in archivo:
        print (linea.superior)
except:
    print("Error. arhivo no existe")
#print (archivo.read())

