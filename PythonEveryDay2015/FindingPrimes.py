# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?
# http://nbviewer.ipython.org/gist/rpmuller/5920182
# Typer: Ginny C Ghezzo 
# What I learned: Python was silly to change things like range. Python is very picky about types, 

# Retur a list of prime nubmers from 2 to < n 
def primes(n):
	if n==2: return[2]
	elif n<2: return[]
	s=list(range(3, n+1, 2))					# range(start, stop, step)
	mroot = n ** 0.5
	half = (n+1)/2-1					# round down I guess 
	i = 0
	m = 3
	while m <= mroot:
		if s[i]:						# not sure, does this check if it is in range
			j=int((m*m-3)/2)
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

num = input("What numer do you want to check?")
print(primes(int(num)))