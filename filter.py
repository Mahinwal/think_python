if __name__ == '__main__':
    items = []
    for i in range(1, int(input("Enter the size of list: ")) + 1):
        items.append(int(input("Enter item "+ str(i)+": ")))
    # Filter the even numbers
    filter_even = list(filter(lambda x: (x%2 == 0), items))
    # Filter the odd numbers
    filter_odd = list(filter(lambda x: (x%2 != 0), items))
    # print even number list
    print("Filter out list of even numbers :", filter_even)
    # Print odd numbers list
    print("Filter out list of odd numbers :", filter_odd)
