if __name__ == '__main__':
    n = int(input())
    int_list = list(map(int, input().split()))
    tp = tuple(int_list)
    print(hash(tp))