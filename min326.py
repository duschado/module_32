#!/usr/bin/python3
import random
n = input('Enter the number of items in the list\n > ')
n = int(n)
N = random.sample(range(1, 101), n)
print(N)
for i in range(n-1):
	sw = 0
	for j in range(n-1-i):
		if N[j] % 2 > N[j+1] % 2: 
			N[j], N[j+1] = N[j+1], N[j]
			sw = 1					
	if sw == 0:		
		break
for i in range(n-1):
	sw = 0
	for j in range(n-1-i):
		if N[j] > N[j+1] and N[j] % 2 == N[j+1] % 2: 
			N[j], N[j+1] = N[j+1], N[j]
			sw = 1					
	if sw == 0:		
		break	
print(N)