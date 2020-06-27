import random
import string

from character import Character
from phrase import Phrase

class Game:

    def __init__(self, phrases):

        self.lives = 5
        self.play = True
        self.phrases = phrases

        if self.verification():
            self.phrases = phrases
            self.phrase_picker()
            
        else:
            print("\nYou can only add a list of >= 5 phrases in string format. Example: ['valid list', 'of five', 'phrases in', 'string format', 'are required']. Try again.\n")
            exit()


    def verification(self):
        verified_list = True
        verified_str = True

        if not isinstance(self.phrases, list) or len(self.phrases) < 5:
            verified_list = False

        for i in self.phrases:
            if not isinstance(i, str):
                verified_str = False
                break

        return verified_list and verified_str
    

    def phrase_picker(self):

        try:
            self.phrase = []
            
            for i in list(random.choice(self.phrases)):
                self.phrase.append(Character(i.lower()))

            self.phrase = Phrase(self.phrase)

        except ValueError as error:

            print("\nInvalid characters in the phrase: {}. Please start over with a list of valid phrases.\n".format(error))
            

    def guessing(self):
        guess = input("\nPlease make a guess: ")
        
        if guess in string.ascii_letters and len(guess) == 1:
            if guess in self.phrase:
                for i in self.phrase:
                    if i == guess:
                        i.was_guessed = True
            else:
                self.lives -= 1
                print("\nWrong! You have {} lives remaining".format(self.lives))

            self.phrase.dynamic()
            self.phrase.display()
            
        else:
            print("\nPlease use only letters from A-Z, and only one per guess.")
            self.phrase.display()


    def retry(self):
        retry = input("\nWould you like to retry? [yay/nay] ")
        
        if retry.lower() == "yay":
            self.lives = 5
            self.phrase_picker()
            self.game_loop()
            
        elif retry.lower() == "nay":
            print("\nEnjoy your day!")
            self.play = False
            
        else:
            print("\nEither yay or nay")
            self.retry()
            

    def game_loop(self):
        self.phrase.dynamic()
        self.phrase.display()

        while self.play:

            if not self.phrase.check() and self.lives > 0:
                
                self.guessing()
                
            elif self.phrase.check():
                print ("\nCongratulations!")
                self.retry()
  
            else:
                print("\nGame over!")
                self.retry()
                
    
