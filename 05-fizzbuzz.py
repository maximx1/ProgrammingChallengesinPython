#author - Pedro Nogueira - @pedronogueira

print ('______________________________________')
print ('____ THE FIZZBUZZ SEQUENCE ___________')
print ('______________________________________')

for num in range(1, 101): print("FIZZ" * (num % 3 == 0) + "BUZZ" * (num % 5 == 0) or num)
