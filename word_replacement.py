def word_replacement(word_to_replace, word_replacement):
    str = "This is a python string for testing the word replacement programe."
    print(str.replace(word_to_replace, word_replacement))

if __name__ == '__main__':
    word_to_replace = input("Enter the word to replace :").strip()
    word_replace = input("Enter the word replacement : ").strip()
    word_replacement(word_to_replace, word_replace)