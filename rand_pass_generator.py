def generate_random_password(lenght):
    import string
    import random 

    characters_list = list(string.ascii_letters + string.digits + string.punctuation)
    password = []
    for i in range(0, lenght):
        password.append(random.choice(characters_list))

    random.shuffle(password)
    print("Your password is :", "".join(password))

if __name__ == '__main__':
    choice = input("Do you wnt to generate the password? Yes/No: ")

    if choice == 'Yes' or choice == 'YES' or choice == 'yes':
        pass_length = int(input("Enter the password length: "))
        generate_random_password(pass_length)
    elif choice == 'No' or choice == 'NO' or choice == 'no':
        print("Programe has been terminated, thanks for coming.")
        quit()