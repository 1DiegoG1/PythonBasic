"""
- [name] converter
- [summary] The function converts a currency to dollars
- [param] currency_type is the currency type that it's will be converted to dollars
- [param] dolar_value is the dollar value in the selected currency
"""
def converter(currency_type, dolar_value):
    currency = float(input(f"¿How much {currency_type} do you have?: "))
    dollars = currency / dolar_value
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print(f"You have: {dollars} USD")

option = int(input((""""
WELCOME TO THE CURRENCY CONVERTER $$$

1 - COP (pesos colombianos)
2 - ARG (pesos argentinos)
3 - MXN (pesos mexicanos)
4 - VEF (bolívares fuertes)

Select an option!: """)))

if option == 1:
    converter("COP", 3815.03)
elif option == 2:
    converter("ARG", 95.94)
elif option == 3:
    converter("MXN", 19.96)
elif option == 4:
    converter("VEF", 3700022.18)
else:
    print(f"¡Oooops!. {option} no es una opcion correcta, ¡vuelve a intentarlo!")