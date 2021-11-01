def check_pair_or_odd(num):
  result = num % 2
  if(result == 0):
    return f"The number {num} is pair"
  else:
    return f"The number {num} is odd"



try:
  number = int(input("Enter a number to check if is pair or odd\n-> "))
  print(check_pair_or_odd(number))
except:
  print("Come on dude, you don't kown what a number is :(")


