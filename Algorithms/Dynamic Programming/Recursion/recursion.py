'''
Created on Sep 10, 2018
'''

from cs115 import map,range ,reduce,filter
import math


def factorial (n):
    if n==0:
        return 1
    return n*factorial(n-1)

#print(factorial(5))

def tower(n):
    '''Computes 2^(2^(2..)) n times'''
    if n==0:
        return 1
    return  2**tower(n-1)

#print(tower(3))
    
#print(tower,range(6)) 

def tower_reduce(n):
    
    def power(x,y):
        return x**y 
    return reduce(power,(2,n))

#print (map(tower_reduce,range(1,5)))

def length(lst):
    '''Returns the length of the list without using the built-in fnc.'''
    if lst==[]:
        return 0
    return 1+length(lst[1:])


#print (length([1,2,3,4,5,8]))
 

def length_str(s):
    """Returns the length of the string."""
    if s==" ":
        return 0
    return  1+length_str(s[1:])

#print(length_str('mango'))

 
def reverse(lst):
    '''Takes a list of elements as input and returns the list in reverse order.'''
    if lst==[]:
        return []
    return reverse(lst[1:])+[lst[0]]

#print(reverse([2,3,5]))

 
def member(x,lst):
    '''Returns True if x is contained in the list and False otherwise.'''
    if lst == []:
        return False
    if x == lst[0]:
        return True
    return member(x,lst[1:])##tail recursive function

#print(member(2,[1,2,5]))
 
def collapse(lst):
    '''Collapses a list of possibly nested lists into a single list of values.'''
    if lst == []:
        return []
    if isinstance(lst[0],list):
        return collapse(lst[0])+collapse(lst[1:])
    return [lst[0]]+ collapse(lst[1:])
                
#print(collapse([1,[2,3],[5],[4]]))


def sqr(x):
    return x*x
  
def my_map(f,lst):
    '''Return a new list where the function f has been applied to every element in the original list.'''
    if lst == []:
        return []
    return [f(lst[0])]+my_map(f,lst[1:])

#print(my_map(sqr,[6,7,89,8]))

"""Tail"""

    
def power(x,y):
    '''Returns x^y.'''
    if y == 0:
        return 1    
    return x*power(x,y-1)

#print(power(2,3))
  
def power_tail(x,y):
    '''computes x^y with tail recursion.'''
    def power_tail_helper(x,y,accum):
        if y == 0:
            return accum 
        return power_tail_helper(x,y-1,accum*x)
    return power_tail_helper(x,y,1)

#print(power_tail(4,3))
  
def my_reduce(f,lst):
    '''Reduces a new list where it's been reduced to a single value as dictated by the predicate f.'''
    if lst == []:
            raise TypeError('my_reduce()or empty sequence with no initial value.')
    def my_reduce_helper(f,lst,accum):
        if lst == []:
            return accum
        return my_reduce_helper(f,lst[1:],f(accum,lst[0]))
    return my_reduce_helper(f,lst[1:],lst[0])

def add(x,y):
    return x+y
  
#print(my_reduce(add,[1,2,3]))
  
  
  
def prime(n):
    '''Returns True if n is prime and False otherwise by testing all possible divisors from 2 to n-1 or sqrt of n.'''
    possible_divisors = range(2,int(math.sqrt(n))+1)
    divisors = filter(lambda x:n%x == 0, possible_divisors)
    return len(divisors) == 0

#print(prime(10))

def prime_below(n):
    '''Returns the list of all prime numbers less than or equal to n.'''
    def sieve(lst):
        if lst == []:
            return []
        return [lst[0]]+sieve(filter(lambda x: x%lst[0]!=0 , lst[1:]))
    return sieve(range(2,n+1))

#print(prime_below(83))

def fib(n):
    '''Returns the nth number.'''
    if n==0 or n==1:
        return n 
    return fib(n-1)+fib(n-2)  ###tree recursion

#print(fib(4))

def subset(target,lst):
    '''Determines whether or not it is possible to create target sum using the values in the list. 
       Values in the list can be positive,negative or zero.'''
    if target==0:
        return True
    elif lst==[]:
        return False
    return subset(target-lst[0],lst[1:]) or subset(target,lst[1:])

#print(subset(15,[1,10,25,50]))




def powerset(lst):
    '''Returns the power set of the list, that is, the set of all subsets of the list.'''
    if lst == []:
        return [[]]
    lose_it = powerset(lst[1:])
    use_it = map(lambda subset: [lst[0]]+subset,lose_it)
    return lose_it +use_it

#print(powerset([1,2,3]))


def subset_with_values(target,lst):
    '''Determines whether or not it is possible to create target sum using the values in the list. 
       Values in the list can be positive,negative or zero. The function returns a tuple of exactly two items.
       The first is a Boolean that indicates True if the sum is possible and 
       False if it's not. The second element in the tuple is a list of all the values that add up to make the target sum.'''
    
    if target == 0:
        return [True,[]]
    if lst == []:
        return [False,[]]
    use_it = subset_with_values(target-lst[0],lst[1:])
    if use_it[0]:
        return [True, [lst[0]] + use_it[1] ]
    return subset_with_values(target,lst[1:])


print(subset_with_values(5,[1,2,3]))



def LCS (s1,s2):
    '''returns the length of the longest common sequence in string s1 and s2.'''
    if s1 == '' or s2 == '':
        return 0
    if s1[0] == s2[0]:
        return 1 + LCS(s1[1:],s2[1:])
    return max(LCS (s1,s2[1:]), LCS(s1[1:], s2))

print(LCS('stocks','bonds'))
    
def LCS_with_values(s1,s2):
    if s1 == '' or s2 == '':
        return [0,'']
    if s1[0] == s2[0]:
        result = LCS_with_values(s1[1:],s2[1:])
        return [1+result[0],s1[0]+result[1]]
    
    useS1 = LCS_with_values(s1,s2[1:])
    useS2 = LCS_with_values(s1[1:],s2)
    if useS1[0]>useS2[0]:
        return useS1
    return useS2


print(LCS_with_values('poles','poke'))

def coin_row(lst):
    if lst == []:
        return 0
    return max(lst[0] + coin_row(lst[2:]),coin_row(lst[1:]))

print(coin_row([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))

def coin_row_with_values(lst):
    if lst == []:
        return [0,[]]
    use_it = coin_row_with_values(lst[2:])
    new_sum = lst[0] + use_it[0]
    lose_it = coin_row_with_values(lst[1:])
    if new_sum > lose_it[0]:
        return [new_sum,[lst[0]]+use_it[1]]
    return lose_it 

print(coin_row_with_values([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))

def distance(first,second):
    if first == '':
        return len(second)
    if second == '':
        return len(first)
    if first[0]==second[0]:
        return distance(first[1:],second[1:])
    substitution = 1 + distance(first[1:],second[1:])
    deletion = 1 + distance(first,second[1:])
    insertion = 1+distance(first[1:],second)
    return 1 + min(substitution, deletion, insertion)

     
    
    


    
      
      


