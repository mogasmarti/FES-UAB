###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom_encaminador = "router oficina"
ubicacio = "escola"
nombre_ports = 4
estat=True
print(f"L'encaminador {nom_encaminador} esta ubicat a {ubicacio}, té {nombre_ports} ports i està encès: {estat}")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
pla_dades= 5
consumits =2
dades_restants= pla_dades - consumits
print(f"Dades restants {dades_restants}")

consumits= 3 
dades_restants = pla_dades - consumits
print(f"Dades restants despres actualitzacio {dades_restants}")