#!/usr/bin/python3
import random
n = input('Enter the number of items in the list\n > ')
n = int(n)
lst_N = random.sample(range(1, 101), n)
print(lst_N)
for i in range(1, n):
	j = i - 1
	while j >= 0 and lst_N[j] > lst_N[j+1]:
		lst_N[j], lst_N[j+1] = lst_N[j+1], lst_N[j]
		j -= 1
print(lst_N)