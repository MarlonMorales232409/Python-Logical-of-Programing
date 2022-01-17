def clean_string(string, pattern):

    return string.replace(pattern, "")


try:
    user_pattern = input("Enter the pattern that you want to delete\n-> ")
    user_string = input("Enter the string that you want to clean\n-> ")
    print(clean_string(user_string, user_pattern))
except:
    print("Be sure to pass the correct parameters")
