# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

a, b = map(int, input().split())

def divisor(n):
	for i in range(2, int(n**0.5)+1):
		if(n % i == 0): return i
	
	return n;

if a != b: 
	print(2)
else:
	print(divisor(a))
