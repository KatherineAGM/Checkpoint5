# **Guía de información clave para iniciante en python**

# ¿Qué es un Condicional en Programación?

Un **condicional** es una estructura de control fundamental en programación que permite a un programa tomar decisiones y ejecutar diferentes bloques de código basándose en si una determinada **condición** es verdadera o falsa. Es como una bifurcación en el camino del programa.

## Analogía de la Vida Real

> **Si** está lloviendo, **entonces** lleva un paraguas. **Sino**, no lo lleves.

## Estructuras Condicionales Comunes

Las más comunes son:

* **`if` (si):** El bloque de código asociado se ejecuta **solo si** la condición especificada es verdadera (`true`).

* **`else if` (sino si) / `elif` (en algunos lenguajes):** Permite verificar múltiples condiciones en secuencia. Si la condición del `if` es falsa, se evalúa la condición del primer `else if`. Si es verdadera, se ejecuta su bloque y se omite el resto. Se pueden tener múltiples `else if`.

* **`else` (sino):** El bloque de código asociado se ejecuta **solo si** todas las condiciones anteriores (`if` y cualquier `else if`) fueron falsas.

## Componentes Clave de un Condicional

1.  **Condición:**
    * Es una expresión que se evalúa a `verdadero` (`true`) o `falso` (`false`).
    * A menudo involucra:
        * **Operadores de comparación:** `==` (igual a), `!=` (no igual a), `>` (mayor que), `<` (menor que), `>=` (mayor o igual que), `<=` (menor o igual que).
        * **Operadores lógicos:** `and` (o `&&`), `or` (o `||`), `not` (o `!`).

2.  **Bloque de Código `if`:**
    * Se ejecuta si la **condición** del `if` es `verdadera`.

3.  **Bloque de Código `else if` (opcional):**
    * Se evalúa si la condición del `if` es `falsa`.
    * Si su propia **condición** es `verdadera`, se ejecuta su bloque.

4.  **Bloque de Código `else` (opcional):**
    * Se ejecuta si todas las **condiciones** anteriores (`if` y cualquier `else if`) son `falsas`.

## Ejemplo en Python (Bloque de Código)

```python
temperatura = 26

if temperatura > 30:
  print("¡Que calor hace!")
elif temperatura > 20:
  print("Que buena temperatura.")
else:
  print("Hace fresco.")
  ```
  # Tipos de Bucles en Python

Python ofrece principalmente dos tipos de bucles para la ejecución repetida de bloques de código: el bucle `for` y el bucle `while`.

## 1. Bucle `for`

El bucle `for` se utiliza para iterar sobre una **secuencia** (como listas, tuplas, cadenas, rangos, etc.). Ejecuta el bloque de código una vez por cada elemento de la secuencia.

**Sintaxis:**

```python
for elemento in secuencia:
    # Código a ejecutar para cada elemento
Ejemplos:

Sobre una lista:

frutas = ["manzana", "plátano", "cereza"]
for fruta in frutas:
    print(fruta)

Resultado:

manzana
plátano
cereza

Sobre un  rango de números:

for numero in range(5):  # Genera números del 0 al 4
    print(numero)

Resultado:

0
1
2
3
4

Sobre una cadena de texto:

mensaje = "Hola"
for letra in mensaje:
    print(letra)

Resultado:

H
o
l
a
```

## 2. Bucle `while`
El bucle  `while` un bloque de código **mientras una condición especificada sea verdadera**. Es crucial asegurarse de que la condición eventualmente se vuelva falsa para evitar bucles infinitos.

**Sintaxis:**
```python
while condicion:
    # Código a ejecutar mientras la condición sea verdadera
    # (Asegúrate de modificar la condición dentro del bucle)
```

**Ejemplos:**
```python

contador=0 
while contador <5:
    print(contador)
    contador += 1

Resultado:

0
1
2
3
4
Bucle hasta que el usuario ingresa "salir":
```


## Control de flujo en bucles

Python proporciona palabras clave para controlar el flujo dentro de los bucles:

`break`:Sale inmediatamente del bucle.

`continue`: Salta la iteración actual y pasa a la siguiente.

`else` en Bucles: Se ejecuta después de que el bucle for termina de iterar completamente o cuando la condición del bucle while se vuelve falsa (si el bucle no fue interrumpido por break).

**Ejemplo con else en un bucle for:**

```python

numeros = [1, 3, 5, 7, 9]
for numero in numeros:
    if numero % 2 == 0:
        print("Se encontró un número par:", numero)
        break
else:
    print("No se encontraron números pares en la lista.")
Resultado (en este caso):

No se encontraron números pares en la lista.
```
En resumen, los bucles `for` y `while` son herramientas esenciales para la repetición de código en Python, y las palabras clave **break**, **continue**, y la cláusula **else** ofrecen un control más preciso sobre su ejecución.

los **bucles** son una herramienta poderosa y fundamental en Python (y en la programación en general) porque permiten automatizar tareas repetitivas, procesar grandes cantidades de datos de manera eficiente y escribir código más conciso y legible. Sin ellos, muchas de las tareas que realizamos con la programación serían prácticamente imposibles o extremadamente ineficientes, es por esta razón que son muy utiles.

# Listas por Comprensión en Python

Una **lista por comprensión** (en inglés, *list comprehension*) en Python es una forma concisa y elegante de crear listas nuevas basadas en listas existentes u otros objetos iterables. Ofrece una sintaxis más corta y a menudo más legible para realizar operaciones comunes de creación de listas que involucran bucles `for` y, opcionalmente, condicionales `if`.

Piensa en ella como una forma de definir una lista utilizando una única línea de código que describe cómo generar sus elementos.

## Sintaxis Básica

```python
[expresión for elemento in iterable if condición]
```
**Donde**:

`expresión:` Es la operación o el valor que se aplicará a cada `elemento` del `iterable` para crear el nuevo elemento de la lista resultante.

`for elemento in iterable:` Itera sobre cada `elemento` en el `iterable` (por ejemplo, una lista, un rango, una cadena).

`if condición` (opcional): Es un filtro. Si se incluye, la `expresión` solo se evaluará y el resultado se agregará a la nueva lista si la `condición` es verdadera para el `elemento` actual.

**Ejemplos**
1. Crear una lista con los cuadrados de los números del 0 al 4:

Usando un bucle for tradicional:

```Python

cuadrados = []
for numero in range(5):
    cuadrados.append(numero**2)
print(cuadrados)  # Output: [0, 1, 4, 9, 16]
Usando una lista por comprensión:
```

```Python

cuadrados = [numero**2 for numero in range(5)]
print(cuadrados)  # Output: [0, 1, 4, 9, 16]
```
2. Crear una lista con los números pares del 0 al 9:

Usando un bucle for con un if:


```Python

pares = []
for numero in range(10):
    if numero % 2 == 0:
        pares.append(numero)
print(pares)  # Output: [0, 2, 4, 6, 8]
```
**¿Por qué son útiles?**

*Concisión*: Reducen la cantidad de código necesario.

*Legibilidad*:  menudo son más fáciles de entender que los bucles for tradicionales para operaciones simples.

*Rendimiento (en algunos casos)*: Pueden ser ligeramente más eficientes que los bucles for equivalentes.

# ¿Qué es un argumento en Python?
Un **argumento** en Python es un valor que se pasa a una función o a un método cuando se le llama. Imagina una máquina (la función) que realiza una tarea específica. Para que funcione y produzca un resultado útil, a menudo necesita "materias primas" o "instrucciones", que son los argumentos.

En esencia, los argumentos hacen que las funciones y los métodos sean más **flexibles** y **reutilizables**, ya que pueden operar con diferentes datos en cada llamada.

**Cosas importantes a saber:**

Se definen en la llamada: Los valores dentro de los paréntesis al invocar una función son los argumentos.

Se reciben como parámetros: En la definición de la función, variables especiales llamadas parámetros reciben los valores de los argumentos.

Pueden ser de diferentes tipos: Números, cadenas, listas, diccionarios, objetos, ¡cualquier tipo de dato válido en Python!

Pueden ser posicionales o de palabra clave:

* Argumentos posicionales: Se pasan en el mismo orden que los parámetros en la definición. El primer argumento se asigna al primer parámetro, y así sucesivamente.

* Argumentos de palabra clave: Se pasan especificando el nombre del parámetro (nombre_parametro=valor). Esto permite pasarlos en cualquier orden y mejora la legibilidad.

Las funciones pueden tener cero, uno o múltiples argumentos.

**Ejemplos:**

```Python

# Definición de una función con un argumento (nombre)
def saludar(nombre):
  print(f"¡Hola, {nombre}!")

# Llamada con un argumento posicional
saludar("Ana")  # Salida: ¡Hola, Ana!

# Definición de una función con dos argumentos (base y exponente)
def potencia(base, exponente):
  resultado = base ** exponente
  return resultado

# Llamada con argumentos posicionales
resultado1 = potencia(2, 3)  # base = 2, exponente = 3
print(resultado1)  # Salida: 8

# Llamada con argumentos de palabra clave
resultado2 = potencia(exponente=4, base=5)  # El orden no importa
print(resultado2)  # Salida: 625

# Definición de una función sin argumentos
def mostrar_mensaje():
  print("Este es un mensaje.")

# Llamada sin argumentos
mostrar_mensaje()  # Salida: Este es un mensaje.
```
# ¿Qué es una función Lambda en Python?

Una función lambda en Python es una función anónima, pequeña y de una sola expresión. Se definen utilizando la palabra `clave` lambda en lugar de `def`.

### Características principales:

* Anónimas: No tienen un nombre definido.
* Pequeñas: Diseñadas para tareas concisas.
* De una sola expresión: Su cuerpo se limita a una única expresión cuyo resultado se devuelve implícitamente. No pueden contener múltiples expresiones ni sentencias complejas.
  
**Sintaxis**:

```Python

lambda argumentos: expresión
```

* `lambda`: Palabra clave para definir la función lambda.
* `argumentos`: Lista de cero o más argumentos (separados por comas).
* `:`: Separador entre argumentos y la expresión.
* `expresión`: Única expresión a evaluar y retornar.

### ¿Cuándo usar funciones Lambda?

Útiles para funciones simples y de uso corto, a menudo como argumento de otras funciones de orden superior:

* Con `map()`, `filter()` y `reduce()`: Para definir la función que se aplica a los elementos de una secuencia.
* Como clave para `sorted()`: Para especificar criterios de ordenamiento personalizados.
* En GUI: Para definir pequeñas funciones de callback para eventos.
  
**Ejemplos:**

```Python

# Suma de dos números
suma = lambda a, b: a + b
print(suma(5, 3))  # Salida: 8

# Elevar al cuadrado con map()
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]

# Filtrar números pares con filter()
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4]

# Ordenar tuplas por el segundo elemento con sorted()
data = [(1, 'z'), (2, 'a'), (3, 'b')]
ordenado = sorted(data, key=lambda item: item[1])
print(ordenado)  # Salida: [(2, 'a'), (3, 'b'), (1, 'z')]
``` 
**Limitaciones:**

* Solo una expresión.
* No pueden contener sentencias complejas.
* Pueden ser menos legibles si la expresión es compleja. En tales casos, usar `def` es preferible.

# ¿Qué es un paquete pip?

Un **paquete pip es una distribución de código Python** que se puede instalar fácilmente utilizando el gestor de paquetes **pip** (Pip Installs Packages o Python Package Index). Son como módulos de software preconstruidos que contienen todo lo necesario para realizar tareas específicas, permitiendo añadir nuevas funcionalidades a tu proyecto sin escribir código desde cero.

**Puntos clave:**

+ **Distribuciones de código:** Conjunto organizado de archivos para su instalación y gestión por pip.
+ **Reutilización de código:**  Permiten usar código de otros desarrolladores, ahorrando tiempo.
+ **Funcionalidad extendida:** Añaden nuevas capacidades a tu entorno Python.
+ **Gestionados por pip:**  La herramienta de línea de comandos `pip` gestiona los paquetes.
+ **Python Package Index (PyPI):** El repositorio oficial y más grande de paquetes Python.
+ **Dependencias:** `pip` gestiona automáticamente la instalación de otros paquetes de los que dependa el que quieres instalar.

### ¿Cómo se usan los paquetes pip?

Se interactúa con `pip` a través de la línea de comandos. Comandos comunes:

- `pip install nombre_del_paquete:` Descarga e instala un paquete desde PyPI.
- `pip uninstall nombre_del_paquete:` Desinstala un paquete.
- `pip list:` Muestra los paquetes instalados.
- `pip show nombre_del_paquete:` Muestra información sobre un paquete instalado.
- `pip search término_de_búsqueda:` Busca paquetes en PyPI.
pip install -r requirements.txt: Instala paquetes de un archivo de dependencias.
- `pip freeze > requirements.txt:` Genera un archivo de dependencias.
- `pip update nombre_del_paquete:` Actualiza un paquete.
  
**Ejemplo:**

Para usar la biblioteca `requests:`

```
pip install requests
```
Luego, en tu código Python:

```Python

import requests

respuesta = requests.get('https://www.ejemplo.com')
print(respuesta.status_code)
```

En conclusión, los paquetes pip son bloques de código reutilizable que extienden las capacidades de Python y se gestionan con `pip`, facilitando el desarrollo de aplicaciones.

Links de referencias:
https://www.python.org/
https://keepcoding.io/blog/como-funcionan-los-argumentos-en-python/
https://geekflare.com/es/list-comprehension-in-python/
https://ellibrodepython.com/if-python
https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/if-else-python/
https://www.datacamp.com/es/tutorial/loops-python-tutorial