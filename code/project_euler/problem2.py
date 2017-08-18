#!/usr/bin/python

# def find_n_fibo_numbers(n):
#     fibotab = []
#     fibotab.insert(0,1)
#     fibotab.insert(1,2)
    
#     for i in range(2, n):
#         fibotab.insert(i,fibotab[i-2] + fibotab[i-1])
   
#     return fibotab



# def find_sum_even_numbers(fibotab):
#     sum_even_numbers = 0
#     for value in fibotab:
#         if value % 2 == 0: #even numbers
#             sum_even_numbers+=value
    
#     return sum_even_numbers





# def find_fibo_sum_even_numbers(n):
    
#     fibotab = []
#     fibotab.insert(0,1)
#     fibotab.insert(1,2)
#     fibo_sum_even_numbers=2
    
#     for i in range(2, n):
#         fibotab.insert(i,fibotab[i-2] + fibotab[i-1])
#         if fibotab[i] % 2 == 0:
#             fibo_sum_even_numbers+=fibotab[i]
    
#     return fibo_sum_even_numbers
            

## Optimization VS Reusability
##Low memory comsumption solution  

def get_value(value):
    return value


def find_fibo_sum_even_numbers(n):
    U0=1
    U1=2
    fibo_sum_even_numbers=2
    #print(U0)
    #print(U1)
    i=3
    UN=0
    while (UN < n):
        UN=U0+U1
        if UN % 2 == 0:
            fibo_sum_even_numbers+=UN
            
        #print(UN)
        U0=get_value(U1)
        U1=get_value(UN)
        i+=1
    return fibo_sum_even_numbers


print(find_fibo_sum_even_numbers(4000001))

# if __name__ == '__main__':
    
#     n = 4*10^6
    
#     fibotab = find_n_fibo_numbers(n)
    
#     print(find_sum_even_numbers(fibotab))
            
            
        
        
    