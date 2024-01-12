# Every recursive function has two parts:
# the base case
# the recursive case

# the call stack is an important aspect:
# When a function is called from another function, 
# the calling function is paused in a partially completed state
# see MemoryManagement.py for more. 

# Example:
# def function_1():
#   d = 10
#   function_2(20) <-- function_1 is calling function_2 // stored in STACK memory
#
# def function_2(i):
#   f = 30.0
#   function_3()  <-- function_2 is calling function_3 // stored in STACK memory
#
# def function_3():
#   house_ref = House()  <- instantiation of a class ** stored in HEAP memory

# Visually:
#  ______________
# | function_3   |
# |    house_ref | <-- REFERENCE to the Objects are stored in stack (built last)
# |______________|
# | function_2   | <-- function_2 created on top of function_1 as a frame
# |        i, f  |    
# |______________|     <<<--- STACK
# | function_1   |
# |         d    |   <---- active functions and local variables stored in stack (built first)
# |______________|  
#      STACK