def calcular_resistencias(Vin, I, Vout):


    R2 = Vout / I
    R1 = (Vin / I) - R2


    P1 = I**2 * R1
    P2 = I**2 * R2


    if P1 <= 0.25:
        Pmax1 = 0.25
    elif P1 <= 0.5:
        Pmax1 = 0.5
    else:
        Pmax1 = 1


    if P2 <= 0.25:
        Pmax2 = 0.25
    elif P2 <= 0.5:
        Pmax2 = 0.5
    else:
        Pmax2 = 1


    return [R1, R2, Pmax1, Pmax2]




Vin = float(input("Ingrese el voltaje de entada: "))
I = float(input("Ingrese la corriente: "))
Vout = float(input("Ingrese el voltaje de salida Vout (V): "))




resultado = calcular_resistencias(Vin, I, Vout)


print("\nResultados:")
print("R1 =", resultado[0], "ohm")
print("R2 =", resultado[1], "ohm")
print("Potencia nominal de R1 =", resultado[2], "W")
print("Potencia nominal de R2 =", resultado[3], "W")

