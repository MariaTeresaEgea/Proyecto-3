# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencias_letras(cadena): # esta funcion recibe una cadena y devuelve un diccionario con la frecuencia de cada letra 
    cadena = cadena.replace(" ", "")          # quitamos espacios
    frecuencias = {}

    for letra in cadena:
        if letra in frecuencias:
            frecuencias[letra] += 1  # si ya existe se suma 1
        else:
            frecuencias[letra] = 1 # si no existe se inicia en 1

    return frecuencias

#Ejemplo: 

print(frecuencias_letras("hola mundo")) 

    
# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

ef doble_lista(numeros):
    return list(map(lambda x: x * 2, numeros))

#Ejemplo: 

print(doble_lista([1, 2, 3, 4]))

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def palabras_con_objetivo(lista_palabras, objetivo): # filtra y devuelve las palabras que contienen una subcadena especifica. 
    return [palabra for palabra in lista_palabras if objetivo in palabra]

#Ejemplo: 

lista = ["python", "pyme", "piloto", "pyramid", "java"]
print(palabras_con_objetivo(lista, "py"))

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

# Ejemplo

print(diferencia_listas([10, 20, 30], [1, 2, 3]))

# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def media_y_estado(numeros, nota_aprobado=5): # calcula la media y compara con una nota mínima, en este caso 5. De vuelve una tupla
    if not numeros:
        return (0, "suspenso") # si no hubiese elemento, se considera el suspenso

    media = sum(numeros) / len(numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n < 0:
        raise ValueError("El factorial no existe para números negativos")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda t: "".join(map(str, t)), lista_tuplas))

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.
# pide dos números e intenta dividirlos. 

def dividir_interactivo():
    try:
        a = float(input("Introduce el numerador: "))
        b = float(input("Introduce el denominador: "))
        resultado = a / b
    except ValueError:
        print("Error: Debes introducir valores numéricos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        print("División exitosa. Resultado =", resultado)

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

prohibidas = {"Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"}

def filtrar_mascotas(lista_mascotas):
    return list(filter(lambda m: m not in prohibidas, lista_mascotas))

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception):
    pass

def promedio_lista(lista):
    if not lista:
        raise ListaVaciaError("La lista está vacía")
    return sum(lista) / len(lista)

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

# pide una edad válida y maneja los errores

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera de rango")
    except ValueError as e:
        print(" Error:", e)
        return None
    else:
        print(" Edad válida:", edad)
        return edad

#12. Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().

def longitudes_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

#13. Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

def mayus_minus_unicas(caracteres):
    unicos = list(dict.fromkeys(caracteres))  # elimina repetidos pero respeta el orden
    return list(map(lambda c: (c.upper(), c.lower()), unicos))

#14. Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

def palabras_con_inicial(lista, letra):
    return list(filter(lambda p: p.startswith(letra), lista))

#15. Crea una función lambda que sume 3 a cada número de una lista dada.

suma_tres = lambda lista: list(map(lambda x: x + 3, lista))

#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter(). Filtra palabras cuyo tamaño sea mayor que n. 

def palabras_mas_largas(frase, n):
    return list(filter(lambda p: len(p) > n, frase.split()))

#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().

from functools import reduce

def digitos_a_numero(digitos):
    return reduce(lambda a, b: a * 10 + b, digitos, 0)

#18.Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

def estudiantes_destacados(estudiantes):
    return list(filter(lambda e: e["calificacion"] >= 90, estudiantes))

#19. Crea una función lambda que filtre los números impares de una lista dada.

filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

#20. Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().

def solo_enteros(lista):
    return list(filter(lambda x: isinstance(x, int) and not isinstance(x, bool), lista))

#21. Crea una función que calcule el cubo de un número dado mediante una función lambda.

cubo = lambda x: x ** 3

#22. Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().

from functools import reduce
import operator

def producto_total(lista):
    if not lista:
        return 0
    return reduce(operator.mul, lista, 1)

#23. Concatena una lista de palabras. Usa la función reduce().

from functools import reduce

def concatenar_palabras(palabras):
    if not palabras:
        return ""
    return reduce(lambda a, b: a + " " + b, palabras)

#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

from functools import reduce

def diferencia_total(lista):
    if not lista:
        return 0
    return reduce(lambda a, b: a - b, lista)

#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(cadena):
    return len(cadena)

#26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda a, b: a % b

#27. Crea una función que calcule el promedio de una lista de números.

def promedio(lista):
    return sum(lista) / len(lista) if lista else 0

#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    vistos = set()
    for elem in lista:
        if elem in vistos:
            return elem
        vistos.add(elem)
    return None

#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.

def enmascarar(valor):
    cadena = str(valor)
    if len(cadena) <= 4:
        return cadena
    return "#" * (len(cadena) - 4) + cadena[-4:]

#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

from collections import Counter

def son_anagramas(a, b):
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    return Counter(a) == Counter(b)

#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.

class NombreNoEncontradoError(Exception):
    pass

def buscar_nombre_interactivo():
    nombres = input("Introduce nombres separados por comas: ").split(",")
    nombres = [n.strip() for n in nombres if n.strip()]

    objetivo = input("Introduce el nombre a buscar: ").strip()

    if objetivo in nombres:
        print(f"✔️ Nombre encontrado: {objetivo}")
        return True
    else:
        raise NombreNoEncontradoError(f" {objetivo} no está en la lista")
    
    #32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_puesto(nombre_completo, empleados):
    for empleado in empleados:
        if empleado.get("nombre") == nombre_completo:
            return empleado.get("puesto")
    return "La persona no trabaja aquí"

#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_elementos = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

#34. Crea la clase Arbol
#Define un árbol genérico con un tronco y ramas como atributos.
#Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
#Código a seguir:
#Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#Implementar el método quitar_rama para eliminar una rama en una posición específica.
#Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.
#Caso de uso:
#        a. Crear un árbol.
#        b. Hacer crecer el tronco una unidad.
#        c. Añadir una nueva rama.
#        d. Hacer crecer todas las ramas una unidad.
#        e. Añadir dos nuevas ramas.
#        f. Retirar la rama situada en la posición 2.
#        g. Obtener información sobre el árbol.

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [r + 1 for r in self.ramas]

    def quitar_rama(self, posicion):
        index = posicion - 1
        if 0 <= index < len(self.ramas):
            self.ramas.pop(index)
        else:
            raise IndexError("Posición fuera de rango")

    def info_arbol(self):
        return {
            "tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }
    
    #35 Crea la clase UsuarioBanco
#Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
#Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
#Código a seguir:
#Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
#Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
#Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
#Implementar agregar_dinero para aumentar el saldo del usuario.
#Caso de uso:
#        a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#        b. Agregar 20 unidades al saldo de Bob.
#        c. Transferir 80 unidades de Bob a Alicia.
#        d. Retirar 50 unidades del saldo de Alicia.

    class FondosInsuficientesError(Exception):
    pass

class UsuarioBanco:
    def __init__(self, nombre, saldo=0, cuenta_corriente=False):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad < 0:
            raise ValueError("Cantidad inválida")
        if self.saldo < cantidad:
            raise FondosInsuficientesError("Fondos insuficientes")
        self.saldo -= cantidad

    def transferir_dinero(self, destino, cantidad):
        if self.saldo < cantidad:
            raise FondosInsuficientesError("Fondos insuficientes")
        self.saldo -= cantidad
        destino.saldo += cantidad

    def agregar_dinero(self, cantidad):
        if cantidad < 0:
            raise ValueError("Cantidad inválida")
        self.saldo += cantidad

        #36 Crea una función llamada procesar_texto
# Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
# Código a seguir:
# Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
# Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
# Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
# Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
# Caso de uso:
# Verificar el funcionamiento completo de procesar_texto

        from collections import Counter

def contar_palabras(texto):
    return dict(Counter(texto.split()))

def reemplazar_palabras(texto, original, nueva):
    return texto.replace(original, nueva)

def eliminar_palabra(texto, palabra):
    return " ".join(p for p in texto.split() if p != palabra)
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción inválida")
    
    #37 Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.

    def periodo_por_hora(hora):
    if hora < 0 or hora > 23:
        raise ValueError("Hora inválida")
    if 6 <= hora < 12:
        return "mañana"
    elif 12 <= hora < 20:
        return "tarde"
    else:
        return "noche"
    
    #38 Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.

    def calificacion_texto(nota):
    if nota < 0 or nota > 100:
        raise ValueError("Nota fuera de rango")

    if nota <= 69:
        return "insuficiente"
    elif nota <= 79:
        return "bien"
    elif nota <= 89:
        return "muy bien"
    else:
        return "excelente"
    
    #39 Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

    import math

def area_figura(figura, datos):
    figura = figura.lower()

    if figura == "rectangulo":
        largo, ancho = datos
        return largo * ancho

    elif figura == "circulo":
        (radio,) = datos
        return math.pi * radio**2

    elif figura == "triangulo":
        base, altura = datos
        return 0.5 * base * altura

    else:
        raise ValueError("Figura desconocida")
    
    #40 Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. 

    def aplicar_descuento():
    try:
        precio = float(input("Precio original: "))
        tiene_cupon = input("¿Tiene cupón? (sí/no): ").lower()

        descuento = 0
        if tiene_cupon in ("sí", "si", "s"):
            descuento = float(input("Introduce el valor del cupón: "))
            if descuento <= 0:
                print("Cupón inválido. No se aplica descuento.")
                descuento = 0

        precio_final = max(0, precio - descuento)
        print("Precio final:", precio_final)

    except ValueError:
        print("Error: Entrada inválida.")