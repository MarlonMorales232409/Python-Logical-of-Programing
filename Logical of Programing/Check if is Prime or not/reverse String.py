def isPrime(num):
  cont = 2
  for i  in range(num):
    result =  num % cont
    cont+=1 
    print(f"This is num {num}\nThis is cont {cont}\nThis is result {result}")

    if result == 0 and num != cont:
      return f"The number {num} isn't prime"
    else:
      return f"The number {num} is prime"



try:
  number = int(input("Enter a number to check if is pair or odd\n-> "))
  print(isPrime(number))
except:
  print("Come on dude, you don't kown what a number is :(")

