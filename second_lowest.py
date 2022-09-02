if __name__ == '__main__':
    n = int(input())
    items = []
    scores = []
    names = []
    for i in range(0,n):
        name = input()
        score = float(input())
        scores.append(score) # Created list of scores
        items.append([name, score]) # Created list of name and score
    
    scores.sort() # sort the list by default is ASC order
    second_low = scores[scores.count(scores[0])] # Get second lowest from the scores list
    
    for i in items:
        if second_low in i:
            names.append(i[0])
        names.sort()
    print(*names, sep="\n")