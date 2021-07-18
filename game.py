import random
def main():
    random_number = random.randint(1, 100)
    enter_number = int(input("Enter a number from 1 to 100 : "))
    while enter_number != random_number:
        if enter_number > random_number:
            print("No! please enter a smaller number!")
        else:
            print("No! please enter a larger number!")
        enter_number = int(input("Enter a number from 1 to 100 : "))
    print("You won!")
        
              

if __name__ == '__main__':
    main()