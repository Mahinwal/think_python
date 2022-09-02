if __name__ == '__main__':
    x = int(input("Enter value of x:"))
    y = int(input("Enter value of y:"))
    z = int(input("Enter value of z:"))
    n = int(input("Enter value of n:"))
    perms = []

    for i in range(0, x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                if i + j + k != n:
                    perms.append([i, j, k])

    # for loo
    print("For loop result", perms)

    print("List comprehensions", [[i, j, k] 
        for i in range(0, x+1)
        for j in range(0, y+1)
        for k in range(0, z+1)
        if i+j+k != n
        ])