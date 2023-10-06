# Problem | https://www.interviewquery.com/questions/prime-to-n
#Given an integer N, write a function that returns a list of all of the prime numbers up to N.
#Note: Return an empty list if there are no prime numbers less than or equal to N.

import math

def prime_numbers(N):

    if N<2:
        array=[] 
    else:
        array =[]
        for i in range(2,N+1):
            for j in range(2,int(math.sqrt(i)) + 1):
                if i%j==0:
                    i = 0
            if i !=0:
                array.append(i)
    return array
                       
                       
if __name__ == "__main__":
    
    N = input("Enter a number:")
    array = prime_numbers(int(N))
    if not array:
        print("NO Prime",array)
    else:
        print("Prime Num List", array)
                       
                       