def count_palindrome_words(sentance):
    words = []
    sentance = sentance.split(" ")
    for word in sentance:
        if word == word[::-1]:
            words.append(word)
    if not words:
        return "No palindrome word found..."
    else:
        return words

if __name__ == '__main__':
    sentance = input().strip()
    words = count_palindrome_words(sentance)
    print(words)