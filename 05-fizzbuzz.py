#author - Pedro Nogueira - @pedronogueira

print ('______________________________________')
print ('____ THE FIZZBUZZ SEQUENCE ___________')
print ('______________________________________')

num = 0
for num in range(100):
	if num % 15 == 0:
		print ('FIZZBUZZ')
	elif num % 3 == 0:
		print ('FIZZ')
	elif num % 5 == 0:
		print ('BUZZ')
	else:
		print (num)			