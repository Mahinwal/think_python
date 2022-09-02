def pascal_triangle(num):

    for i in range(num):
        print(' '.join(map(str, str(11**i))))

if __name__ == '__main__':
    n = int(input("Enter the number number for Pascal triangle: "))
    pascal_triangle(n)
