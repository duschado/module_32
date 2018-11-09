#!/usr/bin/python3
lst = list()
for i in range(1500, 3001):
	if i % 7 == 0 and i % 3 != 0:
		lst.append(i)
print(lst)