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

Caso de prueba
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



