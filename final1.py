#CS5 Final Project

# Paul Abizer and Luis

##Starter    Starting with the example below,
#Decide on an idea for your game
#Self-designed or traditional variations are more than welcome!
#Begin implementing the play-one-round function for your game...
#Be sure your starter.py runs and plays (at least part of) one round of your game successfully.
#You'll need an opponent and/or AI (even if it always plays the same / plays randomly).
#Be sure, too, to include starter.txt with a description of your game's vision (and your final-project team).

import random
def get_text(filename): #used to get access to dictionary of 5 letter words
        f = open(filename, encoding = 'latin1')
        text = f.read()
        f.close()
        return text

class Wordle:
    "A data type that represents the game Wordle"
    
    def __init__(self, width, height):
        """Construct objects of type Wordle, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # The string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # Bottom of the board
        s += '\n'
        for i in range(0, self.width):
            s += ' ' + str(i) # Add code here to put the numbers underneath

        return s       # The board is complete; return it
    
    def addMove(self,col,ox):
        """
        This method takes two arguments: the first, col, represents the index 
        of the column to which the letter will be added. The second argument, 
        ox, will be a 1-character string representing the letter to add to the board. 
        That is, ox should either be an alphabet
        """
        H = self.height
        for row in range(0,H):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return
        self.data[H-1][col] = ox

    def choose_word(self):
        """
        Computer chooses random 5 letter word from dictionary
        """
        w = self.width 
        h = self.height 
        
        word = get_text("words.txt")
        words = []
        words = word.split("\n")
        x = random.choice(words)
        x = x.lower()
        print(x)
        return x

    def match(self,wordx,guess): 
        """
        If user guesses right position for letter, letter is upper-cased
        if user guesses only right letter not right position, a lower case version of
        letter appears on board
        If user guesses wrong letter, letter + X appears on board
        """
        newString = ''
        visible = ''
        for x in range(0,5):
            if guess[x:x+1] == wordx[x:x+1]:
                newString = guess[x:x+1].upper()
                self.addMove(x,newString)
                visible += newString
            elif guess[x:x+1] in wordx:
                newString = guess[x:x+1].lower()
                self.addMove(x,newString)
                visible += newString
            else:
                newString = '?'
                self.addMove(x,newString)
                visible += newString
        print(visible)
        print("Incorrect letters:")
        print(self.wrongLetters)
        print("Correct letters:")
        print(self.correctLetters)
        print("Correct letters in the right spot:")
        print(self.rightSpot)
        print(visible)
    
    def identify_guess(self,wordx,guess): 
        """
        If user guesses right position for letter, letter is upper-cased
        if user guesses only right letter not right position, a lower case version of
        letter appears on board
        If user guesses wrong letter, letter + X appears on board
        """
        newString = ''
        visible = ''
        for x in range(0,5):
            if guess[x:x+1] == wordx[x:x+1]:
                newString = guess[x:x+1].upper()
                #self.addMove(x,newString)
                visible += newString
            elif guess[x:x+1] in wordx:
                newString = guess[x:x+1].lower()
                #self.addMove(x,newString)
                visible += newString
            else:
                newString = '?'
                #self.addMove(x,newString)
                visible += newString
        return visible
    
    def aiMove(self, visible):
        """ Looks at user input. If any Capital letters in user input, creates a list from 
        word list of words having that capital letter in correct position. If any lower case letters
        in Guess, creates a shorter list with Capital letter and small letter.If no correct letters in Guess, randomly selects word
        from text file
        """

        Lol = []
        word = get_text("words.txt")
        words = []
        words = word.split("\n")
         
        for l in range(len(visible)):
            for word in words: 
                if ord('A') <= ord(visible[l]) <= ord('Z') and visible[l].lower() == word[l]:
                    Lol += [word]
                elif ord('a') <= ord(visible[l]) <= ord('z'):
                    Lol += []
                else:
                    Lol += []
        Lol += [word]
        print(Lol)
        
        if Lol == []:
            Lol = words

        return random.choice(Lol)

        
    
    #this function randomly chooses a word for words.txt
    def hostGame(self):
        """
        Play the game of Wordle
        """
        wordx = self.choose_word() #takes word from previous function
        
        word = wordx.lower() #puts word in lowercase

        print(self)
        
        for live in range(5): #this gives us 5 lives
            guess = input("Choose a word:  ") #user guess
            
            if guess == word:
                print('You win!')
                return
            
            if guess == 'quit':
                print('Better luck next time!')
                return
            
            while guess not in (get_text("words.txt")).lower():
                guess = input("Choose another word:  ") 
            
            self.match(word,guess)       
            print(self)
            
            visible = self.identify_guess(wordx,guess)

            comp = self.aiMove(visible)
            self.match(word,comp)       
            print(self)

            if comp == word:
                print('AI wins!')
                return



        print("You Lose!! The word was:" + word) #use if last guess is wrong
        return