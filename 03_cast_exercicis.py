###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
paquets_rebuts= int(input("Introdueix nombre paquets rebuts:"))
total_paquets= paquets_rebuts + 1200
print(f"paquets totals {total_paquets}")
# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
velocitat_conexio=float(input("Introdueix velocitat en Mbps: "))
print(f"Velocitat en MB/s: {velocitat_conexio/8}")