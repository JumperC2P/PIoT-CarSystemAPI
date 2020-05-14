# Documentation: https://passlib.readthedocs.io/en/stable/index.html
# Reference: https://pythonprogramming.net/password-hashing-flask-tutorial/
# pip3 install passlib
from passlib.hash import mysql323

hashedPassword = mysql323.hash("ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f")
# hashedPassword = sha256_crypt.using(rounds = 1000).hash("abc123")

print(hashedPassword)

# while True:
#     password = input("Enter your password: ")
#
#     if mysql323.verify(password, hashedPassword):
#         print("That is your password. Welcome!")
#         break
#     else:
#         print("That's not your password... please try again. \n")
