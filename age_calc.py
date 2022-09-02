def age_calculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    return age

if __name__ == '__main__':
    y = int(input("Enter your Birth year: "))
    m = int(input("Enter your Birth month(1-12): "))
    d = int(input("Enter your Birth date(1-31): "))
    dob = age_calculator(y,m,d)
    print("Your age is:",dob, " years")