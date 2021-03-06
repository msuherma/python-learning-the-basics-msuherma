# ABE36500
# Mukhamad Suhermanto 0030930122
"""
Created on Fri Jan 17 14:27:43 2020

@author: msuherma
"""
# Exercise 3.2
# 1.
def do_twice_1(f):          # define do_twice
    f()
    f()
    
def print_spam():           # to define print_spam
    print('spam1')

do_twice_1(print_spam)      #  to command print_spam using do_twice

# 2.
def do_twice(f,val):        # to define do_twice, f is function, val is value/argument        
    f(val)
    f(val)
# 3.
def print_twice(bruce):     # copying print_twice from earlier as instructed 
    print(bruce)
    print(bruce)
# 4.
do_twice(print_twice, 'spam')
# 5.
def do_four(f,val):         # to define do four
    do_twice(f,val)         # since only two lines are required, then do_twice is used, f is function object, val is value/argument
    do_twice(f,val)
do_four(print_twice,'spam5')
