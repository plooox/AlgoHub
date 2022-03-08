vowel = {'a','e','i','o','u','A','E','I','O','U'}

N = int(input())
for _ in range(N):
	string = input()
	only_vowel = [s for s in string if s in vowel]
	if len(only_vowel) != 0:
		print(''.join(only_vowel))
	else:
		print('???')