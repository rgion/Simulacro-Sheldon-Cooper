#traductor

def introducirPalabras(dicc):
    words = input("Introduce la lista de palabras y traducciones en formato \
palabra:traducción separadas por comas: ")
    for i in words.split(','):
        key, value = i.split(':')
        if key in dicc:
            print("la palabra ", key," no ha sido añadida al traductor, ya que existe \
actualmente con la traducción: ", value)
        else:
            dicc[key]=value
            print("La palabra ",key," ha sido añadida al traductor")
        
def traducirTexto(dicc):
    phrase = input('Introduce una frase en español: ')
    for i in phrase.split():
        if i in dicc:
            print(dicc[i], end=' ')
        else:
            print(i, end=' ')

def mostrarMenu(dicc):
    salir= False
    while salir==False:
        print ("=============================")
        print ("TRADUCTOR CASTELLANO-INGLÉS =")
        print ("=============================")
        print (" 1) Introducir palabras      ")
        print (" 2) Traducir texto           ")
        print (" 3) Salir                    ")               
        print ("=============================")           
        opcion=int(input("¿Qué opción deseas? "))
        if opcion==1:
            introducirPalabras(dicc)
        elif opcion==2:
            traducirTexto(dicc)
        elif opcion==3:
            salir=True
        else:
            print ("LA OPCION INTRODUCIDA ES INCORRECTA, VUELVA A INTENTARLO ")

            
# programa principal
dicc = dict()
mostrarMenu(dicc)