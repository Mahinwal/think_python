if __name__ == '__main__':
    input_str = input("Enter any string: ")
    # title method
    print("title()", input_str.title())

    # upper()
    print("upper()", input_str.upper())

    # lower()
    print("lower()", input_str.lower())

    # Concate strings
    print("concate strings:", input_str.upper() + " " +input_str.lower())

    # Adding Whitespace to Strings with Tabs or Newlines
    print("\t",input_str)
    print("\n",input_str)

    # Stripping Whitespace
    print(input_str.strip())
    print(input_str.lstrip())
    print(input_str.rstrip())

    # swapcase
    print("swapcasse()", input_str.swapcase())

    # Python String capitalize()
    print("capitalize()", input_str.capitalize())

    # Example 2: capitalize() Doesn't Change the Original String
    print("String before capitalize:", input_str)
    print("String capitalize:", input_str.capitalize())
    print("String after capitalize:", input_str)

    # count(): This method returns the number of occrance of substring in the given string.
    # sytax: string.count(substring, start, end)
    print("count()",input_str.count('l', 3))

    # Python String find()
    # Find() method will return the index of the first occurrence of the sub string if found, else it will return -1.

    print(input_str.find("l"))

    # Python String index()
    # index() method returns the index of the first occurrence of substring if found else it will raise an exception.

    print(input_str.index("l"))

    # isalnum(): This will return True if string is alphanumeric else return false.
    # isalpha(): This method will return True if all the chars are alphabets else it will return False.
    # isdecimal(): Return True if all chars are decimal else return False.
    # isdigit(): Returns True if all chars are digit else return False.
    # islower(): Returns True if all chars are in lowercase else retrun False.
    # isupper(): returns True if all chars are in upper case else return False.
    # isnumeric(): Return True if all chars are numeric else return False.
    # istitle(): Return True if string is in title case else return False.

    # split(): String to list conversion.
    print(input_str.split())

    # join(): The join string method return a string by joining all elements of a iterale such list, tuple, string.
    # join elements of text with comma
    print(",".join(input_str))
