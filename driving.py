country = input('What is your country?')
age = input('How old are you?')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You can drive!')
	else :
		print('You need to wait until 18')
elif country == 'USA' or 'America' or 'the United States of America' or 'the United States' :
	if age >= 16:
		print('You can drive!')
	else :
		print('You need to wait until 16')
else :
	print('Taiwan and USA only')