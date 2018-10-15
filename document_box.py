

#user_input = int(input("Enter your marks: "))

#if user_input > 60:
#	if user_input > 90:
#		print("A+")
#	elif user_input > 80:
#		print("A")
#	else:
#		print("A-")

#marks()

#elif user_input > 60:
#	print("B+")
#	else:
#		print("B")

#elif user_input > 40:
#	if user_input >55:
#		print("C+")
#	else:
#		print("C")
	
#else:
#	print("Pass")



#ANOTHER WAY

#if user_input >70:
	
#	if user_input > 90:
	#	print("A+")

#	print("A-")
#	if user_input > 75:
#		print("A")

#-----------------------------------------------------------

import random
x = random.randint(1, 11)
guess = 0
trials = 2

print("Guess a number i am thinking of between 1 and 10")
user_input = int(input("Enter your guess: "))

while x != user_input and guess!=3:
	guess +=1
	#print(guess)
	print("you are wrong")
	user_input = int(input("Enter your guess: "))
	if guess == trials:
		print("game over!!!")
		break

if x == user_input:
	print("You are correct!!!")