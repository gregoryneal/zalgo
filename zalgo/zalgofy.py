import random

class zalgo():
    
    def zalgofy(self, text):
        '''
        Zalgofy a string
        '''
        #downward going diacritics
        dd = ['̖',' ̗',' ̘',' ̙',' ̜',' ̝',' ̞',' ̟',' ̠',' ̤',' ̥',' ̦',' ̩',' ̪',' ̫',' ̬',' ̭',' ̮',' ̯',' ̰',' ̱',' ̲',' ̳',' ̹',' ̺',' ̻',' ̼',' ͅ',' ͇',' ͈',' ͉',' ͍',' ͎',' ͓',' ͔',' ͕',' ͖',' ͙',' ͚',' ',]
        #upward diacritics
        du = [' ̍',' ̎',' ̄',' ̅',' ̿',' ̑',' ̆',' ̐',' ͒',' ͗',' ͑',' ̇',' ̈',' ̊',' ͂',' ̓',' ̈́',' ͊',' ͋',' ͌',' ̃',' ̂',' ̌',' ͐',' ́',' ̋',' ̏',' ̒',' ̽',' ̉',' ͣ',' ͤ',' ͥ',' ͦ',' ͧ',' ͨ',' ͩ',' ͪ',' ͫ',' ͬ',' ͭ',' ͮ',' ͯ',' ̾',' ͛',' ͆',' ̚',]
        #build the alterations - zalgo and [text](/a) for shaking angery text
        dm = [' ̕',' ̛',' ̀',' ́',' ͘',' ̡',' ̢',' ̧',' ̨',' ̴',' ̵',' ̶',' ͜',' ͝',' ͞',' ͟',' ͠',' ͢',' ̸',' ̷',' ͡',' ҉','_',]
        #get the letters list
        letters = list(text) #['p','r','e',...]
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

            num = random.randint(1,3)
            #add the diacritics going up
            for i in range(num):                            
                d = du[random.randrange(0, len(du))]
                a = a + d

            num = random.randint(1,3)
            #add the diacritics going down
            for i in range(num):                            
                d = dd[random.randrange(0, len(dd))]
                a = a + d

            num = random.randint(0,2)
            #add the diacritics in the middle
            for i in range(num):                            
                d = dm[random.randrange(0, len(dm))]
                a = a + d
                        
            a = a.replace(" ","") #remove any spaces, this also gives it the zalgo text look
            #print('accented a letter: ' + a)
            newLetters.append(a)
                        
        newWord = ''.join(newLetters)
        return newWord

if __name__ == "__main__":
    z = zalgo()

    while True:
        print(z.zalgofy("my transcriptions a r e v i t a l"))
        input("press enter to continue...")