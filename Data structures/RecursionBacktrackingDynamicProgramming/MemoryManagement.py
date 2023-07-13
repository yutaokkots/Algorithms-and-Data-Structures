#1) when application is compiled, machine-level binary code is generated
#2) machine-level code is loaded into memory
#3) RAM is a memory region that is used to run programs (has 3 segments)
#     i) heap memory
#     ii) stack memory
#     iii) Machine code
#  ______________  
# | heap memory  |   
# |______________| 
# | stack memory |
# |______________|    
# | Machine code |   
# |______________|  

#
# -> Heap Memory
# special region i nthe RAM
# dynamic meemory allocation takes place
# size of heap is much larger than the size of stack memory
# objects and reference types are stored in heap memory, but the reference is stored in the stack memory, pointing to the given object in heap memory
# heap memory is large in size but slow to access
# can be fragmented
#
# -> Stack Memory
# special region in the RAM
# stack abstract data type
# stores local variables and method calls
# how the programming language knows where to return after finishing execution of a given method
# * small in size, but fast to access
# no fragmentation 
#

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
#
# Visually:
#  ______________
# | function_3   |
# |    house_ref | <-- REFERENCE to the Objects are stored in stack (built last)
# |______________|
# | function_2   | <-- function_2 created on top of function_1 as a frame
# |        i, f  |    
# |______________|     <--- STACK
# | function_1   |
# |         d    |   <---- active functions and local variables stored in stack (built first)
# |______________|  
#      STACK
#
#  ______________
# |              |
# |              |
# |              | <-- Stores OBJECTS, like:
# |              |
# |              |      class House:
# |              |          windows = 5  // class variables
# |              |          doors = 10
# |              |   
# |______________|  
#      HEAP

# STACKS store active functions and local variables

# when function_3 is removed, the reference (house_ref) is removed, and the class found in heap memory
#       is eligible for garbage collection
#

