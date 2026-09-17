# lab-programaci-n-
# Laboratorio: Lógica de Programación 

Asignatura: Programación (II-2026)  
Profesor: Alexander López-Parrado   
Institución: Universidad del Quindío 

Integrantes
* JUANITA MORALES CORREA 
* JUAN FELIPE CABRERA MEDINA 
* JUAN SEBASTIAN TRUJILLO SUAREZ 

Introducción 
Este repositorio contiene la solución algorítmica y las simulaciones desarrolladas para el análisis de un divisor de tensión resistivo, aplicando estructuras de datos, condicionales, ciclos, funciones y PySpice en Python.

0. Código de Corrientes (`codigo_corrientes.py`)

Este script calcula la corriente eléctrica (I) que circula a través de un divisor de tensión resistivo compuesto por dos resistencias en serie (R_1 y R_2). El programa solicita los valores de entrada al usuario, aplica la Ley de Ohm y entrega el resultado expresado en Amperios (A) y Miliamperios (mA).

Caso de prueba:
Ingrese el voltaje de entrada (V): 12
Ingrese el valor de R1 (ohmios): 10000
Ingrese el valor de R2 (ohmios): 2000
La corriente que circula por el divisor es: 0.001 A
La corriente es: 1.0 mA

1. Sentencias Condicionales (`punto2_condicionales_grupo.py` y `punto2_condicionales_ia.py`)

Este programa evalúa la potencia disipada por cada resistencia a partir del voltaje de entrada y los valores de R_1 y R_2. Compara la potencia calculada con la potencia nominal máxima especificada e informa al usuario si los componentes operan dentro de un rango térmico seguro.

Caso de prueba:
Ingrese el voltaje de entrada Vin (V): 12
Ingrese el valor de R1 (ohmios): 10000
Ingrese el valor de R2 (ohmios): 2000
Corriente del circuito: 0.001 A

Resistencia R1:
Potencia calculada: 0.01 W
Potencia máxima: 0.25 W
R1 opera dentro del rango permitido de potencia.

Resistencia R2:
Potencia calculada: 0.002 W
Potencia máxima: 0.5 W
R2 opera dentro del rango permitido de potencia.

2. Ciclos y Arreglos (`punto3_ciclos_grupo.py` y `punto3_ciclos_ia.py`)

Este programa fija un voltaje de entrada de 5V y una corriente de 100uA. Solicita al usuario una cantidad deseada de voltajes de salida (Vout) e implementa un ciclo de validación para garantizar que cada voltaje esté en el rango de 0V a 5V. Calcula los valores requeridos para R1 y R2, los almacena en listas independientes e imprime finalmente los valores máximo y mínimo calculados para cada resistencia.

Caso de prueba:
¿Cuántos voltajes de salida desea ingresar?: 3
Ingrese el voltaje de salida (0 < Vout < 5 V): 2
Ingrese el voltaje de salida (0 < Vout < 5 V): 4
Ingrese el voltaje de salida (0 < Vout < 5 V): 3.5

Valores calculados:
Vout = 2.0 V
R1 = 30000.0 ohm
R2 = 20000.0 ohm

Vout = 4.0 V
R1 = 10000.0 ohm
R2 = 40000.0 ohm

Vout = 3.5 V
R1 = 15000.0 ohm
R2 = 35000.0 ohm

R1 mínimo = 10000.0 ohm
R1 máximo = 30000.0 ohm
R2 mínimo = 20000.0 ohm
R2 máximo = 40000.0 ohm

3. Funciones (`punto4_funciones_grupo.py` y `punto4_funciones_ia.py`)

Este programa modulariza la solución del problema mediante el uso de funciones. Implementa funciones específicas para la lectura de datos con validación, el cálculo numérico de las resistencias R1 y R2 a partir de un arreglo de voltajes de salida (Vout) con Vin fijo en 5V e I en 100uA, y la impresión organizada de los resultados.

Caso de prueba:
Ingrese el voltaje de entada: 10
Ingrese la corriente: 0.1
Ingrese el voltaje de salida Vout (V): 6

Resultados:
R1 = 40.0 ohm
R2 = 60.0 ohm
Potencia nominal de R1 = 0.5 W
Potencia nominal de R2 = 1 W



