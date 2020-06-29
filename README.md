Treehouse Techdegree #Project-3 Phrase Hunters

This is an exercise in object-oriented programming using Python. 
 
This is a game where the users guess the characters (letters and spaces only) in a phrase. They have 5 lives, losing one for each wrong guess. The phrase should be randomly chosen from a list of at least five phrases. Before each character has been guessed correctly an underscore will be displayed in its place. Spaces should be displayed at all times, to show the separation of words. 

Every character in the phrase is converted to an instance of the character class. The actual phrase that the user is trying to guess is an instance of the Phrase class holding a list of all instances of the Character class. 

The Character class holds each of the characters in the phrase. Only 1 letter (A-Z) or space can be passed, or else an error will occur.  The show() method returns either the character, space or, if the character has not yet been guessed, an underscore to hide the character.

The Phrase class takes in a string phrase and makes a list of Character instances. The class has a dynamic() method for making a dynamic list, or phrase, that calls the Character().show() for every instance of characters in the phrase. The display() method joins the list made by the dynamic() method and prints the string in its current state for the user to see how much of the phrase is correctly guessed. The check() method verifies whether the full phrase is guessed or not and sets all the Characters' was.guessed attribute to false if the full phrase is guessed, in case it gets picked again.  

The Game class ties it all together. The verification() method verifies that it is a valid list of string phrases that is passed to the instance of Game(). If not, the program will exit, as the user needs to add valid phrases in order to play. The guessing() method handles the guess input and changes the Character().was_guessed attribute to True for every instance of the same letter that the user guessed correctly. It also subtracts a life if the guess is wrong, and it informs the user if the input is not valid. The game_loop() and retry() methods make the game a continuous experience for the user.  