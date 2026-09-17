Vin = float(input("Ingrese el voltaje de entrada (V): "))
R1 = float(input("Ingrese el valor de R1 (ohmios): "))
R2 = float(input("Ingrese el valor de R2 (ohmios): "))

I = Vin / (R1 + R2)
I_mA = I * 1000

print("La corriente que circula por el divisor es:", I, "A")
print("La corriente es:", I_mA, "mA")
