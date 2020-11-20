""" PROGRAMA CÁLCULO DE CONJETURA DE SHELDON"""
"""El 73 es el 21º número primo, y leído al revés es el 37,
que es el 12º número primo, que al revés es el 21,
que es el resultado de multiplicar, agarraos fuerte, 7 por 3."""

# Dividimos el proceso en varios pasos, es cierto que en el primer paso se
# realizan varias acciones
#paso 1: N es primo? si no es así, ya no hay nada más que calcular
#paso 2: ¿que número de primo es N? Le llamaremos numPrim
#paso 3: el espejo de N es primo? Le llamaremos espejo
#paso 4: que número de primo es el espejo? Le llamaremos numPrimEsp
#paso 5: coincide que numPrimEsp es igual que el espejo de Numprim?
#paso 6: numPrim es igual a multiplicar las cifras de N? P.ej es 21 ==
#a multiplicar 7*3

def esPrimo(num):
    i=2
    es_primo=True
    while (i<((num/2)+1) and es_primo==True):
        if num%i==0:
            es_primo=False
        i+=1
    return es_primo

def obtenerEspejo(num):#obtenemos dado un número
    aux=str(num)
    aux=aux[::-1]#recorremos al revés
    return int(aux)

def añadirPrimos(lista_primos,num):
#calculamos todos los primos existentes    
    for i in range (2,num+1):
        if esPrimo(i):
            lista_primos.append(i)
    print(lista_primos)
            
def obtenerNumMult(num):
    numcad=str(num)
    res=1
    for i in numcad:
        res=res*int(i)
    return res

# programa principal
lista_primos=[]
numsheldon=False
print ("===========================================")
print ("    PROGRAMA CÁLCULO CONJETURA SHELDON     ")
print ("===========================================")
num=int(input("Dame el número para el que quieres comprobar \
si cumple el teorema de Sheldon: "))

#paso 1: N es primo? si no es así, ya no hay nada más que calcular
if esPrimo(num):
    print("el número %d es primo. PASO 1 OK"%(num))
# si efectivamente es primos añadimos los primos hasta ese número
#calculamos todos los primos existentes
    añadirPrimos(lista_primos,num)
    
#paso 2: ¿que número de primo es N? Le llamaremos numPrim
    numPrim=lista_primos.index(num)+1 #como las listas empiezan a contar
    # en cero, añadimos 1
    print("PASO 2 OK.es el número de primo %d "%(numPrim))
    
#paso 3: el espejo de N es primo? Le llamaremos espejo
    espejo=obtenerEspejo(num)
    
    if espejo in lista_primos:
        numprimo_espejo=lista_primos.index(espejo)+1
        print("PASO 3 OK. El espejo %d es primo y el número de primo es %d. PASO 2. OK"%
              (espejo, numprimo_espejo))

#paso 4: que número de primo es el espejo? Le llamaremos numPrimEsp
        numPrimEsp=obtenerEspejo(numprimo_espejo)
        print ("PASO 4: que número de primo es el espejo? numPrimEsp= ",numPrimEsp)

#paso 5: coincide que numPrimEsp es igual que el espejo de Numprim?
        if numPrimEsp==numPrim:
            print("PASO 5: coincide que", numPrimEsp,"==", numPrim)

#paso 6: numPrim es igual a multiplicar las cifras de N? P.ej es 21 ==
#a multiplicar 7*3
            print ("cuanto es si multiplico las cifras del número ",num)
            resmult=obtenerNumMult(num)
            print ("Es ",resmult,"==",numPrimEsp,"?")
            if resmult==numPrimEsp:
                print("PASO 6 OK")
                numsheldon=True
                
if numsheldon:
    print("El número %d es un número Sheldon"%(num))
else:
    print("El número %d NO es un número Sheldon"%(num))
print ("===========================================")    

