"""
Exception Handling Exercise

Create a dictionary car
create 3 keys
#make
#model
#year

Try to access the color key. remember, we never created the color key,
so it's going to throw an exception. You need to handle the exception
using the try, except and finally block.
"""
def exceptionhandling():
    try:
        car={"make":"bmw", "model":"550i", "year": "2022"}
        print(car["color"])
    except:
        print("In the except block, Key not found")
    else:
        print("Because there was no exception, else is executed")
    finally:
        print("Finally always executed, Please try a different key")



exceptionhandling()
