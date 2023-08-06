# De acuerdo a la consiga de Ticmas realizo lo siguiente:
# Sueldos de Juan en diferentes meses

sueldos_por_mes = [
    300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700
]

# Calcular el sueldo promedio de Juan
sueldo_promedio = sum(sueldos_por_mes) / len(sueldos_por_mes)

# Definir los limites de ingresos promedios para sueldo bajo, normal y mejor de lo normal
sueldo_bajo = 300
sueldo_normal = 900

# Determinar la categoría del sueldo de Juan
if sueldo_promedio < sueldo_bajo:
    categoria = "bajo"
elif sueldo_promedio <= sueldo_normal:
    categoria = "normal"
else:
    categoria = "mejor de lo normal"

# Mostrar el sueldo promedio y la categoría correspondiente
print(f"El sueldo promedio de Juan es: {sueldo_promedio} dólares")
print(f"Su sueldo es considerado {categoria}.")
