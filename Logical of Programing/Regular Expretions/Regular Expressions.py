import re

def check_name(name):

  if(name.isnumeric()):
    return "A number is not a name"
  
  name_result = re.search(r"[A-Za-z]+", name)
  if(name != name_result.group()):
    return f"The name {name} is invalid :("
  else:
    return "Success :), your name was validated"


user_name = input("Let's go to validate your name\nEnter your name -> ")

print(check_name(user_name))