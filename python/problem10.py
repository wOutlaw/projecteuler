'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def is_prime(n):
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
			
	return True

def prime_sum(n):
	prime = 1
	primes = []
	
	while prime < n:
		prime += 1
		if is_prime(prime):
			primes.append(prime)
	return sum(primes)
	
if __name__ = "__main__":
	print(prime_sum(2000000))