from character import Character

class Phrase():

    def __init__(self, phrase):
        self.phrase = []

        for char in list(phrase):
            self.phrase.append(Character(char.lower()))
        

    def __iter__(self):
        yield from self.phrase

        
    def check(self):
        if "_" in self.dynamic_phrase:
            return False

        else:
            for char in self.phrase:
                char.was_guessed = False

        return True

    def display(self):
        print ("\n"+"".join(self.dynamic_phrase))


    def dynamic(self):
        self.dynamic_phrase = []

        for i in self.phrase:
            self.dynamic_phrase.append(i.show())



    
        

        
    
        

 

        

  
        
