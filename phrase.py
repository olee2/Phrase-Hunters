from character import Character

class Phrase():
    """
    The class takes a string phrase and creates a list of Character instances.
    """

    def __init__(self, phrase):
        self.phrase = [Character(char.lower()) for char in list(phrase)]

    def __iter__(self):
        yield from self.phrase

    def check(self):
        """
        Checks if the full phrase has been guessed and, if so,
        set the was.guessed attribute to false for all instances of Character
        in the phrase, in case the same phrase will be picked again.
        """
        
        if "_" in self.dynamic_phrase:
            return False

        else:
            for char in self.phrase:
                char.was_guessed = False

        return True

    def display(self):
        """ Returns a string of the list returned from the dynamic method. """
    
        print ("\n"+"".join(self.dynamic_phrase))

    def dynamic(self):
        """
        Creates a list where Character.show() is called on all
        instances of Character in self.phrase.
        """
        
        self.dynamic_phrase = [i.show() for i in self.phrase]




    
        

        
    
        

 

        

  
        
