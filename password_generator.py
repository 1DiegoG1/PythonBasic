import random
"""
- [name] generate_password 
- [summary] The function generates a password with 20 randoms chars.
- [returns] The generated password.
"""
def generate_password () :
    MAJUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMBS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    SYMBLS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    CHARS = MAJUS + MINUS + SYMBLS + NUMBS 
    
    password = []
    
    for i in range(20):
        chars_random = random.choice(CHARS)
        password.append(chars_random)
        
    password = ''.join(password)
    return password


def main():
    password = generate_password()
    print(f"Your new password is: {password}")

if __name__ == '__main__':
    main()