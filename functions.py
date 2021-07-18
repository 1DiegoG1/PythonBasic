# def imprimir_mensaje ():
#     print('Mensaje especial: ')
#     print('Estoy aprendiendo a usar funciones!')


# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()
"""
- [name] conversation
- [summary] The function displays a message and calls itself.
- [param] message, type: string
"""
def conversation(message):
    print('Hello!')
    print("How are you?")
    print(message)
    print("Bye!")

opcion = int(input('Select an option! (1, 2, 3): '))
if opcion == 1:
    conversation("XD")
elif opcion == 2:
    conversation("OWO")
elif opcion == 3:
    conversation("._. xD")
else:
    print("Select a correct option!")