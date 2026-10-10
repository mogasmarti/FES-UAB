###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
tecnic = input("Introdueix el nom del tècnic: ")
xarxa = input("Introdueix el nom de la xarxa: ")
print(f"El tècnic {tecnic} està instal·lant la xarxa {xarxa}.")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud = float(input("Longitud del enllaç de fibra en quilòmetres: "))
velocitat = float(input("Velocitat de transmissió: "))
temps = (8 / velocitat) * longitud
print(f"El temps necessari per transmetre 1 GB de dades és de {temps} segons.")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores = float(input("Hores de feina: "))
preuh = float(input("preu per hora: "))
preum = float(input("preu material: "))
cost = (preuh * hores) + preum
print(f"El cost total de la instal·lació es: {cost}")