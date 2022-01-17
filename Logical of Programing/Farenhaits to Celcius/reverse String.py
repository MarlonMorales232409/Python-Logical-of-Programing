def farenhaits_to_celcius(degree):
  return (degree - 32) * 5/9

def celcius_to_farenhaits(degree):
  return (degree * 9/5) + 32

op = int(input("1 - Farenhaits to Celcius\n2 - Celcius to Farenhaits\n-> "))

if(op == 1):
  deg = int(input("Enter the temperature in Farenhaits\n-> "))
  print(farenhaits_to_celcius(deg),"°")
elif(op == 2):
  deg = int(input("Enter the temperature in Celcius\n-> "))
  print(celcius_to_farenhaits(deg),"°")
else:
  print("Error, that option doesn't exits :(")