# This programe is to return unique username.
# Username will be conbination of email(string before @) and random string.

def username_generate(email):
    import string
    import random

    sliced_email = email.split('@')[0]
    characters = list(string.ascii_letters + string.digits)
    randstr = []
    for i in range(5):
        randstr.append(random.choice(characters))
    random.shuffle(randstr)

    username = sliced_email + "_"+ "".join(randstr)
    print("Unique username is: ", username)

if __name__ == '__main__':
    choice = input("Do you want to generate username from your email address? Yes/No : ").strip()
    if choice == 'Yes' or choice == 'YES' or choice == 'yes':
        email = input("Enter your email address: ").strip()
        username_generate(email)
    elif choice == 'No' or choice == 'NO' or choice == 'no':
        print("Thanks for comming.")
        quit()