import string

class Character(str):

    def __init__(self, char):
        self.was_guessed = False

        if isinstance(char, str) and len(char) == 1 and (char in string.ascii_letters or char ==" "):
            self.original = char
        else:
            raise ValueError("A character can only be one letter or a whitespace in string format.") 
            
    def show(self):
        if self.original == " ":
            return (self.original)
        elif self.was_guessed:
            return (self.original)
        return ("_")



    
        
        
