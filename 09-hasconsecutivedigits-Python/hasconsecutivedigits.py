# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	n = abs(n)
	flag = False
	previousDigit = -1
	while n > 0:
		lastDigit = n % 10
		n = n // 10
		if lastDigit == previousDigit - 1:
			flag = True
			print(lastDigit,previousDigit)
		# return True
		# if lastDigit != previousDigit:
		#     print(lastDigit, previousDigit)
		previousDigit = lastDigit
	return flag
