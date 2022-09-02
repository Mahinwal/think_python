if __name__ == '__main__':
    n = int(input())
    items = []
    for i in range(0, n):
        ls = input().split()
        if 'insert' in ls:
            items.insert(int(ls[1]), int(ls[2]))
        elif 'remove' in ls:
            items.remove(int(ls[1]))
        elif 'append' in ls:
            items.append(int(ls[1]))
        elif 'sort' in ls:
            items.sort()
        elif 'pop' in ls:
            items.pop()
        elif 'reverse' in ls:
            items.reverse()
        else:
            print(items)

# Sample input
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample output
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]