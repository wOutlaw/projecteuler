'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def findit(min, max):
	span = list(range(min, max))

	for i in range(max, 999999999, max):
		if all(i % n == 0 for n in span):
			print(i)
			break

if __name__ == "__main__":
	findit(1, 20)