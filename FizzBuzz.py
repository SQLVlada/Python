
def FizzBuzz(inp):

	FizzBuzz = []
	for i in range(1, inp + 1):
		if (i % 3 == 0) and (i % 5 == 0):
			FizzBuzz.append('FizzBuzz')
		elif i % 3 == 0:
			FizzBuzz.append('Fizz')
		elif i % 5 == 0:
			FizzBuzz.append('Buzz')
		else:
			FizzBuzz.append(i)
	return FizzBuzz

inp = int(input("Enter No to be FizzBuzzed: "))
print(FizzBuzz(inp))

