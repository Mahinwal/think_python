def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False

if __name__ == '__main__':
    word1 = input("Enter word1: ").strip()
    word2 = input("Enter word1: ").strip()
    print(anagram(word1, word2))