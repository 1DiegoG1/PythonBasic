"""
- [name] is_prime
- [summary] The function determines if n is a prime number or not.
"""
def is_prime(n):
    n2 = n % 1 
    print(n2)
    n3 = n % n
    print(n3)
    if n2 or n3 == 0 :
        print("The number is Prime!")
        return True
    else:
        print("The number is not prime!")
        return False
    
def main():
    number = int(input("Enter a integer number: "))
    is_prime(number)


if __name__ == '__main__':
    main() 