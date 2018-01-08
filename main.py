import sys
import string
import quantumrandom


i=0
rand_word = []
new_word = ""
counter = 0
probability = 144**27
success_count = 0
sentence = "quels que soient les progres des connaissances humaines, il y aura toujours place pour l'ignorance et par suite pour le hasard et la probabilite"
# "whatever the progress of human knowledge, there will always be room for ignorance, hence for chance and probability"
# Emile Borel (1914). Le hasard. Librairie Felix Alcan. p. 12-13

letters = ''.join(string.ascii_lowercase)
print("Predicting with a random engine based on quantum processes:")
print('"%s"' %(sentence))
print(" ")
print('(whatever the progress of human knowledge, there will always be room for ignorance, hence for chance and probability)')
print ("Emile Borel (1914). Le hasard. Librairie Felix Alcan. p. 12-13")
print(" ")
print("probability for the whole sentence is 1:%i" %(probability))
print(" ")

# generate quote randomly using quantum processes
while new_word is not sentence:
	success_count = 0
	rand_word = []
	counter = counter + 1
	#print("%i attempts to randomly generate" %counter)
	#print("'" + sentence + "'")
	for i in range(len(sentence)):
		rand = quantumrandom.randint(0, 28)
		if rand <= 25:
			rand_word = rand_word + [letters[round(rand)]]
		elif 25 < rand <= 26:
			rand_word = rand_word + [","]
		elif 26 < rand <= 27:
			rand_word = rand_word + ["'"]
		elif 27 < rand <= 28:
			rand_word = rand_word + [" "]
		# if rand == 27:
		# 	rand_word = rand_word + [","]
		#print ('')
		if rand_word[i] is sentence[i]:
			sys.stdout.write('*')
			success_count = success_count + 1
		else:
			sys.stdout.write('>')
		sys.stdout.flush()
	print(" ")
	new_word = ''.join(rand_word)
	print("randomly predicted sentence:")
	print(new_word)
	print(" ")
	pred = "%.2f%%" %(success_count/144 * 100)
	print("success of random prediction: %s" %(pred))
	if new_word is sentence:
		print("'%s' took %i attempts to be randomly generated" %(sentence, counter))
