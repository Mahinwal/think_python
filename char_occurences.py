def count_characters(word):
    new_string = word.lower()
    count = {"space": 0}
    space = 0
    for i in new_string:
        if i.isspace():
            count['space'] +=1
        else:
            if i in count:
                count[i] +=1
            else:
                count[i] = 1
    return count

if __name__ == '__main__':
    word = input("Enter the sentance: ").strip()
    char_counts = count_characters(word)
    print("count charater in the given sentance are: ", char_counts)
    print("The space count in the given sentace is: ", char_counts['space'])