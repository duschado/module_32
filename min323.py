#!/usr/bin/python3
import random
N = input('Enter the number of items in the list N, N < 50\n > ')
N = int(N)
lst_N = random.sample(range(1, 50), N)
M = input('Enter the number of items in the list M, M < 50\n > ')
M = int(M)
lst_M = random.sample(range(1, 50), M)
print(lst_N)
print(lst_M)
lst_new = list()
for i in range(N):
	for j in range(M):
		if lst_N[i] == lst_M[j]:
			lst_new.append(lst_M[j])
if lst_new == []:
	print("These lists don't have generic numbers")
else:
	print(lst_new)			