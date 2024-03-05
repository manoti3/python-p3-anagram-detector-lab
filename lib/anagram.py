# your code goes here!
class Anagram:
    def __init__(self, word, anagramiclist=list()):
        self.word = word
        self.anagramiclist = anagramiclist
    
    def match(self, list):
        self.anagramiclist = []
        wordcheck = sorted([letter for letter in self.word])
        print(f'original word:{self.word}')
        for entry in list:
            entrycheck = sorted([letter for letter in entry])
            if wordcheck == entrycheck:
                self.anagramiclist.append(entry)
        print(self.anagramiclist)
        return self.anagramiclist