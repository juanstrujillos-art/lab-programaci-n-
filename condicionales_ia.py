
def obtener_corriente(voltaje, resistencia_a, resistencia_b):
    corriente = voltaje / (resistencia_a + resistencia_b)
    return corriente


print("===== ANALISIS DEL DIVISOR =====")

# Ingreso de los datos

voltaje_entrada = float(input("Digite el voltaje de entrada en voltios: "))

resistencia_1 = float(input("Digite el valor de la primera resistencia en ohmios: "))


print("\nSeleccione la potencia maxima de la resistencia 1:")
print("1. 0.25 W")
print("2. 0.50 W")
print("3. 1.00 W")

seleccion_1 = int(input("Digite el numero de la opcion: "))

if seleccion_1 == 1:
    limite_1 = 0.25
elif seleccion_1 == 2:
    limite_1 = 0.50
elif seleccion_1 == 3:
    limite_1 = 1
else:
    print("La opcion ingresada no es correcta.")
    limite_1 = 0


resistencia_2 = float(input("\nDigite el valor de la segunda resistencia en ohmios: "))


print("\nSeleccione la potencia maxima de la resistencia 2:")
print("1. 0.25 W")
print("2. 0.50 W")
print("3. 1.00 W")

seleccion_2 = int(input("Digite el numero de la opcion: "))

if seleccion_2 == 1:
    limite_2 = 0.25
elif seleccion_2 == 2:
    limite_2 = 0.50
elif seleccion_2 == 3:
    limite_2 = 1
else:
    print("La opcion ingresada no es correcta.")
    limite_2 = 0


# Obtencion de la corriente

corriente_total = obtener_corriente(
    voltaje_entrada,
    resistencia_1,
    resistencia_2
)


# Calculo de la potencia

consumo_1 = corriente_total ** 2 * resistencia_1
consumo_2 = corriente_total ** 2 * resistencia_2


print("\n===== DATOS OBTENIDOS =====")

print("Corriente del circuito:", corriente_total, "A")
print("Corriente del circuito:", corriente_total * 1000000, "uA")

print("\nPotencia en la resistencia 1:", consumo_1, "W")
print("Potencia en la resistencia 2:", consumo_2, "W")


# Comprobacion de la primera resistencia

print("\n===== REVISION DE RESISTENCIA 1 =====")

if consumo_1 <= limite_1:
    print("La resistencia 1 trabaja correctamente con la potencia seleccionada.")
else:
    print("La resistencia 1 supera el limite de potencia seleccionado.")


# Comprobacion de la segunda resistencia

print("\n===== REVISION DE RESISTENCIA 2 =====")

if consumo_2 <= limite_2:
    print("La resistencia 2 trabaja correctamente con la potencia seleccionada.")
else:
    print("La resistencia 2 supera el limite de potencia seleccionado.")
