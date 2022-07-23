# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

print('Ingrese el primer valor:')
num_01 = float(input())
print('Ingrese el segundo valor:')
num_02 = float(input())

suma = num_01+num_02
resta = num_01-num_02
multiplicacion = num_01*num_02
division = num_01/num_02
potenciacion = num_01**num_02

print('La suma entre', num_01, 'y', num_02, 'es', suma)
print('La resta entre', num_01, 'y', num_02, 'es', resta)
print('La multiplicacion entre', num_01, 'y', num_02, 'es', multiplicacion)
print('La division entre', num_01, 'y', num_02, 'es', division)
print('La potenciacion entre', num_01, 'y', num_02, 'es', potenciacion)