#Remember to use the random module
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
import random

res=random.randint(0,1)

if(res==1):
    print ("Head")
else:
    print ("Tails")