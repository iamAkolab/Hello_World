def spam():
    global eggs #tells the functions that eggs should be a global variable
    eggs = "hello"
    print(eggs)

eggs = 42 #Global scope
spam()
print(eggs)

def  div42by(numbertodivby):
    """Divide 42 by the given numberCount in `content`.
     
      Args:
        numbertodivby (int): The number to divide by.

     Returns:
        int
  
     # Add a section detailing what errors might be raised
  
     Raises:
       ValueError: If `numbertodivby` is not int or floay.
    """
  
    try:
        return 42 / numbertodivby
    except ZeroDivisionError:
        print("You tried to divide by zero")

print(div42by(42))
print(div42by(21))
print(div42by(0))
print(div42by(12))
print(div42by(4))

