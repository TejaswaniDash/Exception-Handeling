"""
Exceptions are errors
we should handle exceptions in our code
to make sure the code is working the way we want and is handling all the unwanted issues
Link to 3.5 built-in exceptions- https://docs.python.org/3/library/exceptions.html
"""

#create a method

def exceptionhandling():
    a = 10
    b = 20
    c = 10

    d = ( a + b) / c

    print(d)

#let's say imagine that we don't know the value of these variables
#they might get changed during the program where we are assigning some value to some other variable
#to a different variable we are assigning a different value where these values might change

#let's say

   # a = 10
  #  b = 20
    #c = 0

    #d = ( a + b) / c

   # print(d)
#exceptionhandling()

#in above we will get an error "ZeroDivisionError: division by zero"
#let's say we enter string

#def exceptionhandling():
#    a = 10
 #   b = "any string"
 #   c = 10

 #   d = ( a + b) / c

   # print(d)

#exceptionhandling()

#in above we will get an error "TypeError: unsupported operand type(s) for +: 'int' and 'str'"

#HOW do we handle these exceptions?

#we use the try and except

def exceptionhandling():
   try:
       a = 10
       b = "any string"
       c = 10

       d = ( a + b) / c

       print(d)
   except:
       print("In the except block, this is not possible")

exceptionhandling()

print("*"*40)

def exceptionhandling():
   try:
       a = 10
       b = 20
       c = 0

       d = ( a + b) / c

       print(d)
   except:
       print("In the except block, this is not possible")

exceptionhandling()

print("*"*60)

# let's say we have both the issue "string" and "divided by 0"
#when we have multiple Error
def exceptionhandling():
   try:
       a = 10
       b = "any string"
       c = 0

       d = ( a + b) / c

       print(d)
   except ZeroDivisionError:
       print("Zero Division Error")
   except TypeError:
       print("Can't add string to integer")
#when we run we will get "Can't add string to integer" as output
# because the first incounter of error is string
#skipped "Zero Division Error" because this happening afterward and the first error is string

exceptionhandling()

print("*"*60)

# Example 2
#when we have multiple Error
def exceptionhandling():
   try:
       a = 10
       b = 20
       c = 0

       d = ( a + b) / c

       print(d)
   except ZeroDivisionError:
       print("Zero Division Error")
   except TypeError:
       print("Can't add string to integer")

exceptionhandling()

print("*"*60)

#Example 3
#we don't prefer to mention so many excepts , what we usualy do is:

def exceptionhandling():
   try:
       a = 10
       b = 20
       c = 0

       d = ( a + b) / c

       print(d)
   #except ZeroDivisionError:
   #    print("Zero Division Error")
   #except TypeError:
    #   print("Can't add string to integer")
   except:
       print("In the except block")


exceptionhandling()



