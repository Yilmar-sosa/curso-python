notas = [70, 85, 90, 60, 75]
suma = 0
for nota in notas:
    suma = suma + nota
promedio = suma / len(notas)
print(f"La suma total de los valores de esta lista {notas} es: {suma}")
print(f"El promedio es de: {promedio}")