import random

class zalgo():

	def __init__(self):
		self.numAccentsUp = (1, 3)
		self.numAccentsDown = (1,3)
		self.numAccentsMiddle = (1,2)
		#downward going diacritics
		self.dd = ['̖',' ̗',' ̘',' ̙',' ̜',' ̝',' ̞',' ̟',' ̠',' ̤',' ̥',' ̦',' ̩',' ̪',' ̫',' ̬',' ̭',' ̮',' ̯',' ̰',' ̱',' ̲',' ̳',' ̹',' ̺',' ̻',' ̼',' ͅ',' ͇',' ͈',' ͉',' ͍',' ͎',' ͓',' ͔',' ͕',' ͖',' ͙',' ͚',' ',]
		#upward diacritics
		self.du = [' ̍',' ̎',' ̄',' ̅',' ̿',' ̑',' ̆',' ̐',' ͒',' ͗',' ͑',' ̇',' ̈',' ̊',' ͂',' ̓',' ̈́',' ͊',' ͋',' ͌',' ̃',' ̂',' ̌',' ͐',' ́',' ̋',' ̏',' ̽',' ̉',' ͣ',' ͤ',' ͥ',' ͦ',' ͧ',' ͨ',' ͩ',' ͪ',' ͫ',' ͬ',' ͭ',' ͮ',' ͯ',' ̾',' ͛',' ͆',' ̚',]
		#build the alterations - zalgo and [text](/a) for shaking angery text
		self.dm = [' ̕',' ̛',' ̀',' ́',' ͘',' ̡',' ̢',' ̧',' ̨',' ̴',' ̵',' ̶',' ͜',' ͝',' ͞',' ͟',' ͠',' ͢',' ̸',' ̷',' ͡',]

	def zalgofy(self, text):
		'''
		Zalgofy a string
		'''
		#get the letters list
		letters = list(text) #['t','e','s','t',' ','t',...]
		#print(letters)
		newWord = ''
		newLetters = []
					
		#for each letter, add some diacritics of all varieties
		for letter in letters: #'p', etc...
			a = letter #create a dummy letter

			#skip this letter we can't add a diacritic to it
			if not a.isalpha():
				newLetters.append(a)
				continue

			num = random.randint(self.numAccentsUp[0],self.numAccentsUp[1])
			#add the diacritics going up
			for i in range(num):                            
				d = self.du[random.randrange(0, len(self.du))].strip()
				a = self.combine(d, a)

			num = random.randint(self.numAccentsDown[0],self.numAccentsDown[1])
			#add the diacritics going down
			for i in range(num):                            
				d = self.dd[random.randrange(0, len(self.dd))].strip()
				a = self.combine(d, a)

			num = random.randint(self.numAccentsMiddle[0],self.numAccentsMiddle[1])
			#add the diacritics in the middle
			for i in range(num):                            
				d = self.dm[random.randrange(0, len(self.dm))].strip()
				a = self.combine(d, a)
						
			#a = a.replace(" ","") #remove any spaces, this also gives it the zalgo text look
			#print('accented a letter: ' + a)
			newLetters.append(a)
						
		newWord = ''.join(newLetters)
		return newWord

	def test(self, *letters):
		for letter in letters:
			for d in self.du:
				print(self.combine(d,letter))
			for d in self.dd:
				print(self.combine(d,letter))
			for d in self.dm:
				print(self.combine(d,letter))

	def combine(self, diacritic, character):
		return diacritic.strip()+character.strip()


if __name__ == "__main__":
	z = zalgo()
	z.numAccentsUp = (0,2)
	z.numAccentsDown = (0,2)
	z.numAccentsMiddle = (0,2)

	print(z.zalgofy("A small library to create zalgo styled text."))
