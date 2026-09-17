Vin = float(input("Ingrese el voltaje de entrada Vin (V): "))

R1 = float(input("Ingrese el valor de R1 (ohmios): "))
R2 = float(input("Ingrese el valor de R2 (ohmios): "))

Pmax1 = 0.25
Pmax2 = 0.5
Pmax3 = 1

I = Vin / (R1 + R2)


P1 = I**2 * R1
P2 = I**2 * R2

print("Corriente del circuito:", I, "A")

print("\nResistencia R1:")
print("Potencia calculada:", P1, "W")
print("Potencia máxima:", Pmax1, "W")

if P1 <= Pmax1:
    print("R1 opera dentro del rango permitido de potencia.")
elif P1 <= Pmax2:
    print("R1 opera dentro del rango permitido de potencia.")
elif P1 <= Pmax3:
    print("R1 opera dentro del rango permitido de potencia.")
else:
    print("R1 SUPERA el rango permitido de potencia.")

print("\nResistencia R2:")
print("Potencia calculada:", P2, "W")
print("Potencia máxima:", Pmax2, "W")

if P2 <= Pmax2:
    print("R2 opera dentro del rango permitido de potencia.")
elif P2 <= Pmax2:
    print("R1 opera dentro del rango permitido de potencia.")
elif P2 <= Pmax3:
    print("R1 opera dentro del rango permitido de potencia.")
else:
    print("R2 SUPERA el rango permitido de potencia.")
