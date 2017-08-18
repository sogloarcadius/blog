#!/usr/bin/python3


def check_is_prime(number):
    isPrime = True
    for i in range(2,number):
        if i != number and number % i == 0:
            isPrime = False
            
    return isPrime
    
            
          
def get_prime_numbers(n):         
    prime_numbers = []
    for i in range(2, n+1):
        if check_is_prime(i):
            prime_numbers.append(i)
    return prime_numbers



def get_prime_factors(number):
    
    actual_value = number
    prime_numbers = get_prime_numbers(number)
    prime_factors = []
    while actual_value != 1:
        for prime_number in prime_numbers:
            if actual_value % prime_number == 0:
                actual_value = actual_value / prime_number
                actual_prime_factor = prime_number
                prime_factors.append(actual_prime_factor)
                pass
    return prime_factors
        
     
    
def get_largest_prime_factors(number):
    actual_value = number
    actual_prime_factor=1
    i = 2
    while ( i < number ):
        i=i+1
        if actual_value != 1:
            if check_is_prime(i):
                prime_number = i
                if actual_value % prime_number == 0:
                    
                    actual_value = actual_value / prime_number
                    if prime_number > actual_prime_factor:
                        actual_prime_factor = prime_number

    return actual_prime_factor
        
        
   