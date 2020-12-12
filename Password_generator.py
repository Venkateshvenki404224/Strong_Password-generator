#!/bin/python3
from random import randint
small='qwertyuiopasdfghjklzxcvbnm'
large=small.upper()
symbols='!£$%^&_-+=;:><?*()'
numbers='1234567890'
pass_word=small+large+symbols+numbers
pass_length=int(input("Enter the Password Length You want:"))
password="\n"
length=0
if pass_length<8:
	print("The Mininmum length of Password Should be 8:")
else:		
	while length < pass_length:
		password=password+pass_word[randint(0,len(pass_word)-1)]
		length +=1
	print('Generated password is:',password)
	#Creating a file name called Password 
f = open("Password.txt","a")
f.write(password)#Writing the file 
f.close()
f = open("Password.txt", "r+")
print(f.read())
