# Program to add natural numbers up to n
# sum = 1+2+3+...+n

def add_nums(n):
    i = 1
    sum = 0

    while i <= n:
        sum +=i
        i +=1
    return sum

if __name__ == '__main__':
    n = int(input("Enter n:"))
    sum = add_nums(n)
    print("Sum for first "+ str(n) +" numbers are:", sum)
    