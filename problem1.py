i = 0
sum = 0
cap = 1000

while i < cap:
	if i % 3 == 0 or i % 5 == 0:
		sum = sum + i
		i = i + 1
	else:
		i = i + 1

print(sum)