input_string = input()

s = "00"+input_string+"00"

def BF_SEARCH(s):
	if "12" in s:
		idx = s.find("12")
		sub_s1 = s[idx+2:]
		sub_s2 = s[:idx]
		if "21" in sub_s1 or "21" in sub_s2:
			return "Yes"

	if "21" in s:
		idx = s.find("21")
		sub_s1 = s[idx+2:]
		sub_s2 = s[:idx]
		if "12" in sub_s1 or "12" in sub_s2:
			return "Yes"

	return "No"



	
print(BF_SEARCH(s))