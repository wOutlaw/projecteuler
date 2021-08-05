'''
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def difference(min, max):
	nums = list(range(min, max + 1))
	sum_square = 0
	square_sum = 0
	
	for n in nums:
		sum_square += n**2
		
	for n in nums:
		square_sum += n
	
	square_sum = square_sum**2
	
	return square_sum - sum_square

if __name__ = "__main__":
	print(difference(1, 100))