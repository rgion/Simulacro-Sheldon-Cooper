""" PROGRAMA CÁLCULO DE CONJETURA DE SHELDON"""
""" Dado un número calcula hasta ese número si existe algún número sheldon"""
"""El 73 es el 21º número primo, y leído al revés es el 37,
que es el 12º número primo, que al revés es el 21,
que es el resultado de multiplicar, agarraos fuerte, 7 por 3."""
# Dividimos el proceso en varios pasos, es cierto que en el paso se
# realizan varias acciones
#paso 1: 73 es primo?
#paso 2: el espejo 37 es primo?
#paso 3: que número de primo es el espejo? 12 y su espejo cual es? 21
#paso 4: ese 21 == a multiplicar 7*3

def es_primo(num):
    i=2
    es_primo=True
    while (i<(num/2)+1 and es_primo==True):
        if num%i==0:
            es_primo=False
        i+=1
    return es_primo

def obtenerEspejo(num):#obtenemos
    aux=str(num)
    print(aux)
    aux=aux[::-1]#recorremos al revés
    print(aux)
    return int(aux)

def añadirPrimos(lista_primos,num):
#calculamos todos los primos existentes    
    for i in range (2,num+1):
        if es_primo(i):
            lista_primos.append(i)
    print(lista_primos)
            
def obtenerNumMult(num):
    #pasamos el número a cadena
    numcad=str(num)
    res=1
    for i in numcad:
        res=res*int(i)
    return res
def calcularConjeturaSheldon(num,lista_primos):
    numsheldon=False    
    # 1 - el número que vamos a calcular es primo? si no no hay nada que mirar
    if num in lista_primos:
    #    print("el número %d es primo. PASO 1 OK"%(num))
            
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
        print("ALARM: El número %d es un número Sheldon"%(num))
    else:
        print("El número %d NO es un número Sheldon"%(num))
    print ("===========================================")    

# programa principal
lista_primos=[]

print ("===========================================")
print ("    PROGRAMA CÁLCULO CONJETURA SHELDON     ")
print ("===========================================")
num=int(input("Dame el número hasta el que quieres que calculemos \
si cumple la conjetura de Sheldon "))
# 1.1-si efectivamente es primos añadimos los primos hasta ese número
#calculamos todos los primos existentes
añadirPrimos(lista_primos,num)
for i in range(2,num+1):
    calcularConjeturaSheldon(i,lista_primos)