tasks=["Wake up", "Go  to gym", "Attend classes", "Hangout with friends", "Study at night"]
while True:
   x=input("What do you want to do? ")

   match x:
      case "Add1":
            y=input("What tasks to add? ")
            if y in tasks:
               tasks.append(y)
               print(tasks)
      
      case "Add2":
            w="Have breakfast"
            tasks.insert(1,w)
            print(tasks)
      
      case "View":
            for task in tasks:
               print("-", task)
      
      case "Remove":
            z=input("Which tasks to remove? ")
            if z in tasks:
               tasks.remove(z)
               print(tasks)
      
      case _:
            print("Invalid option")
          
            
           
            
            
            
      
 