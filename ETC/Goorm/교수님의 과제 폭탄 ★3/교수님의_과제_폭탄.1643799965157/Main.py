# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def chk(date_list):
	stack = []
	for ele in date_list:
		if ele[1] > 0:
			stack.append(ele)
		else:
			val = stack.pop()
			if(val[1] != -ele[1]):
				return "No"
	
	return "Yes"
	
	

N = int(input())
start_end = []
date_list = []

for _ in range(N):
	start, end = input().split()
	
	start_val = int(start.split("/")[0])*100 + int(start.split("/")[1])
	end_val = int(end.split("/")[0])*100 + int(end.split("/")[1])
	
	start_end.append((start_val, end_val))
	
start_end = sorted(start_end, key = lambda x: (x[0], (-1)*x[1]))

idx = 1
for ele in start_end:
	date_list.append((ele[0], idx))
	date_list.append((ele[1], -idx))
	idx += 1

date_list = sorted(date_list, key=lambda x: (x[0], x[1]))
print(chk(date_list))