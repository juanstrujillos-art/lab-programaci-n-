# Valores fijos solicitados por la guia

Vin = 5
I = 100e-6

# Listas donde se almacenarán los valores

R1_lista = []
R2_lista = []
Vout_lista = []


print("=== CALCULO DE RESISTENCIAS ===")
print("Vin = 5 V")
print("I = 100 uA")

# Cantidad de voltajes

cantidad = int(input("\nIngrese el numero de voltajes de salida: "))


# Ciclo para solicitar los voltajes

for i in range(cantidad):

    Vout = float(input(
        f"Ingrese el voltaje de salida Vout #{i + 1} (0 < Vout < 5): "
    ))

    # Verificacion del valor de Vout

    while Vout <= 0 or Vout >= 5:

        print("ERROR: el voltaje debe cumplir 0 < Vout < 5.")

        Vout = float(input(
            f"Ingrese nuevamente Vout #{i + 1}: "
        ))

    # Calculo de R2

    R2 = Vout / I

    # Calculo de R1

    R1 = (Vin - Vout) / I

    # Guardar los resultados en las listas

    Vout_lista.append(Vout)
    R1_lista.append(R1)
    R2_lista.append(R2)


# Mostrar resultados

print("\n=== RESULTADOS ===")

for i in range(cantidad):

    print(f"\nVout #{i + 1}")
    print("Vout =", Vout_lista[i], "V")
    print("R1 =", R1_lista[i], "ohmios")
    print("R2 =", R2_lista[i], "ohmios")


# Valores maximos y minimos

print("\n=== VALORES MAXIMOS Y MINIMOS ===")

print("R1 maxima =", max(R1_lista), "ohmios")
print("R1 minima =", min(R1_lista), "ohmios")

print("R2 maxima =", max(R2_lista), "ohmios")
print("R2 minima =", min(R2_lista), "ohmios")
