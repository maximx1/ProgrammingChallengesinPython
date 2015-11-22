import random

print ('___________________________')
print ('__ROCK - PAPER - SCISSORS__')
print ('___________________________\n')

print('Type in rock, paper or scissors \n')
print('you will fight against the computer\n')

isRunning = True
options = ['rock','paper','scissors']


while isRunning :
	op = input('Your option: ')
	print ('color a')
	randomchoice = random.choice(options)
	if op == options[0]:
		if op == randomchoice:
			print ('the Computer choice is: ', randomchoice)
			print ('TIE! you both chose Rock')
		elif randomchoice == options[1]:
			print ('the Computer choice is: ', randomchoice)
			print ('You lost to the power of paper!')
		elif randomchoice == options[2]:
			print ('the Computer choice is: ', randomchoice)
			print ('You won over that stupid scissors!')
		else:
			print('invalid choice!\n\n')			
	elif op == options[1]:		
		if op == randomchoice:
			print ('the Computer choice is: ', randomchoice)
			print ('TIE! you both chose Paper')
		elif randomchoice == options[0]:
			print ('the Computer choice is: ', randomchoice)
			print ('You Won Over that stupid rock! yeah!')
		elif randomchoice == options[2]:
			print ('the Computer choice is: ', randomchoice)
			print ('You lost to that sharp scissors')
		else:
			print('invalid choice!\n\n')
	elif op == options[2]:		
		if op == randomchoice:
			print ('the Computer choice is: ', randomchoice)
			print ('TIE! you both chose Scissors')
		elif randomchoice == options[0]:
			print ('the Computer choice is: ', randomchoice)
			print ('You Lost to the scissor power!')
		elif randomchoice == options[1]:
			print ('the Computer choice is: ', randomchoice)
			print ('You Won over that flat paper! hurray!')
		else:
			print('invalid choice!\n\n')
	else:
		print ('invalid option - Please Try again')	
	print('\n Would you like to Try again ? y/n')
	tr = input('y or n: ')
	if tr == 's':
		pass
	elif tr =='n':
		print ('------------ program terminated -------------------')
		break
