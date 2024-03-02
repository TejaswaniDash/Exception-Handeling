#let's say there is no error and everything is fine
#let's see else block

def exceptionhandling():
   try:
       a = 10
       b = 20
       c = 10

       d = ( a + b) / c

       print(d)
   except:
       print("In the except block")
   else:
       print("Because there was no exception, else is executed")

#only and only if there is no exception,
# then this elif block, else block is going to execute


exceptionhandling()

print('*'*40)

#let's assume that there is an exception

def exceptionhandling():
   try:
       a = 10
       b = 20
       c = 0

       d = ( a + b) / c

       print(d)
   except:
       print("In the except block")
   else:
       print("Because there was no exception, else is executed")

exceptionhandling()

print('*'*40)

#let's see Finally block when there is no exception

def exceptionhandling():
   try:
       a = 10
       b = 20
       c = 10

       d = ( a + b) / c

       print(d)
   except:
       print("In the except block")
   else:
       print("Because there was no exception, else is executed")
   finally:
       print("finally, always executed")
#Finally  block is really useful when you have some cleanup in your code,
# whether you want to close the database connections,
# or you have some files open, you want to close the files,
# and or you want to clean up any other thing that in your code you have opened previously,
# any other network connections
# or something that you definitely want to close them in the finally block,
# so you don't leave any connections open,
# so it just saves the memory leak and all those sorts of different things
exceptionhandling()


print('*'*40)

#Exmple2
#let's see Finally block when there is exception

def exceptionhandling():
   try:
       a = 10
       b = 20
       c = 0

       d = ( a + b) / c

       print(d)
   except:
       print("In the except block")
   else:
       print("Because there was no exception, else is executed")
   finally:
       print("finally, always executed")

exceptionhandling()

print('*'*40)

#Exmple3
#let's see Finally block when there is exception

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
   else:
       print("Because there was no exception, else is executed")
   finally:
       print("finally, always executed")

exceptionhandling()

print("*"*40)

#RAISE KEYWORD

#raise' is the keyword that when we have any exception,
# and we could not handle it properly

def exceptionhandling():
   try:
       a = 10
       b = 20
       c = 0

       d = ( a + b) / c

       print(d)
   except:
       print("In the except block")
       raise Exception("This is an exception")
       #to see all the stack trace to debugg the code nicely
   else:
       print("Because there was no exception, else is executed")
   finally:
       print("finally, always executed")

exceptionhandling()


