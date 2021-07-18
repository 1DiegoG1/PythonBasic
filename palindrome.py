"""
- [name] palindrome
- [summary]
- [param] word, type: string 
"""
def palindrome(word):
    word = word.replace(' ', '')
    word = word.lower()
    reverted_word = word[::-1]
    if word == reverted_word:
        return True
    else:
        return False


def main():
    word = input("Escribe una palabra: ")
    its_palindrome = palindrome(word)
    if its_palindrome == True:
        print("It's palindrome!")
    else:
        print("It isn't palindrome")


if __name__ == '__main__':
    main()