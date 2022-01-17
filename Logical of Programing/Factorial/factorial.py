def factorial(num):

	if isinstance(num, int) == False:
    	return "Error, the parameter must to be a 'Integer'"
  	if num < 0:
    	return "Your number must to be greater than 0"

  	result = 1
  	for i in range(num):
    	i+=1
    	result *= i

  	return result


print(factorial(5))