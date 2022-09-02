def check_palindrome(word):
    new_str = word.lower()
    if new_str == new_str[::-1]:
        return "Palindrome"
    else:
        return "Not palindrome!"

if __name__ == '__main__':
    word = input("Enter the word to check palindrome or not :").strip()
    print("The entered word is ", check_palindrome(word))