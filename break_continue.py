def main():
#  for counter in range(1001):
#      if counter % 2 != 0:
#          continue
#      print(counter)
    # for i in range(10000):
    #     print(i)
    #     if i == 5140:
    #         break

    text = input("Enter a word: ")
    for letter in text:
        print(letter)
        if letter == 'z':
            break 
        
if __name__ == '__main__':
    main()