#!/usr/bin/env python3

phrase1="hello world"
phrase2="top spot"

def is_palindrome(string):
    clean_string=string.replace(" ","")
    ans = (clean_string == clean_string[::-1])
    
    if ans:
        print(string,":", "Yes")
    else:
        print(string,":", "No")


is_palindrome(phrase1)
is_palindrome(phrase2)
