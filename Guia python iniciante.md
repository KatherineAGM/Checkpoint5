# **Guía de información clave para iniciante en python**

# ¿Qué es un Condicional en Programación?

Un **condicional** es una estructura de control fundamental en programación que permite a un programa tomar decisiones y ejecutar diferentes bloques de código basándose en si una determinada **condición** es verdadera o falsa. Es como una bifurcación en el camino del programa.

## Analogía de la Vida Real

> **Si** está lloviendo, **entonces** lleva un paraguas. **Sino**, no lo lleves.

## Estructuras Condicionales Comunes

<img src="https://github.com/KatherineAGM/Checkpoint5/blob/main/condicionales.png" img width="500px">

Las más comunes son:

* **`if` (si):** El bloque de código asociado se ejecuta **solo si** la condición especificada es verdadera (`true`),  ejecuta el código al que va asociado si la condición es verdadera. En el ejemplo, sería mostrar el mensaje “No puedes beber alcohol” si el/la usuario/a tiene menos de 18 años.


* **`else` (sino):** El bloque de código asociado se ejecuta **solo si** todas las condiciones anteriores (`if` y cualquier `else if`) fueron falsas, va después de un if. Aplica el código al que está conectado si la condición que el if marca es falsa. Es decir, si A no se cumple, else B.
  
* **`else if` (sino si) / `elif` (en algunos lenguajes):** Permite verificar múltiples condiciones en secuencia. Si la condición del `if` es falsa, se evalúa la condición del primer `else if`. Si es verdadera, se ejecuta su bloque y se omite el resto. Se pueden tener múltiples `else if`,  si hay varias condiciones que comprobar antes de “decidir”, se utiliza if en la primera y elif en las siguientes. En la tabla, expresa que, si el/la usuario/a no es mayor de 18 años, sino que tiene justo los 18, puede beber alcohol legalmente.

## Condicionales anidados y operadores lógicos en Python

Los condicionales anidados en Python son el resultado de introducir un condicional dentro de otro. Como las matrioshkas, pero con requisitos en lugar de muñecas.

Como ocurre con el elif, se emplean para comprobar distintas variables. Entonces, ¿qué los distingue exactamente de esta secuencia? ¡Veámoslo!

<img src="https://github.com/KatherineAGM/Checkpoint5/blob/main/diferencias.png" img width="500px">

Otra de las dudas que pueden surgirte es si los condicionales anidados suponen una alternativa válida al operador or. Lo cierto es que ambos hacen lo mismo: determinar si, como mínimo, uno de los requisitos expresados es verdadero. Por ejemplo, estos dos códigos indican las mismas instrucciones:

<img src="https://github.com/KatherineAGM/Checkpoint5/blob/main/dudas.png" img width="500px">

Hay otros operadores lógicos que pueden sustituir las anidaciones condicionales, como el and. Emplear unos y otros depende del grado de detalle que quieras darle al código y de lo complejidad de las condiciones que haya que describir.

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
Primero, aclaremos el término iterar que significa “realizar una acción varias veces”, y cada repetición se llama iteración. Los bucles sirven para que los programas implementen iteraciones, es decir, ejecuten un mismo bloque de código dos o más veces mientras se cumple la condición declarada. Cuando la condición llega a ser falsa, el programa sale del bucle y continúa con su ejecución de forma secuencial.

**El flujo de ejecución es el siguiente:**

1. Evaluar la condición, definiendo si es verdadera o falsa (True o False).
2. Si la condición es verdadera, ejecutar el cuerpo y regresar al paso 1.
3. Si la condición es falsa, salir del bucle y continuar con la siguiente sentencia.

Python ofrece principalmente dos tipos de bucles para la ejecución repetida de bloques de código: el bucle `for` y el bucle `while`.

## 1. Bucle `for`

La sentencia `for` forma un bucle definido que recorre los elementos de una colección de datos o una secuencia ordenada como listas, diccionarios, tuplas, strings, etc. El bucle hará tantas iteraciones cuántos elementos hay en la secuencia.

**Sintaxis:**
```python
for <variable> in <secuencia>:
<bloque de código>
```
Por ejemplo, para iterar los elementos de la lista “idiomas” con un bucle for, se le asigna el nombre “idioma” a una variable que representará los elementos de la lista en cada repetición.

```python
idiomas = ['Árabe', 'Inglés', 'Francés', 'Español']
índice = 0
for idioma in idiomas:
print ('Este idioma está en la lista: ' + idiomas[índice])
índice += 1
Este idioma está en la lista: Árabe
Este idioma está en la lista: Inglés
Este idioma está en la lista: Francés
Este idioma está en la lista: Español
```
El bucle for con cadenas tipo string funciona de la misma manera, pero con caracteres en lugar de elementos:

```python
cadena = 'Python'
for carácter in cadena:
print(carácter)
P
y
t
h
o
n
```
Igual que con el bucle while, se puede usar la sentencia else para agregar una acción adicional al finalizar el bucle. Veamos un ejemplo con la función range():

```python
for x in range(5):
print(x)
else:
print('Fin del bucle')
0
1
2
3
4
Fin del bucle
```


## 2. Bucle `while`
El bucle  `while` permite repetir la ejecución de un bloque de código siempre y cuando la condición del bucle sea verdadera. Un bloque de código **mientras una condición especificada sea verdadera**. Es crucial asegurarse de que la condición eventualmente se vuelva falsa para evitar bucles infinitos.

**Sintaxis:**
```python	
1. while <condición>:
2. <bloque de código>
   
```
El código del cuerpo del bucle debe cambiar una o más variables hasta que la condición resulte falsa y el bucle termine. En este ejemplo la variable de iteración cambia el valor del parámetro cada vez que se ejecuta el ciclo y controla cuándo finaliza el ciclo.

```python
x = 5
while x > 0:
x -= 1
print(x)
print('¡Pum!')
4
3
2
1
0
¡Pum!
```
En Python se puede indicar una operación alternativa mediante la sentencia else al final del bucle while. El fragmento de código dentro de else se ejecutará una vez la condición del bucle ya no devuelve True, es decir, hasta que la condición del bucle deja de cumplirse.

```python
x = 5
while x > 0:
x -= 1
print(x)
else:
print('Fin del bucle')
4
3
2
1
0
Fin del bucle
```
Si no hay ninguna variable de iteración que determine cuántas veces tiene que ejecutar un bucle y la condición permanece verdadera, el mismo fragmento de código se repetirá para siempre, lo que producirá un bucle infinito. Normalmente, los bucles infinitos se deben a errores y hay que evitarlos para no perder el control del programa.

```python
x = 5
while x > 0:
print('¡Al infinito y más allá!')
¡Al infinito y más allá!
¡Al infinito y más allá!
¡Al infinito y más allá!
…
```
## Bucles anidados

Python permite anidar bucles metiendo uno dentro de otro. Esto puede ser útil para resolver problemas más complejos: por ejemplo, si quieres iterar algún objeto donde cada elemento tiene otra clase iterable como una lista de listas.

```python
lista = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
```
Para acceder a cada elemento individualmente, puedes anidar dos bucles for. El primero de ellos se encargará de iterar las listas anidadas, y el otro, sus elementos.

```python
for a in lista:
for b in a:
print(b)
1
2
3
4
5
6
7
8
9
```
De la misma forma puedes anidar un bucle while. Por ejemplo, te puede ayudar si quieres generar todas las combinaciones posibles de dos números:

```python
a = 0
b = 0
while a < 3:
while b < 3:
print(a,b)
b += 1
a += 1
b = 0
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```
## Control de flujo en bucles

Python proporciona palabras clave para controlar el flujo dentro de los bucles:

`break`:Sale inmediatamente del bucle.

 La sentencia **break** “rompe” el bucle en cualquier momento, aun cuando la condición sigue siendo verdadera. En el siguiente ejemplo el bucle for recorre todos los números del rango del 0 al 4, pero el programa finaliza cuando el número tenga el valor de 3:

 ```python
for x in range(5):
if x == 3:
break
print (x)
0
1
2
```
Lo mismo pasa con el bucle while: al recibir una entrada determinada, el programa sale del bucle y procede a la siguiente línea del código:

```python
while True:
respuesta = input('> ')
if respuesta == 'salir':
break
else:
print(respuesta)
print ('¡Adiós!')
> ¡Hola!
¡Hola!
> ¿Qué tal?
¿Qué tal?
> salir
¡Adiós!
```
`continue`: Salta la iteración actual y pasa a la siguiente.

La sentencia continue termina la iteración corriente sin tomar en cuenta el código que está debajo y se vuelve al inicio del bucle.

```python
x = 0
while x < 5:
x += 1
if x == 3:
continue
print(x)
1
2
4
5
```
En el ejemplo abajo, cuando el valor llegue a ‘y’, el programa saltará de nuevo al bucle for sin ejecutar la última línea de print y sin salir del bucle:

```python
for carácter in 'Python': 
if carácter == 'y':
continue
print ('La letra es:', carácter)
La letra es: P
La letra es: t
La letra es: h
La letra es: o
La letra es: n
```
`pass`: Por último, cabe mencionar la sentencia pass. Cuando la ejecución de un bucle llega a la sentencia pass, simplemente pasa a la siguiente instrucción sin modificar el flujo establecido. Habitualmente, se utiliza para reservar espacio si en el momento de escribir un código hay una parte que todavía no está completada:

```python
for x in range(1, 5):
if x == 2:
pass
print (x)
1
2
3
4
```
Python también permite utilizar la cláusula `else` con los bucles for y while. La cláusula else se ejecuta cuando el bucle termina de forma natural (es decir, no se encuentra una sentencia break). 

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
En resumen, los bucles `for` y `while` son herramientas esenciales para la repetición de código en Python, y las palabras clave **break**, **continue**, **pass** y la cláusula **else** ofrecen un control más preciso sobre su ejecución.

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

**Tipos de Argumentos en Python:**
- **Argumentos Posicionales:** Se pasan a la función en el orden en que están definidos en la definición de la función. Por ejemplo: 
```python
    def saludar(nombre, edad):
        print(f"Hola, {nombre}, tienes {edad} años.")

    saludar("Alice", 30)  # Aquí "Alice" y 30 son argumentos posicionales
```
El orden en que se pasan los argumentos es crucial. 
- A**rgumentos de Palabra Clave:** Se pasan a la función especificando el nombre del parámetro que se le está pasando. Por ejemplo:
```python
    def saludar(nombre, edad):
        print(f"Hola, {nombre}, tienes {edad} años.")

    saludar(nombre="Bob", edad=25)  # Aquí "nombre" y "edad" son argumentos de palabra clave
```
El orden en que se pasan los argumentos de palabra clave no importa. 
- **Argumentos con Valor por Defecto**: Se les asigna un valor por defecto en la definición de la función. Si no se pasa un valor para ese argumento cuando se llama a la función, se usará el valor por defecto. Por ejemplo:
 ```python
    def saludar(nombre, edad=30): # "edad" tiene un valor por defecto de 30
        print(f"Hola, {nombre}, tienes {edad} años.")

    saludar("Charlie")  # Se usa el valor por defecto de edad (30)
    saludar("David", 28) # Se usa el valor pasado (28)
```
- **Argumentos Arbitrarios (`*args y **kwargs` )**: Permiten pasar un número variable de argumentos a una función. 
1.  `*args:` Se usa para pasar un número variable de argumentos posicionales como una tupla. Por ejemplo: 
```python
  def sumar(*numeros):
       return sum(numeros)
    print(sumar(1, 2, 3))  # La función recibe una tupla (1, 2, 3)
```
2. `**kwargs:` Se usa para pasar un número variable de argumentos de palabra clave como un diccionario. Por ejemplo: 
```python
  def mostrar_informacion(**informacion):
        for clave, valor in informacion.items():
           print(f"{clave}: {valor}")

  mostrar_informacion(nombre="Eve", edad=32, ciudad="Segovia")
```
**Otros ejemplos:**

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
**En resumen:** Los argumentos son los valores que se pasan a una función para que pueda realizar su trabajo. Los tipos de argumentos permiten flexibilidad en cómo se llaman las funciones y qué datos se les pasan.
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
* `map()`: aplica una función (que puede ser una lambda) a cada elemento de un iterable (lista, tupla, etc.).
Retorna un objeto map que puede ser convertido a una lista usando list().
Ejemplo: list(map(lambda x: x * 2, [1, 2, 3])) devolverá [2, 4, 6]. 

* `filter()`: La función filter() es capaz de devolver una nueva colección con los elementos filtrados que cumplan una condición.

Podemos comprobar, por ejemplo, cuales son los números pares de una lista dada. Para ello le pasaremos una lista a una Lambda de la siguiente forma:

```python
#Tengo una lista con muchos números
comprobar = [38,24,99,42,2,3,11,23,53,21,3,53,77,12,34,92,122,1008,26]
#Creo una variable y le aplico filter() y la lambda
filt = filter(lambda x: x % 2 == 0, comprobar)
#Creo una variable para convertir el resultado de 'filt' en una lista 
pares = list(filt)
#Finalmente obtengo la lista con los resultados que han devuelto True al pasar el filtro
print(pares)
```
* `reduce()`: (en Python 3 se encuentra en el módulo functools) aplica una función a los elementos de un iterable acumulativamente. 
La función lambda toma dos argumentos: el acumulador y el siguiente elemento. 
Retorna un único valor. 
Ejemplo: from functools import reduce; reduce(lambda x, y: x + y, [1, 2, 3, 4]) devolverá 10. 
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
 Se utiliza para instalar, actualizar y eliminar paquetes de software en Python. pip es el gestor de paquetes estándar de Python, según Python documentation. 

**Detalles importantes:**
- **Instalación:**
Con pip, puedes instalar paquetes desde el Python Package Index (PyPI) o desde otros repositorios. 
- **Dependencias**:
pip resuelve automáticamente las dependencias de los paquetes, lo que significa que instala también los paquetes necesarios para que el paquete principal funcione. 
- **Versiones**:
Puedes especificar la versión de un paquete que deseas instalar. 
- **Entornos virtuales:**
pip se usa a menudo en combinación con entornos virtuales para aislar los paquetes de un proyecto en particular. 
- **Comandos:**
Los comandos comunes de pip incluyen install, uninstall, list, show, y search. 

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
### ¿Dónde se encuentran los paquetes?
Muchos paquetes se encuentran en el Python Package Index (PyPI). 

### ¿Cómo funciona?
Ejecutando comandos en la terminal (por ejemplo, pip install nombre_paquete).

### Ventajas:
- **Aislamiento de paquetes:** Permite aislar los paquetes en entornos virtuales para evitar conflictos entre versiones. 
- **Gestión de dependencias:** Identifica y resuelve las dependencias entre paquetes de manera automática. 
-**Simplificación del desarrollo:** Reduce el tiempo y esfuerzo de la gestión de bibliotecas. 

### ¿Cómo instalar pip?
Por lo general, Python viene con pip incluido en versiones a partir de 2.7.9 y 3.4. Si no, puedes instalarlo usando get-pip.py. 

En conclusión, los paquetes pip son bloques de código reutilizable que extienden las capacidades de Python y se gestionan con `pip`, facilitando el desarrollo de aplicaciones.

Links de referencias:
https://www.python.org/
https://keepcoding.io/blog/como-funcionan-los-argumentos-en-python/
https://geekflare.com/es/list-comprehension-in-python/
https://ellibrodepython.com/if-python
https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/if-else-python/
https://www.datacamp.com/es/tutorial/loops-python-tutorial
https://www.tokioschool.com/noticias/condicionales-python/
