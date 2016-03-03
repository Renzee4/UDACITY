# UDACITY STAGE 2 PROJECT by RENZEE STO TOMAS
#python

# strings to load different levels of quizzes
easyQuiz = "Pokemon are caught by using ___1___. When throwing ___1___, there is a chance that the pokemon will break free! You can visit the ___2___ to heal your pokemon or use ___3___ to restore health. You can also visit the ___4___ to purchase goods such as ___1___ and ___3___, usually located near a ___2___. Some ___1___ are better than others and can usually be purchased at a ___4___ or even found!."
mediumQuiz = "Pikachu is an ___1___ type pokemon. If you give a Pikachu a thunderstone it evolves into a ___2___! A ___2___ is generally faster and stronger than Pikachu. Both pokemon are ___1___ which makes them weak to ___3___ type moves. But their ___1___ type moves are strong against water and ___4___ type pokemon. If a pokemon is both water and ___4___, it is 4x weaker to ___1___ moves!"
hardQuiz = "Pokemon that are ___1___ type are weak to poison and steel type moves. However, ___1___ types are immune to ___2___ type moves. The mega evolution of ___3___ is the only ___2___ pokemon that is immune to other ___2___ type moves because it is also part ___1___. ___3___'s ability ___4___ turns its normal type moves to ___1___ type moves with 1.5x more damage! ___4___ also makes it a B.A.S.E move that gives it another 1.5x bonus damage."

#	QUIZ ANSWERS
#	easy Quiz: 1 = pokeballs, 2 = pokecenter, 3 = potions, 4 = pokemart
#	medium Quiz: 1 = electric, 2 = Raichu, 3 = ground, 4 = flying
#	hard Quiz: 1 = fairy, 2 = dragon, 3 = altaria, 4 = pixilate


##### EASY QUIZ PROCEDURES #####
#easyQuiz blank1 procedures::
def easy1(easyQuiz): # first procedure to replace blank1 with the correct answer. easyQuiz string is an input to replace and return a newly revised blank1 filled string.
	easyQuiz_Blank1 = easyQuiz.split()
	replaced = []
	blank1 = '___1___'
	for word in easyQuiz_Blank1:
		if blank1 == '___1___':
			word = word.replace(blank1, 'pokeballs')
			replaced.append(word)
		else:
			replaced.append(word)
	easyQuiz_solvedForBlank1 = ' '.join(replaced)
	return easyQuiz_solvedForBlank1

def easyAnswer1():
	print easyQuiz
	answer = raw_input('Answer to ___1___: ')
	attempts = 3
	while attempts > 1 and answer != 'pokeballs': #loops until the user gets the answer correct, if not the game ends
		attempts -= 1
		print 'attempts remaining', attempts
		answer = raw_input('Try again: ')
	if answer == 'pokeballs':
		print easy1(easyQuiz) 
		return True #required to return True, if True the game continues to ask the user to answer the next question. 
	else:
		return #returns to end the procedure, thus ends the game if the user doesn't get the right answer

#easyQuiz blank2 procedures::
def easy2():
	easyQuiz_Blank2 = easy1(easyQuiz)
	easyQuiz_Blank2 = easyQuiz_Blank2.split()
	replaced = []
	blank2 = '___2___'
	for word in easyQuiz_Blank2:
		if blank2 == '___2___':
			word = word.replace(blank2, 'pokecenter')
			replaced.append(word)
		else:
			replaced.append(word)
	easyQuiz_solvedforBlank2 = ' '.join(replaced)
	return easyQuiz_solvedforBlank2

def easyAnswer2():
	answer = raw_input('Answer to ___2___: ')
	attempts = 3
	while attempts > 1 and answer != 'pokecenter': #loops until the user gets the answer correct, if not the game ends
		attempts -= 1
		print 'attempts remaining', attempts
		answer = raw_input('Try again: ')
	if answer == 'pokecenter':
		print easy2()
		return True #required to return True, if True the game continues to ask the user to answer the next question. 
	else:
		return #returns to end the procedure, thus ends the game if the user doesn't get the right answer

#easyQuiz blank3 procedures:: 
def easy3():
	easyQuiz_Blank3 = easy2()
	easyQuiz_Blank3 = easyQuiz_Blank3.split()
	replaced = []
	blank3 = '___3___'
	for word in easyQuiz_Blank3:
		if blank3 == '___3___':
			word = word.replace(blank3, 'potions')
			replaced.append(word)
		else:
			replaced.append(word)
	easyQuiz_solvedforBlank3 = ' '.join(replaced)
	return easyQuiz_solvedforBlank3

def easyAnswer3():
	answer = raw_input('Answer to ___3___: ')
	attempts = 3
	while attempts > 1 and answer != 'potions': #loops until the user gets the answer correct, if not the game ends
		attempts -= 1
		print 'attempts remaining', attempts
		answer = raw_input('Try again: ')
	if answer == 'potions':
		print easy3()
		return True #required to return True, if True the game continues to ask the user to answer the next question. 
	else:
		return #returns to end the procedure, thus ends the game if the user doesn't get the right answer

#easyQuiz blank4 procedures::
def easy4():
	easyQuiz_Blank4 = easy3()
	easyQuiz_Blank4 = easyQuiz_Blank4.split()
	replaced = []
	blank4 = '___4___'
	for word in easyQuiz_Blank4:
		if blank4 == '___4___':
			word = word.replace(blank4, 'pokemart')
			replaced.append(word)
		else:
			replaced.append(word)
	easyQuiz_solvedforBlank4 = ' '.join(replaced)
	return easyQuiz_solvedforBlank4

def easyAnswer4():
	answer = raw_input('Answer to ___4___: ')
	attempts = 3
	while attempts > 1 and answer != 'pokemart': #loops until the user gets the answer correct, if not the game ends
		attempts -= 1
		print 'attempts remaining', attempts
		answer = raw_input('Try again: ')
	if answer == 'pokemart':
		print easy4()
		return True #required to return True, if True the game continues to ask the user to answer the next question. 
	else:
		return #returns to end the procedure, thus ends the game if the user doesn't get the right answer

##### MEDIUM QUIZ PROCEDURES #####
 #mediumQuiz blank1 procedures:: 
def medium1(mediumQuiz): # first procedure to replace blank1 with the correct answer. mediumQuiz string is an input to replace and return a newly revised blank1 filled string.
	mediumQuiz_Blank1 = mediumQuiz.split()
	replaced = []
	blank1 = '___1___'
	for word in mediumQuiz_Blank1:
		if blank1 == '___1___':
			word = word.replace(blank1, 'electric')
			replaced.append(word)
		else:
			replaced.append(word)
	mediumQuiz_Blank1 = ' '.join(replaced)
	return mediumQuiz_Blank1

def mediumAnswer1():
	print mediumQuiz
	answer = raw_input('Answer to ___1___')
	attempts = 3
	while attempts > 1 and answer != 'electric': #loops until the user gets the answer correct, if not the game ends
		attempts -= 1
		print 'attempts remaining', attempts
		answer = raw_input('Try again: ')
	if answer == 'electric':
		print medium1(mediumQuiz)
		return True #required to return True, if True the game continues to ask the user to answer the next question. 
	else:
		return #returns to end the procedure, thus ends the game if the user doesn't get the right answer

#mediumQuiz blank2 procedures::
def medium2():
	mediumQuiz_Blank2 = medium1(mediumQuiz)
	mediumQuiz_Blank2 = mediumQuiz_Blank2.split()
	replaced = []
	blank2 = '___2___'
	for word in mediumQuiz_Blank2:
		if blank2 == '___2___':
			word = word.replace(blank2, 'Raichu')
			replaced.append(word)
		else:
			replaced.append(word)
	mediumQuiz_Blank2 = ' '.join(replaced)
	return mediumQuiz_Blank2

def mediumAnswer2():
	answer = raw_input('Answer to ___2___: ')
	attempts = 3
	while attempts > 1 and answer != 'Raichu': #loops until the user gets the answer correct, if not the game ends
		attempts -= 1
		print 'attempts remaining', attempts
		answer = raw_input('Try again: ')
	if answer == 'Raichu':
		print medium2()
		return True #required to return True, if True the game continues to ask the user to answer the next question. 
	else:
		return #returns to end the procedure, thus ends the game if the user doesn't get the right answer

#mediumQuiz blank3 procedures::
def medium3():
	mediumQuiz_Blank3 = medium2()
	mediumQuiz_Blank3 = mediumQuiz_Blank3.split()
	replaced= []
	blank3 = '___3___'
	for word in mediumQuiz_Blank3:
		if blank3 == '___3___':
			word = word.replace(blank3, 'ground')
			replaced.append(word)
		else:
			replaced.append(word)
	mediumQuiz_Blank3 = ' '.join(replaced)
	return mediumQuiz_Blank3

def mediumAnswer3():
	answer = raw_input('Answer to ___3___: ')
	attempts = 3
	while attempts > 1 and answer != 'ground': #loops until the user gets the answer correct, if not the game ends
		attempts -= 1
		print 'attempts remaining', attempts
		answer = raw_input('Try again: ')
	if answer == 'ground':
		print medium3()
		return True #required to return True, if True the game continues to ask the user to answer the next question. 
	else:
		return #returns to end the procedure, thus ends the game if the user doesn't get the right answer

#mediumQuiz blank4 procedures::
def medium4():
	mediumQuiz_Blank4 = medium3()
	mediumQuiz_Blank4 = mediumQuiz_Blank4.split()
	replaced = []
	blank4 = '___4___'
	for word in mediumQuiz_Blank4:
		if blank4 == '___4___':
			word = word.replace(blank4, 'flying')
			replaced.append(word)
		else:
			replaced.append(word)
	mediumQuiz_Blank4 = ' '.join(replaced)
	return mediumQuiz_Blank4

def mediumAnswer4():
	answer = raw_input('Answer to ___4___: ')
	attempts = 3
	while attempts > 1 and answer != 'flying': #loops until the user gets the answer correct, if not the game ends
		attempts -= 1
		print 'attempts remaining', attempts
		answer = raw_input('Try again: ')
	if answer == 'flying':
		print medium4()
		return True #required to return True, if True the game continues to ask the user to answer the next question. 
	else:
		return #returns to end the procedure, thus ends the game if the user doesn't get the right answer

##### HARD QUIZ PROCEDURES #####
#hardQuiz blank1 procedures::
def hard1(hardQuiz): # first procedure to replace blank1 with the correct answer. hardQuiz string is an input to replace and return a newly revised blank1 filled string.
	hardQuiz_Blank1 = hardQuiz.split()
	replaced = []
	blank1 = '___1___'
	for word in hardQuiz_Blank1:
		if blank1 == '___1___':
			word = word.replace(blank1, 'fairy')
			replaced.append(word)
		else:
			replaced.append(word)
	hardQuiz_Blank1 = ' '.join(replaced)
	return hardQuiz_Blank1

def hardAnswer1():
	print hardQuiz
	answer = raw_input('Answer to ___1___')
	attempts = 3
	while attempts > 1 and answer != 'fairy': #loops until the user gets the answer correct, if not the game ends
		attempts -= 1
		print 'attempts remaining', attempts
		answer = raw_input('Try again: ')
	if answer == 'fairy':
		print hard1(hardQuiz)
		return True #required to return True, if True the game continues to ask the user to answer the next question. 
	else:
		return #returns to end the procedure, thus ends the game if the user doesn't get the right answer

#hardQuiz blank2 procedures::
def hard2():
	hardQuiz_Blank2 = hard1(hardQuiz)
	hardQuiz_Blank2 = hardQuiz_Blank2.split()
	replaced = []
	blank2 = '___2___'
	for word in hardQuiz_Blank2:
		if blank2 == '___2___':
			word = word.replace(blank2, 'dragon')
			replaced.append(word)
		else:
			replaced.append(word)
	hardQuiz_Blank2 = ' '.join(replaced)
	return hardQuiz_Blank2

def hardAnswer2():
	answer = raw_input('Answer to ___2___: ')
	attempts = 3
	while attempts > 1 and answer != 'dragon': #loops until the user gets the answer correct, if not the game ends
		attempts -= 1
		print 'attempts remaining', attempts
		answer = raw_input('Try again: ')
	if answer == 'dragon':
		print hard2()
		return True #required to return True, if True the game continues to ask the user to answer the next question. 
	else:
		return #returns to end the procedure, thus ends the game if the user doesn't get the right answer

#hardQuiz blank3 procedures::
def hard3():
	hardQuiz_Blank3 = hard2()
	hardQuiz_Blank3 = hardQuiz_Blank3.split()
	replaced = []
	blank3 = '___3___'
	for word in hardQuiz_Blank3:
		if blank3 == '___3___':
			word = word.replace(blank3, 'altaria')
			replaced.append(word)
		else:
			replaced.append(word)
	hardQuiz_Blank3 = ' '.join(replaced)
	return hardQuiz_Blank3

def hardAnswer3():
	answer = raw_input('Answer to ___3___: ')
	attempts = 3
	while attempts > 1 and answer != 'altaria': #loops until the user gets the answer correct, if not the game ends
		attempts -= 1
		print ' attempts remaining', attempts
		answer = raw_input('Try again: ')
	if answer == 'altaria':
		print hard3()
		return True #required to return True, if True the game continues to ask the user to answer the next question. 
	else:
		return #returns to end the procedure, thus ends the game if the user doesn't get the right answer

#hardQuiz blank4 procedures::
def hard4():
	hardQuiz_Blank4 = hard3()
	hardQuiz_Blank4 = hardQuiz_Blank4.split()
	replaced = []
	blank4 = '___4___'
	for word in hardQuiz_Blank4:
		if blank4 == '___4___':
			word = word.replace(blank4, 'pixilate')
			replaced.append(word)
		else:
			replaced.append(word)
	hardQuiz_Blank4 = ' '.join(replaced)
	return hardQuiz_Blank4

def hardAnswer4():
	answer = raw_input('Answer to ___4___: ')
	attempts = 3
	while attempts > 1 and answer != 'pixilate': #loops until the user gets the answer correct, if not the game ends
		attempts -= 1
		print ' attempts remaining', attempts
		answer = raw_input('Try again: ')
	if answer == 'pixilate':
		print hard4()
		return True #required to return True, if True the game continues to ask the user to answer the next question. 
	else:
		return #returns to end the procedure, thus ends the game if the user doesn't get the right answer



#### If a user picks a level, it will execute one of these functions. As long as the first function remains True, the user will be prompted to answer the next question until fail, or finish 'game over' 
def user_picks_easy():
	if easyAnswer1() == True:
		if easyAnswer2() == True:
			if easyAnswer3() == True:
				easyAnswer4()
				print 'GAME OVER!'

def user_picks_medium():
	if mediumAnswer1() == True:
		if mediumAnswer2() == True:
			if mediumAnswer3() == True:
				mediumAnswer4()
				print 'GAME OVER'

def user_picks_hard():
	if hardAnswer1() == True:
		if hardAnswer2() == True:
			if hardAnswer3() == True:
				hardAnswer4()
				print 'GAME OVER!'


###### Function to ask the user which level they would like to play
def pick_a_level():
	userLevel = raw_input('Pick a level (easy/medium/hard): ').lower()
	if userLevel == 'easy':
		user_picks_easy()
	if userLevel == 'medium':
		user_picks_medium()
	if userLevel == 'hard':
		user_picks_hard()


##### silly title.... 
def intro():
	print ' '
	print 'WELCOME TO....'
	print '''                      
								                         
	                              .;:**'                       
	                              `                              
	  .:XHHHHk.              db.   .;;.     dH  MX              
	oMMMMMMMMMMM       ~MM  dMMP :MMMMMR   MMM  MR      ~MRMN     
	QMMMMMb  "MMX       MMMMMMP !MX' :M~   MMM MMM  .oo. XMMM 'MMM
	  `MMMM.  )M> :X!Hk. MMMM   XMM.o"  .  MMMMMMM X?XMMM MMM>!MMP
	   'MMMb.dM! XM M'?M MMMMMX.`MMMMMMMM~ MM MMM XM `" MX MMXXMM 
	    ~MMMMM~ XMM. .XM XM`"MMMb.~*?**~ .MMX M t MMbooMM XMMMMMP 
	     ?MMM>  YMMMMMM! MM   `?MMRb.    `"""   !L"MMMMM XM IMMM  
	      MMMX   "MMMM"  MM       ~%:           !Mh.""" dMI IMMP  
	      'MMM.                                             IMX   
	       ~M!M                                             IMP   
	                                                             '''
 	print 'QUIZ!!! LETS PLAY!!!!'
 	pick_a_level()

intro()
