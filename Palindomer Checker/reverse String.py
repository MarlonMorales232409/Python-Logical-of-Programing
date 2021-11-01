def palindomer_checker(str_val):
  if isinstance(str_val, str) == False:
    return "Error, the parameter must to be a 'String'"
  if len(str_val) < 1:
    return "You string is invalid"
  

  test = list(str_val)
  test.reverse()
  test = "".join(test)

  if(test == str_val):
    return f"Yes, we have a Palindomer here :)\n {str_val} => {test}"
  else:
    return f"No, this isn't a Palindomer :(\n {str_val} => {test}"

word = input("Enter a word to check if it is a Palindomer\n-> ")

print(palindomer_checker(word))


