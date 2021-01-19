# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 10:49:21 2021

@author: DiSoJi

The objective of this small test is to compare the time consumption of two different flow control mechanisms.
We have the if-elif-else statement option and the list-tuple-dictionary option.

Several differences appear obvious. For example, the list-tuple-dictionary option requires for the code to be in functions/methods
to work properly, since we are using the function reference as elements in the data structures. Which also requires them to be
declared prior to use. On the other hand, the if-elif-else statements don't require this.

In a case where the call of functions is what the program requires then this will mean that the list-tuple-dictionary option will lead to
a cleaner, shorter code.
"""
import time

#Every option does the same. Two simple addition operation
def option_0():
    a = 1+1
    a+=a
def option_1():
    a = 1+1
    a+=a
def option_2():
    a = 1+1
    a+=a
def option_3():
    a = 1+1
    a+=a
def option_4():
    a = 1+1
    a+=a
def option_5():
    a = 1+1
    a+=a
def option_6():
    a = 1+1
    a+=a
def option_7():
    a = 1+1
    a+=a
def option_8():
    a = 1+1
    a+=a
def option_9():
    a = 1+1
    a+=a

#Definition of constants
OPTION_LIST= [option_0,option_1,option_2,option_3,option_4,option_5,option_6,option_7,option_8,option_9]
OPTION_TUPLE = (option_0,option_1,option_2,option_3,option_4,option_5,option_6,option_7,option_8,option_9)
OPTION_DICTIONARY = {0:option_0,1:option_1,2:option_2,3:option_3,4:option_4,5:option_5,6:option_6,7:option_7,8:option_8,9:option_9}    



def list_alternative_constant_tuple(option):
    OPTION_TUPLE[option]()

def list_alternative_created_tuple(option):
    OPTION_TUPLE_C = (option_0,option_1,option_2,option_3,option_4,option_5,option_6,option_7,option_8,option_9)
    OPTION_TUPLE_C[option]()

def list_alternative_constant_dictionary(option):
    
    OPTION_DICTIONARY[option]()    

def list_alternative_created_dictionary(option):
    OPTION_DICTIONARY_C = {0:option_0,1:option_1,2:option_2,3:option_3,4:option_4,5:option_5,6:option_6,7:option_7,8:option_8,9:option_9}    
    OPTION_DICTIONARY_C[option]()    
    
def list_alternative_constant_list(option):
    OPTION_LIST[option]()
    
def list_alternative_created_list(option):
    OPTION_LIST_C= [option_0,option_1,option_2,option_3,option_4,option_5,option_6,option_7,option_8,option_9]
    OPTION_LIST_C[option]()


    
def if_elif_statement_no_function_calls(option):
    if option == 0:
        a = 1+1
        a+=a
    elif option == 1:
        a = 1+1
        a+=a
    elif option == 2:
        a = 1+1
        a+=a
    elif option == 3:
        a = 1+1
        a+=a
    elif option == 4:
        a = 1+1
        a+=a
    elif option == 5:
        a = 1+1
        a+=a
    elif option == 6:
        a = 1+1
        a+=a
    elif option == 7:
        a = 1+1
        a+=a
    elif option == 8:
        a = 1+1
        a+=a
    else:
        a = 1+1
        a+=a
        
def if_elif_statement(option):
    if option == 0:
        option_0()
    elif option == 1:
        option_1()
    elif option == 2:
        option_2()
    elif option == 3:
        option_3()
    elif option == 4:
        option_4()
    elif option == 5:
        option_5()
    elif option == 6:
        option_6()
    elif option == 7:
        option_7()
    elif option == 8:
        option_8()
    else:
        option_9() 


if __name__=='__main__':
    #print("Begins")
    REPETITIONS = 1000000
    #if-elif-else statement###################################
    avg_time = 0.0
    for _ in range(0,REPETITIONS):
        for i in range(0,10):
            t = time.perf_counter()
            if_elif_statement(i)
            elapsed_time = time.perf_counter() - t
            avg_time+=elapsed_time
    avg_time = avg_time/REPETITIONS
    print("Average Elapsed time (if statement): ", avg_time," With: ",REPETITIONS," repetitions.")
    
    #if-elif-else statement no function calls###################################
    avg_time = 0.0
    for _ in range(0,REPETITIONS):
        for i in range(0,10):
            t = time.perf_counter()
            if_elif_statement_no_function_calls(i)
            elapsed_time = time.perf_counter() - t
            avg_time+=elapsed_time
    avg_time = avg_time/REPETITIONS
    print("Average Elapsed time (if statement no function calls): ", avg_time," With: ",REPETITIONS," repetitions.")
    
    #Constant list alternative################################
    avg_time = 0.0
    for _ in range(0,REPETITIONS):
        for i in range(0,10):    
            t = time.perf_counter()
            list_alternative_constant_list(i)
            elapsed_time = time.perf_counter() - t
            avg_time+=elapsed_time
    avg_time = avg_time/REPETITIONS
    print("Average Elapsed time (constant list alternative): ", avg_time," With: ",REPETITIONS," repetitions.")
    
    #Created list alternative ################################
    avg_time = 0.0
    for _ in range(0,REPETITIONS):
        for i in range(0,10):    
            t = time.perf_counter()
            list_alternative_created_list(i)
            elapsed_time = time.perf_counter() - t
            avg_time+=elapsed_time
    avg_time = avg_time/REPETITIONS
    print("Average Elapsed time (created list alternative): ", avg_time," With: ",REPETITIONS," repetitions.")
    
    #Constant tuple alternative ################################
    avg_time = 0.0
    for _ in range(0,REPETITIONS):
        for i in range(0,10):    
            t = time.perf_counter()
            list_alternative_constant_tuple(i)
            elapsed_time = time.perf_counter() - t
            avg_time+=elapsed_time
    avg_time = avg_time/REPETITIONS
    print("Average Elapsed time (constant tuple alternative): ", avg_time," With: ",REPETITIONS," repetitions.")
    
    #Created tuple alternative ################################
    avg_time = 0.0
    for _ in range(0,REPETITIONS):
        for i in range(0,10):    
            t = time.perf_counter()
            list_alternative_created_tuple(i)
            elapsed_time = time.perf_counter() - t
            avg_time+=elapsed_time
    avg_time = avg_time/REPETITIONS
    print("Average Elapsed time (created tuple alternative): ", avg_time," With: ",REPETITIONS," repetitions.")
    
    #Constant dictionary alternative ################################
    avg_time = 0.0
    for _ in range(0,REPETITIONS):
        for i in range(0,10):    
            t = time.perf_counter()
            list_alternative_constant_dictionary(i)
            elapsed_time = time.perf_counter() - t
            avg_time+=elapsed_time
    avg_time = avg_time/REPETITIONS
    print("Average Elapsed time (constant dictionary alternative): ", avg_time," With: ",REPETITIONS," repetitions.")
    
    #Created dictionary alternative ################################
    avg_time = 0.0
    for _ in range(0,REPETITIONS):
        for i in range(0,10):    
            t = time.perf_counter()
            list_alternative_created_dictionary(i)
            elapsed_time = time.perf_counter() - t
            avg_time+=elapsed_time
    avg_time = avg_time/REPETITIONS
    print("Average Elapsed time (created dictionary alternative): ", avg_time," With: ",REPETITIONS," repetitions.")