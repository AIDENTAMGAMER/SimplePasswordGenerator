import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqr}stuvwxyz1234567890`!@#$%^&*(){_+|:<>?"

while 1:
    password_len = int(input("How many characters do your passwords need to be? : "))
    password_count =int(input("How many password(s) would you like? : "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(chars)
            password      = password + password_char

        print ("Here's your password(s): ", password)
