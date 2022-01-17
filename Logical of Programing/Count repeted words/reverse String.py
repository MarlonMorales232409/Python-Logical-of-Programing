def count_repeat(text,str_val):
  if isinstance(text, str) == False:
    return "Error, the text must to be a 'String'"
  elif isinstance(str_val, str) == False:
    return "Error, the word to find must to be a 'String'"
  else:
    return(f"The word {str_val} was found {text.count(str_val)} times")


word = input("Enter the word you want search\n-> ")
text = input("Enter the text you want use\n-> ")

print(count_repeat(text, word))

