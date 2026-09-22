cuenta = float(input("Ingrese el valor de la cuenta: "))
porcentaje = int(input("Ingrese el porcentaje de propina(10, 15, 20): "))

propina = cuenta * porcentaje / 100
cuenta_total = cuenta + propina

print(f'''Cuenta: ${cuenta}\nPorcentaje de la propina: {porcentaje} % = ${propina}\n
Total: ${cuenta_total}''')

