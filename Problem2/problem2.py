def evenFibSum(one, two):
	if one + two > 4000000:
		return 0
	if (one + two) % 2 == 0:
		return one + two + evenFibSum(two, one + two)
	else:
		return evenFibSum(two, one + two)

print( evenFibSum(1, 1) )
