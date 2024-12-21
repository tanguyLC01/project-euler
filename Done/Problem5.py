""" Problem 5 Of Project Euler """
import os
def ppcm(*args):
	def _pgcd(a,b):
		while b:
			a, b = b, a%b
		return a
	p = abs(args[0] * args[1]) // _pgcd(args[0], args[1])
	for x in args[2:]:
		p = abs(p * x)// _pgcd(p,x)
	return p

	
print(ppcm(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
os.system("Pause")