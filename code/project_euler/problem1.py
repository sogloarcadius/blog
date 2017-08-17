#!/usr/bin/python3

# Find the sum of all the multiples of 3 or 5 below 1000.
# BELOW 1000 : exclude 1000

def isMultiple3or5(number):
    if number % 3 == 0 or number % 5 == 0:
        return True
    else:
        return False

    
if __name__ == '__main__':
    
    mutiple_of_3_or_5 = []
    for number in range(10):
        if isMultiple3or5(number):
            mutiple_of_3_or_5.append(number)
    
    print(mutiple_of_3_or_5)
    print(sum(mutiple_of_3_or_5))
        

        
