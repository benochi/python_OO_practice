"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Finds random words from file
    
    wf = WordFinder("words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
'   dog'"""
    #t is instantiated with a path to a file on disk that contains words, one word per line
    def __init__(self, path):
        """opens file and prints words"""
        open_file = open(path)  
        self.words =self.list_words(open_file)   #it reads that file, and makes an attribute of a list of those words

        print(f"{len(self.words)} words read") #it prints out “[num-of-words-read] words read”


    def random(self):
        """returns random word from file"""
        return random.choice(self.words)
    
    def list_words(self, open_file):
        """Return a list of words from open_file"""
        return [word.strip() for word in open_file] #removes leading/trailing chars.


class SpecialWordFinder(WordFinder):
    """Wordfinder to ignore blanks and comments.
    
    swf = SpecialWordFinder("complex.txt")
    3 words read

    >>>swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def list_words(self, open_file):
        """returns lsit of words from file, ignoring spaces and comments"""
        return [word.strip() for word in open_file if word.strip() and not word.startswith("#")]
