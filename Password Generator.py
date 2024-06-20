#-------------------------------------------------------------------------------
# Name:        Password Generator
# Purpose:
#
# Author:      Hamza Khan
#
# Created:     25-05-2024
# Copyright:   (c) Hamza Khan 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
import string
print("Welcome")
def important():
    length=int(input("Enter The Length of Password: "))
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    digit=string.digits
    symbols=string.punctuation
    combine=lower+upper+digit+symbols
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
important()
important()