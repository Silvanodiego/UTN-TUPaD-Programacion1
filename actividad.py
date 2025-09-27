#Actividad 1
print("Hola Mundo!")

#Actividad 2
# Pido al usuario que ingrese su nombre
nombre = input("Por favor, ingresa tu nombre: ")
# Muestro un saludo usando el nombre que ingresó
print(f"Hola {nombre}!")


#Actividad 3
# Pido todos los datos al usuario uno por uno
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
lugar = input("¿Dónde vives? ")

# Uno todos los datos en una sola oración
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")


#Actividad 4
# Importo math para usar el número pi
import math

# Pido el radio del círculo
radio = float(input("Ingresa el radio del círculo: "))

# Calculo el área (pi por radio al cuadrado)
area = math.pi * radio ** 2

# Calculo el perímetro (2 por pi por radio)
perimetro = 2 * math.pi * radio

# Muestro los resultados con 2 decimales
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")


#Actividad 5
# Pido los segundos al usuario
segundos = int(input("Ingresa la cantidad de segundos: "))

# Calculo las horas (segundos dividido 3600)
horas = segundos / 3600

# Muestro el resultado
print(f"{segundos} segundos equivalen a {horas:.2f} horas")


#Actividad 6
# Pido el número al usuario
numero = int(input("Ingresa un número: "))

# Muestro el título de la tabla
print(f"Tabla de multiplicar del {numero}:")

# Uso un ciclo for para mostrar la tabla del 1 al 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


#Actividad 7
# Pido dos números al usuario
num1 = int(input("Ingresa el primer número (no cero): "))
num2 = int(input("Ingresa el segundo número (no cero): "))

# Realizo todas las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

# Muestro todos los resultados
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicación es: {multiplicacion}")
print(f"La división es: {division:.2f}")


#Actividad 8
# Pido altura y peso al usuario
altura = float(input("Ingresa tu altura en metros (ej: 1.75): "))
peso = float(input("Ingresa tu peso en kg: "))

# Calculo el IMC (peso dividido altura al cuadrado)
imc = peso / (altura ** 2)

# Muestro el resultado
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")


#Actividad 9
# Pido la temperatura en Celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Convierto a Fahrenheit usando la fórmula
fahrenheit = (9/5) * celsius + 32

# Muestro el resultado
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")


#Actividad 10
# Pido tres números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

# Calculo el promedio (suma dividido 3)
promedio = (num1 + num2 + num3) / 3

# Muestro el resultado
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")
