# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
# We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. 
# It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"


def likes(names):
    # your code here
    if len(names) == 0 :
        return "no one likes this"
    
    elif len(names) == 1:
        for i in names:
            a = f"{i} likes this"
            
        return a
        
    elif len(names) == 2 :
        for i in range(len(names)-1):
            a = f"{names[i]} and {names[i+1]} like this"
        return a
        
    elif len(names) == 3 :
        for i in range(len(names)-2):
            a = f"{names[i]}, {names[i+1]} and {names[i+2]} like this"
        return a
        
    elif len(names)>3:
        for i in range((len(names))-(len(names)-1)):
            a = f"{names[i]}, {names[i+1]} and {len(names)-2} others like this"
        return a
    
    
print(likes(['Macky Stingray', 'Linna Yamazaki', 'Daley Wong', 'Galatea', 'Leon McNichol', 'Nigel','Utsav']))