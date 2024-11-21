#! python3
"""
The Fibonacci sequence was created to model how populations
of bunnies increase over time.  It is also used in strategies
that prolong how long you can play Blackjack before you 
eventually lose all your money.
It follows a pattern where the last two number are added 
together to make the next number, starting with 1 1:
Create a program to show the Fibonacci sequence, stopping
after the number in the sequence is greater than 100:
(2 points) 

Example:
1 1 2 3 5 ...
"""
import os

os.system("cls")

num1 = int(0)
num2 = int(0)
fnum = int(1)

while fnum < 100:
    print(fnum)
    num1 = num2
    num2 = fnum
    fnum = num1 + num2
    if fnum > 100:
        break
print(fnum)

#done