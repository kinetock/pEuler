x = 600851475143
i = 3

while x != i :
	if x % i == 0:
		x /= i
	else:
		i += 1 
print(i)