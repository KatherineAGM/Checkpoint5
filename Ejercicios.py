#Ejercicio 1

cereales = ["avena", "maiz", "cebada"]
for cereal in cereales:
  print(cereal)

# Ejercicio 2
def suma(x, y, z):
    return x+y+z

respuesta = suma (5,5,3) # 13
print (respuesta)

# Ejercicio 3
suma = lambda x, y, z: x + y + z

respuesta = suma(5, 5, 3)
print(respuesta)

# Ejercicio 4
nombre = 'Enrique'
lista_nombre = ('Jessica', 'Paul', 'George', 'Henry', 'Adán')

if nombre in lista_nombre:
  print(f"Esta persona '{nombre}' coincide con un valor de la lista.")
else:
  print(f"Esta persona '{nombre}' no coincide con ningún valor de la lista.")