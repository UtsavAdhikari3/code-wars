# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters 
# reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one
# word is present.

# Examples:

# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"


def spin_words(sentence):
    list1 = sentence.split()
    list2 = []
    
    for i in list1:
        if len(i)>=5:
            i = i[::-1]
            list2 = list2 + [i]
        else:
            list2 = list2 + [i]
            
    
    return ' '.join(list2)
        
      
sentence = "Hey fellow warriors"

print(spin_words(sentence))

        
        
            
