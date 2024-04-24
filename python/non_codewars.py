# Given an array of words, words[i] can be paired with words[j] if:  words[i] is the reverse of words[j]. 
# Return number of possible pairs (Each word can only be in one pair). Else, return -1
# E.g: [“ab”, “cd”, “dc”, “ba”] => 2


def words(array):
    count = 0
    for i in array:
        rev_word = i[::-1]

        if rev_word in array:
            count = count + 1
        
    return int(count/2)
        

array = ['ab', 'cd', 'dc', 'ba', 'fg', 'gf','hg', 'gh']
print(words(array))