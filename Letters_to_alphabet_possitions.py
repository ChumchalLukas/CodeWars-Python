# Kata: Replace with alphabet position

# In this ka ta you are required to, given a string, replace every letter with its position in the alphabet.
# If anything is the text is not a letter, ignore it and do not return it.

# Input - string, sentence 
# Output - letters number by it is possition in alphabet with gab between each number

# Main used idea : nested list - list inside a list | 

def alphabet_position(text):
    """
    Change letters into it´s possition in alphabet
    
    """
    
    alphabeto = {"a": 1, "b":2, "c":3,"d":4,"e":5, "f":6,"g":7,"h":8,"i":9,"j":10,"k":11,
                 "l":12, "m":13,"n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21,
                 "v":22, "w":23, "x":24, "y":25,"z":26      
    }
    
    text_words = list(text.lower().split(" ")) # Sentence to words
    
    for i in range(0,len(text_words)): # Nested list - words to letters
        text_words[i] = list(text_words[i])            
    
    result = []
    
    for i in text_words: # Change letters to possitions in alphabet
        for j in i:
            if j in alphabeto.keys():
                result.append(str(alphabeto[j]))
            else:
                 continue
    
    return ' '.join(result)
  
 
