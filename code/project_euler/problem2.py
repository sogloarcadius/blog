#!/usr/bin/python

def find_n_fibo_numbers(n):
    fibotab = []
    fibotab.insert(0,1)
    fibotab.insert(1,2)
    
    for i in range(2, n):
        fibotab.insert(i,fibotab[i-2] + fibotab[i-1])
   
    return fibotab



def find_sum_even_numbers(fibotab):
    sum_even_numbers = 0
    for value in fibotab:
        if value % 2 == 0: #even numbers
            sum_even_numbers+=value
    
    return sum_even_numbers



## Optimization VS Reusability


##Low memory comsumption solution

def find_fibo_sum_even_numbers(n):
    
    fibotab = []
    fibotab.insert(0,1)
    fibotab.insert(1,2)
    fibo_sum_even_numbers=2
    
    for i in range(2, n):
        fibotab.insert(i,fibotab[i-2] + fibotab[i-1])
        if fibotab[i] % 2 == 0:
            fibo_sum_even_numbers+=fibotab[i]
    
    return fibo_sum_even_numbers
            

    
#Reusability    

if __name__ == '__main__':
    
    n = 4*10^6
    
    fibotab = find_n_fibo_numbers(n)
    
    print(find_sum_even_numbers(fibotab))
            
            
        
        
    