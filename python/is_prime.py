# // Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

# // Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# // Requirements

# //     You can assume you will be given an integer input.
# //     You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
# //     NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.


def is_prime(num):#My solution
    count = 0
    if num < 2:
        return False
    
    for i in range(1,num):
        
        if num%i == 0:
            count = count + 1
            
        if count > 1:
            break
            
    
    if count > 1:
        return False
        
    else:
        return True
    
def is_prime_hm(number):#clever solution
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
    
    
    
            
    
        
    
        
                

print(is_prime(2))



