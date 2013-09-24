pi = 3.141592653589793

def factorial(x):
	return x * factorial(x - 1) if x else 1

def sin(x):
	return sum([(-1) ** n * x ** (2 * n + 1) / factorial(2 * n + 1) for n in range(0,20)])
	
def cos(x):
	return sum([(-1) ** n * x ** (2 * n) / factorial(2 * n) for n in range(0,20)])

def tan(x):
	return sin(x) / cos(x)	

print factorial(0)
print sin(pi / 2)
print cos(pi * 2)
print tan(pi)
print factorial(80)