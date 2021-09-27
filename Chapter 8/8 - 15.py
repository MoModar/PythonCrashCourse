# TRY IT YOUR SELF
# 8 - 15 Printing models:


# from Printing_Function import print_models, show_completed_models
"""Importing Specific  Functions"""
#from Printing_Function import *


import Printing_Function
"""Importing an Entire Module"""

unprinted_designs = ['iphone case', 'xbox case', 'robot pendant']
completed_models = []


Printing_Function.print_models(unprinted_designs[:], completed_models)
Printing_Function.show_completed_models()

print("\nCopy of unprinted designs list:")
print(unprinted_designs)
