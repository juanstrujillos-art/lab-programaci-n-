Vin = 5
I = 0.0001

cantidad = int(input("¿Cuántos voltajes de salida desea ingresar?: "))

lista_R1 = []
lista_R2 = []

for i in range(cantidad):

    Vout = float(input("Ingrese el voltaje de salida (0 < Vout < 5 V): "))

    while Vout <= 0 or Vout >= 5:
        print("Voltaje no válido. Debe estar entre 0 y 5 V.")
        Vout = float(input("Ingrese nuevamente el voltaje de salida: "))

    R2 = Vout / I
    R1 = (Vin / I) - R2

    lista_R1.append(R1)
    lista_R2.append(R2)

print("\nValores calculados:")

for i in range(cantidad):
    print("Vout =", lista_R2[i] * I, "V")
    print("R1 =", lista_R1[i], "ohm")
    print("R2 =", lista_R2[i], "ohm")
    print()

print("R1 mínimo =", min(lista_R1), "ohm")
print("R1 máximo =", max(lista_R1), "ohm") 

print("R2 mínimo =", min(lista_R2), "ohm") 
print("R2 máximo =", max(lista_R2), "ohm") 
