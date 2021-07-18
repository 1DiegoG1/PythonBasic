def main():
    nombre = input("Enter a name: ")
    for letra in nombre:
        print(letra)
    
    frase = input("Enter a frase")
    for caracter in frase:
        print(caracter.upper())
    
if __name__ == "__main__":
    main()