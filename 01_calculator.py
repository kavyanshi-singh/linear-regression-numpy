calc=input("What operation? ")


     
match calc:
      case "+":
           x=int(input("What's x? "))
           y=int(input("What's y? "))

           z=x+y
           print(z)

      case "-":
           x=int(input("What's x? "))
           y=int(input("What's y? ")) 

           z=x-y
           print(z)

      case "*":
           x=int(input("What's x? "))
           y=int(input("What's y? "))

           z=x*y
           print(z)
     
      case "/":
           x=int(input("What's x? "))
           y=int(input("What's y? "))

           z=x/y
           print(z) 
      case _:
            print("Not Valid")
