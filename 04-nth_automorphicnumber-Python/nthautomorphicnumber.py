# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def Automorphic(n):
	x=n
	a=n**2
	total=0
	while(x>0):
		x=x//10
		total=total+1
		if(x==0):
			break
	b=a%(10**total)
	if(b==n):
		return b
	return False
	return -1
def nthAutomorphicNumber(n):
	total=2
	i=1
	while(total<=n):
		if (Automorphic(i)):
			total=total+1
		i=i+1
	return i-1

print(nthAutomorphicNumber(int(input())))