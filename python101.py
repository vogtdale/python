#!/bin/python3

#print strings
print("strings and things")
print("Hellow world")

#print multi lines
print("""Hellow this is
a multi-line string!""")

#Concatenation
print("this is"+" a string")

#new line
print('\n')

#Variables and Metodes
quote = "This is a quote"
print(len(quote)) #length
print(quote.upper())
print(quote.lower())
print(quote.title())

name = "Bob"
age = 18
print("My name is " + name + " and i'm " + str(age) + " years old")
print('\n')

#Functions 
print("""===========
 Fuctions 
===========""")
def whoAmI():
	name = "john"
	age = 23
	print("My name is " + name + " and i'm " + str(age) + " years old")
whoAmI()
print('\n')

#add parameters 
def add(x,y):
	print(x+y)
x = 1
y = 2
add(x,y) 

#use A return statement to return a value or something 
def multiply(x,y):
	return x*y

print(multiply(1,3))


#userInput
def getUserInput(name, age):
	print("My name is " + name + " and i'm " + str(age) + " years old")


name = input("Hellow please enter your name ?: " + '\n')
age = input("How old are you " + name + ":" +  '\n')
getUserInput(name, age)
	




