# UDACITY STAGE 2 PROJECT by RENZEE STO TOMAS


# different levels of quizzes: 
easyQuiz = "Pokemon are caught by using ___1___. When throwing ___1___, there is a chance that the pokemon will break free! You can visit the ___2___ to heal your pokemon or use ___3___ to restore health. You can also visit the ___4___ to purchase goods such as ___1___ and ___3___, usually located near a ___2___. Some ___1___ are better than others and can usually be purchased at a ___4___ or even found!."
mediumQuiz = "Pikachu is an ___1___ type pokemon. If you give a Pikachu a thunderstone it evolves into a ___2___! A ___2___ is generally faster and stronger than Pikachu. Both pokemon are ___1___ which makes them weak to ___3___ type moves. But their ___1___ type moves are strong against water and ___4___ type pokemon. If a pokemon is both water and ___4___, it is 4x weaker to ___1___ moves!"
hardQuiz = "Pokemon that are ___1___ type are weak to poison and steel type moves. However, ___1___ types are immune to ___2___ type moves. The mega evolution of ___3___ is the only ___2___ pokemon that is immune to other ___2___ type moves because it is also part ___1___. ___3___'s ability ___4___ turns its normal type moves to ___1___ type moves with 1.5x more damage! ___4___ also makes it a B.A.S.E move that gives it another 1.5x bonus damage."

#	QUIZ ANSWERS
#	easy Quiz: 1 = pokeballs, 2 = pokecenter, 3 = potions, 4 = pokemart
#	medium Quiz: 1 = electric, 2 = Raichu, 3 = ground, 4 = flying
#	hard Quiz: 1 = fairy, 2 = dragon, 3 = altaria, 4 = pixilate

easyAnswers = [['___1___', 'pokeballs'],
				['___2___', 'pokecenter'],
				['___3___', 'potions'],
				['___4___', 'pokemart']]

mediumAnswers = [['___1___', 'electric'],
				['___2___', 'Raichu'],
				['___3___', 'ground'],
				['___4___', 'flying']]

hardAnswers = [['___1___', 'fairy'],
				['___2___', 'dragon'],
				['___3___', 'Altaria'],
				['___4___', 'pixilate']]



# 			--- procedures for fourth question ---
def fourthBlank(answers, quizstring):
	quizstring = quizstring.split()
	replaced = []
	for word in quizstring:
		if answers[3][0] in word:
			word = word.replace(answers[3][0], answers[3][1])
			replaced.append(word)
		else:
			replaced.append(word)
	answerString = ' '.join(replaced)
	print answerString
def fourthAnswer(answers, answerString):
	answer = raw_input('Answer to ' + answers[3][0] + ': ').lower()
	attempts = 3
	while attempts > 1 and answer != answers[3][1].lower():
		attempts -= 1
		print 'attempts remaining', attempts
		answer = raw_input('Try again: ').lower()
	if answer == answers [3][1].lower():
		return fourthBlank(answers, answerString)


#				---- procedures for third question --- 
def thirdBlank(answers, quizstring):
	quizstring = quizstring.split()
	replaced = []
	for word in quizstring:
		if answers[2][0] in word:
			word = word.replace(answers[2][0], answers[2][1])
			replaced.append(word)
		else:
			replaced.append(word)
	answerString = ' '.join(replaced)
	print answerString
	return fourthAnswer(answers, answerString)
def thirdAnswer(answers, answerString):
	answer = raw_input('Answer to ' + answers[2][0] + ': ').lower()
	attempts = 3
	while attempts > 1 and answer != answers[2][1].lower():
		attempts -= 1
		print 'attempts remaining', attempts
		answer = raw_input('Try again: ').lower().lower()
	if answer == answers[2][1].lower():
		return thirdBlank(answers, answerString)


#  			---- procedures for 2nd question  --- 	
def secondBlank(answers, quizstring):
	quizstring = quizstring.split()
	replaced = []
	for word in quizstring:
		if answers[1][0] in word:
			word = word.replace(answers[1][0], answers[1][1])
			replaced.append(word)
		else:
			replaced.append(word)
	answerString = ' '.join(replaced)
	print answerString
	return thirdAnswer(answers, answerString)

def secondAnswer(answers, answerString):
	answer = raw_input('Answer to ' + answers[1][0] + ': ').lower()
	attempts = 3
	while attempts > 1 and answer != answers[1][1].lower(): 
		attempts -= 1
		print 'attempts remaining' , attempts
		answer = raw_input('Try again: ').lower()
	if answer == answers[1][1].lower():
		return secondBlank(answers, answerString)



#				---- procedures for first question ----
#this procedure replaces empty blanks for the correct answer
def firstBlank(answers, quizstring):
	quizstring = quizstring.split()
	replaced = []
	for word in quizstring:
		if answers[0][0] in word:
			word = word.replace(answers[0][0], answers[0][1])
			replaced.append(word)
		else:
			replaced.append(word)
	answerString = ' '.join(replaced)
	print answerString
	return secondAnswer(answers, answerString)

#this procedures checks to see if the user answers the first blank correct
#if correct, it calls the next function to take the quiz and replace the blank with the answer
#if incorrect, the user has 3 attempts to try again. 	
def firstAnswer(answers, answerString):
	print answerString
	answer = raw_input('Answer to ' + answers[0][0] + ': ').lower()
	attempts = 3
	while attempts > 1 and answer != answers[0][1].lower():
		attempts -= 1
		print 'attempts remaining', attempts
		answer = raw_input('Try again: ').lower()
	if answer == answers[0][1].lower():
		return firstBlank(answers, answerString)

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

pickALevel = raw_input('Pick a level (easy/medium/hard): ').lower()
if pickALevel == 'easy':
	print firstAnswer(easyAnswers, easyQuiz)
	print ' '
elif pickALevel == 'medium':
	print firstAnswer(mediumAnswers, mediumQuiz)
	print ' '
elif pickALevel == 'hard':
	print firstAnswer(hardAnswers, hardQuiz)