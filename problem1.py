##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""

import os

os.system("cls")

username = ""
password = ""
attempts = int(3)

while username != "admin" and password != "12345" and attempts > 0:
    os.system("cls")
    print(f"You have {attempts} attempts remaining")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username != "admin" and password != "12345" and attempts > 0:
        print("Access denied")
        attempts = attempts - 1
    elif attempts < 1:
        print("Too many failed attempts. Access denied.")
        exit
    else:
        break
print("Access granted")

#done