country = input('What is your country?')
age = input('How old are you?')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You can drive!')
	else :
		print('You need to wait until 18')
elif country == 'USA':
	if age >= 16:
		print('You can drive!')
	else :
		print('You need to wait until 16')