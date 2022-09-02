def mutate_string(strings, pos, char):
    ls = [i for i in strings]
    del ls[pos]
    ls.insert(pos, char)
    return "".join(ls)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    new_string = mutate_string(s, int(i), c)
    print(new_string)