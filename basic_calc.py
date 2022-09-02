def addition(a, b):
    add = a + b
    print(str(a) + " + " + str(b) + " = " + str(add), "\n")

def subtraction(a, b):
    sub = a - b 
    print(str(a) + " - " + str(b) + " = " + str(sub), "\n")

def multiplication(a, b):
    mul = a * b 
    print(str(a) + " * " + str(b) + " = " + str(mul), "\n")

def division(a, b):
    div = a // b 
    print(str(a) + " // " + str(b) + " = " + str(div), "\n")

while True:
    if __name__ == '__main__':
        print("A. Addition")
        print("B. Substraction")
        print("C. Multiplication")
        print("D. Division")
        print("E. Chose any key to exit or quit the program.\n")

        choice = input("Enter your choice : ")

        if choice == "a" or choice == "A":
            print("Addition")
            a = int(input("Enter first number : "))
            b = int(input("Enter second number : "))
            addition(a,b)
        elif choice == "b" or choice == "B":
            print("Substraction")
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            subtraction(a, b)
        elif choice == "c" or choice == "C":
            print("Multiplication")
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            multiplication(a, b)
        elif choice == "d" or choice == "D":
            print("Division")
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            division(a, b)
        else:
            print("Programe has been terminated, thank you!")
            quit()
