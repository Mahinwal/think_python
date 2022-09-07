def main():
    rows = int(input("Enter the number of rows: "))
    for i in range(1, rows+1):
        for j in range(0, i):
           print(i*2 - 1, end='')
        print('')

if __name__ == '__main__':
    main()