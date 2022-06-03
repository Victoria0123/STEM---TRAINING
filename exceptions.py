while (1):
  try:
    x=int(input("Please enter the first number:"))
    y=int(input("Please enter the second number:"))

    z=x/y
    print(z) 
  except ZeroDivisionError:
    print("cannot divide by zero")
    continue
  except ValueError:
    print("You did not enter an integer")
    continue
  else:
    print(z)  
    break
  finally:
    print("This program ends here")          
     