import string

class Character(str):
    """
    An instance of the character class is created for every letter and
    whitespace in the phrase. The class holds the character and information
    of wether or not the character have been guessed.
    """

    def __init__(self, char):
        
        self.was_guessed = False

        if (isinstance(char, str) and len(char) == 1 and
            (char in string.ascii_letters or char ==" ")):
            self.original = char
            
        else:
            raise ValueError("A character can only be one",
                             "letter or a whitespace in string format.")
      
    def show(self):
        """
        Returns the character if it is a whitespace or if it was guessed,
        else it will return an underscore.
        """
    
        if self.original == " ":
            return (self.original)
        
        elif self.was_guessed:
            return (self.original)
        
        return ("_")
