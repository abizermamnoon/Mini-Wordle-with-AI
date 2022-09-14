# Mini-Wordle-with-AI

For our final project, our group chose to make a text-based board-game on the popular New York Times Game known as Wordle. The game involves the player having 6 chances to guess a 5 letter word that was chosen at random from a list. The player is only allowed to guess words that are in the list so any other word will be invalid and they will get to guess again. 

After every word is guessed, the letters that are not in the random word are shown as a '?'. The letters the game shows come from the letters that make up the word the player guessed. If the player guesses a word that contains letters of the random word, the letter will be either lower-cased or upper-cased. A letter that is lower-cased means that the random word contains that letter but the user guessed a word with the letter in the wrong spot. If the letter is upper-cased, then the random word contains the letter in that spot. For example, if the random word was “Dream” and the player guessed “DRUMS”, then letters “U” and “S” would show up as ‘?’, “M” would be a lower-cased ‘m’, and ‘D’ and ‘R’ would show up as upper-cased. Our initial thoughts of the game's design were that the game was simple, yet challenging. At the beginning of our game, the player will be asked if they would like to play against a human (player vs player), against the computer (player vs AI), or watch the computer play (AI play).  To play against a human the player must choose menu option 1, to play against the computer the player must choose menu option 2, and if they want to watch the AI play choose menu option 3. After the user or AI plays a move, the second player or AI plays a move, using the guess as a reference. The strategy used by the AI is to choose a random word from the list that closely resembles the conditions for the word. For example, if the board capitalized “D” and “R” the AI would guess a word that contained those letters in the position they appear in on the board. 

In the end, our code works. We were able to properly make a game based on the game Wordle that plays in a unique way. Using the official Worlde list of words, we were able to make the game closely resemble, feel, and play like the official game. For us, the most difficult part was setting up the AI moves. The AI is choosing its own word, making its own guesses, just like a human would. Coming up with the code for the AI was challenging as the logic for what we wanted the AI to do was tough to translate into code. If there was more time, we would work more on AI. As more capital letters are revealed, it is harder for the AI to win as the AI is creating a list of words of its own after every guess. The list gets larger and larger every time.  

Instructions for Our Game:
1. Open final.py
2. Make sure that the text document "words.txt" is in the same directory as "final.py". 
3. In terminal, create a board by typing w=Wordle(5,6)
4. Next, type w.hostGame() and select among the given options
5. Type in 5 letter words and try to guess the right word!
6. When the game is over, if you wish to play again, repeat the instructions, starting at 3)
7. If you want to quit the game, just type quit in the terminal when you are asked to input a random word.

Thanks for playing!
