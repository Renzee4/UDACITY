#this project was created by: Renzee Sto Tomas

sample = '''A word with 3 letters to describe a motorized vheicle is ___1___'''

print sample

sampleList = sample.split(" ")
newList = []


##this code loops if it does not have the correct answer
#		PROBLMEs::: the amount of attempts a user gets will not terminate when attempts > 1. 
#					it's an infinite loop until the user answers witht he correct input "car" 

def play():
	attempts = int(input('How many tries?: '))
	userinput = raw_input('Answer to ___1___: ')
	for words in sampleList:
		if words == "___1___":
			userinput == "car"
			while attempts > 1:
				while userinput != 'car':
					attempts -= 1
					print "attempts remaining", attempts
					userinput = raw_input('Try again: ')
				break
			newList.append(userinput)
		else:
			newList.append(words)
		joinedList = ' '.join(newList)
	print ' '
	print "CORRECT!"
	print joinedList


play()
