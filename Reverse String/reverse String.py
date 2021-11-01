def reverse_string(str_val):
  if isinstance(str_val, str) == False:
    return "Error, the parameter must to be a 'String'"
  if len(str_val) < 1:
    return "You string is invalid"
  

  test = list(str_val)
  test.reverse()
  test = "".join(test)


  return test

print(reverse_string(""))