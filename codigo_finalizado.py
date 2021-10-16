#Desafio 1, Unidad 1 
#Alumnos: Davida Mansilla y Elvis Guerrero
#Profesores: Gabriel Ñunez y Luz Cardona


from random import randint 

# Cambiamos el código por el uso de temp que permite agilizar más el código #
# evitando el primer paso de las variables con el randint #

############-----------------------------------------------------------------------------------------------------------------
temp = randint(1,4)
if temp ==1 :
    A1="P"
if temp ==2 or temp ==3:
    A1="B"
if temp ==4:
    A1="A"
############-----------------------------------------------------------------------------------------------------------------
temp = randint(1,4)
if temp ==1 :
    A2="P"
if temp ==2 or temp ==3:
    A2="B"
if temp ==4:
    A2="A"
############-----------------------------------------------------------------------------------------------------------------
temp = randint(1,4)
if temp ==1 :
    A3="P"
if temp ==2 or temp ==3:
    A3="B"
if temp ==4:
    A3="A"
############-----------------------------------------------------------------------------------------------------------------
temp = randint(1,4)
if temp ==1 :
    A4="P"
if temp ==2 or temp ==3:
    A4="B"
if temp ==4:
    A4="A"
############-----------------------------------------------------------------------------------------------------------------
temp = randint(1,4)
if temp ==1 :
    B1="P"
if temp ==2 or temp ==3:
    B1="B"
if temp ==4:
    B1="A"
############-----------------------------------------------------------------------------------------------------------------
temp = randint(1,4)
if temp ==1 :
    B2="P"
if temp ==2 or temp ==3:
    B2="B"
if temp ==4:
    B2="A"
############-----------------------------------------------------------------------------------------------------------------
temp = randint(1,4)
if temp==1 :
    B3="P"
if temp ==2 or temp ==3:
    B3="B"
if temp==4:
    B3="A"
############-----------------------------------------------------------------------------------------------------------------
temp = randint(1,4)
if temp ==1 :
    B4="P"
if temp ==2 or temp ==3:
    B4="B"
if temp ==4:
    B4="A"
############-----------------------------------------------------------------------------------------------------------------
temp = randint(1,4)
if temp ==1 :
    C1="P"
if temp ==2 or temp==3:
    C1="B"
if temp ==4:
    C1="A"
############-----------------------------------------------------------------------------------------------------------------
temp = randint(1,4)
if temp ==1 :
    C2="P"
if temp or temp ==3:
    C2="B"
if temp ==4:
    C2="A"
############-----------------------------------------------------------------------------------------------------------------
temp = randint(1,4)
if temp ==1 :
    C3="P"
if temp ==2 or temp ==3:
    C3="B"
if temp ==4:
    C3="A"
############-----------------------------------------------------------------------------------------------------------------
temp = randint(1,4)
if temp ==1 :
    C4="P"
if temp ==2 or temp ==3:
    C4="B"
if temp ==4:
    C4="A"
############-----------------------------------------------------------------------------------------------------------------
temp = randint(1,4)
if temp ==1 :
    D1="P"
if temp ==2 or temp ==3:
    D1="B"
if temp ==4:
    D1="A"
############-----------------------------------------------------------------------------------------------------------------
temp = randint(1,4)
if temp ==1 :
    D2="P"
if temp ==2 or temp ==3:
    D2="B"
if temp ==4:
    D2="A"
############-----------------------------------------------------------------------------------------------------------------
temp = randint(1,4)
if temp ==1 :
    D3="P"
if temp ==2 or temp ==3:
    D3="B"
if temp ==4:
    D3="A"
############-----------------------------------------------------------------------------------------------------------------
temp == randint(1,4)
if temp ==1 :
    D4="P"
if temp ==2 or temp ==3:
    D4="B"
if temp==4:
    D4="A"

#### Variable elementos ####

# Con esta variable contamos la cantidad de plantas y bacterias #
# cada vez que ejecutamos el programa #

ConteoB = 0
ConteoP = 0
ConteoA = 0 

#### Variables para conteo ####

# En esta parte hace que cada vez que se ejecute el programa dependiendo# 
# si se cumple el "if" agrega el número al contador #

if A1 == "P":
    ConteoP = ConteoP + 1
elif A1 == "B": 
    ConteoB = ConteoB + 1
elif A1 == "A": 
    ConteoA = ConteoA + 1
if A2 == "P": 
    ConteoP = ConteoP + 1
elif A2 == "B":
    ConteoB = ConteoB + 1
elif A2 == "A":
    ConteoA = ConteoA + 1
if A3 == "P":
    ConteoP = ConteoP + 1
elif A3 == "B": 
    ConteoB = ConteoB + 1
elif A3 == "A": 
    ConteoA = ConteoA + 1
if A4 == "P":
    ConteoP = ConteoP + 1
elif A4 == "B": 
    ConteoB = ConteoB + 1
elif A4 == "A": 
    ConteoA = ConteoA + 1
if B1 == "P":
    ConteoP = ConteoP + 1
elif B1 == "B": 
    ConteoB = ConteoB + 1
elif B1 == "A": 
    ConteoA = ConteoA + 1
if B2 == "P": 
    ConteoP = ConteoP + 1
elif B2 == "B":
    ConteoB = ConteoB + 1
elif B2 == "A":
    ConteoA = ConteoA + 1
if B3 == "P":
    ConteoP = ConteoP + 1
elif B3 == "B": 
    ConteoB = ConteoB + 1
elif B3 == "A": 
    ConteoA = ConteoA + 1
if B4 == "P":
    ConteoP = ConteoP + 1
elif B4 == "B": 
    ConteoB = ConteoB + 1
elif B4 == "A": 
    ConteoA = ConteoA + 1
if C1 == "P":
    ConteoP = ConteoP + 1
elif C1 == "B": 
    ConteoB = ConteoB + 1
elif C1 == "A": 
    ConteoA = ConteoA + 1
if C2 == "P": 
    ConteoP = ConteoP + 1
elif C2 == "B":
    ConteoB = ConteoB + 1
elif C2 == "A":
    ConteoA = ConteoA + 1
if C3 == "P":
    ConteoP = ConteoP + 1
elif C3 == "B": 
    ConteoB = ConteoB + 1
elif C3 == "A": 
    ConteoA = ConteoA + 1
if C4 == "P":
    ConteoP = ConteoP + 1
elif C4 == "B": 
    ConteoB = ConteoB + 1
elif C4 == "A": 
    ConteoA = ConteoA + 1
if D1 == "P":
    ConteoP = ConteoP + 1
elif D1 == "B": 
    ConteoB = ConteoB + 1
elif D1 == "A": 
    ConteoA = ConteoA + 1
if D2 == "P": 
    ConteoP = ConteoP + 1
elif D2 == "B":
    ConteoB = ConteoB + 1
elif D2 == "A":
    ConteoA = ConteoA + 1
if D3 == "P":
    ConteoP = ConteoP + 1
elif D3 == "B": 
    ConteoB = ConteoB + 1
elif D3 == "A": 
    ConteoA = ConteoA + 1
if D4 == "P":
    ConteoP = ConteoP + 1
elif D4 == "B": 
    ConteoB = ConteoB + 1
elif D4 == "A": 
    ConteoA = ConteoA + 1

#### Porcentaje de ocurriencias ####

# Aquí usando el contador se divide por el total de los Sub-cuadrantes y al multiplicarlo *100 sacamos el % de cada uno #

PorcP = (ConteoP/16) *100
PorcB = (ConteoB/16) *100
PorcA = (ConteoA/16) *100

#----------------------------------------------------------------------------------------------------------------------#

# Aquí se imprime los 16 Sub-cuadrantes #

print("------------------")
print("|",A1, "|",B1, "|",C1, "|",D1, "|")
print("|",A2, "|",B2, "|",C2, "|",D2, "|")
print("|",A3, "|",B3, "|",C3, "|",D3, "|")
print("|",A4, "|",B4, "|",C4, "|",D4, "|")
print("------------------")
    
#----------------------------------------------------------------------------------------------------------------------#

# Aquí imprime el porcentaje que se obtuvo de los Sub-cuadrantes #

print("El porcentaje de ocurrencia de las plantas es: %", PorcP)
print("El porcentaje de ocurrencia de las bacterias es: %",PorcB)
print("El porcentaje de ocurrencia del agua es: %",PorcA)

##### En caso de misma ocurrencia u mayor ocurrencia#####
#----------------------------------------------------------------------------------------------------------------------#

# Con estas líneas de código se imprime en caso de que los porcentajes de ocurrencia sean el mismo #
# O en el caso de que alguno tenga mayor porcentaje de ocurrencia #

if PorcP == PorcB :
    print("El porcentaje de ocurrencias de las plantas y las bacterias es la misma ")
if PorcP == PorcA :
    print("El porcentaje de ocurrencias de las plantas y el agua es la misma ") 
if PorcB == PorcA :
    print("El porcentaje de ocurrencias de las bacterias y el agua es la misma ")
if PorcP > PorcB and PorcP > PorcA : 
    print("La planta tiene mayor ocurrencia con un porcentaje del %", PorcP)
if PorcB > PorcP and PorcB > PorcA : 
    print("Las bacterias tiene mayor ocurrencia con un porcentaje del %", PorcB)
if PorcA > PorcB and PorcA > PorcP : 
    print("El agua tiene mayor ocurrencia con un porcentaje del %", PorcA)
if PorcP < PorcB and PorcP < PorcA : 
    print("La planta tiene menor ocurrencia con un porcentaje del %", PorcP)
if PorcB < PorcP and PorcB < PorcA : 
    print("La bacteria tiene menor ocurrencia con un porcentaje del %", PorcB)
if PorcA < PorcB and PorcA < PorcP : 
    print("El agua tiene menor ocurrencia con un porcentaje del %", PorcA)
    
#### Existencia de ataque ####
#----------------------------------------------------------------------------------------------------------------------#

# Con esto se analiza que en el caso dado que una planta este rodeada por 8 bacterias se considera ataque #

if B2 == "P" :
    if A1 =="B" and A2 =="B" and A3 =="B" and B3 =="B" and C3 =="B" and C2 =="B" and C1 =="B" and B1 =="B":
        print("Planta bajo ataque!!!")
elif C2 == "P" :
    if B1 =="B" and B2 =="B" and B3 =="B" and C3 =="B" and D3 =="B" and D2 =="B" and D1 =="B" and C1 =="B":
        print("Planta bajo ataque!!!")
elif B3 == "P" :
    if A3 =="B" and A4 =="B" and B4 =="B" and C4 == "B" and C3 =="B" and C2 =="B" and B2 =="B" and A2 =="B":
        print("Planta bajo ataque!!!")
elif C3 == "P" : 
    if B3 =="B" and B4 =="B" and C4 =="B" and D4 =="B" and D3 =="B" and D2 =="B" and C2 =="B" and B2 =="B":
        print("Planta bajo ataque!!!")
        
#### Existencia de falta de agua ####
#----------------------------------------------------------------------------------------------------------------------#

# En este se indica que en caso de que en una casilla de Agua este rodeada por 8 plantas exista una escasez de agua #

if B2 == "A" :
    if A1 =="P" and A2 =="P" and A3 =="P" and B3 =="P" and C3 =="P" and C2 =="P" and C1 =="P" and B1 =="P":
        print("Agua con riesgo escasez")
elif C2 == "A" :
    if B1 =="P" and B2 =="P" and B3 =="P" and C3 =="P" and D3 =="P" and D2 =="P" and D1 =="P" and C1 =="P":
        print("Agua con riesgo escasez")
elif B3 == "A" :
    if A3 =="P" and A4 =="P" and B4 =="P" and C4 == "P" and C3 =="P" and C2 =="P" and B2 =="P" and A2 =="P":
        print("Agua con riesgo escasez")
elif C3 == "A" : 
    if B3 =="P" and B4 =="P" and C4 =="P" and D4 =="P" and D3 =="P" and D2 =="P" and C2 =="P" and B2 =="P":
        print("Agua con riesgo escasez")
