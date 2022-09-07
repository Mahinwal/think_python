def main():
    rows = int(input("Enter the number of rows: "))

    for i in range(rows, 0, -1):
        for j in range(0, i+1):
            print(j, end=' ')
        print('')


if __name__ == '__main__':
    main()