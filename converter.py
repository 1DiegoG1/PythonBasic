# Pedimos la cifra a calcular
pesos = float(input("¿Cuátos pesos colombianos tienes?: "))
# Valor actual del dolar en la moneda deseada
dolar_value_col = 3820.98
# Se realiza la conversión, dividiendo la moneda deseada con el valor del dólar
dollars = pesos / dolar_value_col
# Se rondea los dólares, para mostrar sólo dos dígitos en los décimales
dollars = round(dollars, 2)
# Se convierte la cantidad de los dólares a string
dollars = str(dollars)
# ¡Se imprime en pantalla la conversión realizada con éxito!
print(f"Tienes $ {dollars} dollars")

# Pedimos la cifra a calcular
bolívares = float(input("¿Cuátos bolívares tienes?: "))
# Valor actual del dolar en la moneda deseada
dolar_value_ven = 3239654.00
# Se realiza la conversión, dividiendo la moneda deseada con el valor del dólar
dollars = bolívares / dolar_value_ven
# Se rondea los dólares, para mostrar sólo dos dígitos en los décimales
dollars = round(dollars, 2)
# Se convierte la cantidad de los dólares a string
dollars = str(dollars)
# ¡Se imprime en pantalla la conversión realizada con éxito!
print(f"Tienes $ {dollars} dollars")


