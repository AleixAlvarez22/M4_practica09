#Llista d'habitacions y les seves àreas.
areas = ['cuina', 7.88, 'menjador', 13.0, 'terrassa', 20.34, 'lavabo', 6.55, 'habitació1', 7.98, 'habitació2', 12, 'rebedor', 4.23]

#Imprimim el segon element de la llista.
print(areas[1])

#Imprimim el ultim element de la llista.
print(areas[-1])

#Imprimim l'àrea de terrassa.
print(areas[5])

#Imprimim del primer element al 3 element.
print(areas[:3])

#Imprimi del 3 element al ultim element.
print(areas[3:])

#Imprimim la suma de dos elements.
print(areas[9]+areas[11])

#Modifiquem l'element que esta a la posició 7.
areas[7] = 13.4
print(areas)

#Afegim al final de la llista una nova habitació i la seva area.
areas.append("pati interior")
areas.append(2.78)
print(areas)