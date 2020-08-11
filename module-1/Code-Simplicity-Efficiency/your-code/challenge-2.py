"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

#def RandomStringGenerator(l=12, a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):
#    p = 0
#    s = ''
#    while p<l:
#        import random
#        s += random.choice(a)
#        p += 1
#    return s

#def BatchStringGenerator(n, a=8, b=12):
#    r = []
#    for i in range(n):
#        c = None
#        if a < b:
#            import random
#            c = random.choice(range(a, b))
#        elif a == b:
#            c = a
#        else:
#            import sys
#            sys.exit('Incorrect min and max string lengths. Try again.')
#        r.append(RandomStringGenerator(c))
#    return r

#a = input('Enter minimum string length: ')
#b = input('Enter maximum string length: ')
#n = input('How many random strings to generate? ')

#print(BatchStringGenerator(int(n), int(a), int(b)))


#I used the libary string because that's the most convient way of making a string with Upper, Lower, digits,...
#The use of isnumeric() = boolean express. 

import string
import random 


def get_random_string(length):
    letters = string.ascii_lowercase+string.digits
    str = ''.join(random.choice(letters) for num in range(length))
    return str
    
#print(get_random_string(10))

def string_gen ():
    strings = []
    number_of_strings = input("How many strings do you want to generate? ")
    minimum_length = input("What is the minimum length that you want? ")
    maximum_length = input("What is the max length that you want? ")
    
    while not number_of_strings.isnumeric(): 
        print("We only accept numeric values.")
        number_of_strings = input("How many strings do you want to generate?")
    while not minimum_length.isnumeric(): 
        print("We only accept numeric values. ")
        minimum_length = input("What the minimum length that you want? ")
    while not maximum_length.isnumeric(): 
        print("We only accept numeric values. ")
        maximum_length = input("What is the max length that you want? ") 
    
    number_of_strings = int(number_of_strings)
    minimum_length = int(minimum_length)
    maximum_length = int(maximum_length)
    
    while True: 
        if maximum_length < minimum_length: 
            print("Program reboots because your max is smaller than your minimum")
            string_gen()
            break
        else: 
            break
    
    final_length = [minimum_length, maximum_length]
    final_length = random.choice(final_length)
    
    while number_of_strings > 0:
        string = get_random_string(final_length)
        strings.append(string)
        number_of_strings = number_of_strings - 1
        
    return strings
            
            
            
            
print(string_gen())

