def convert(number):
    number = (int(input("Type the Number: ")))
    
    if (number % 3 == 0 and number % 5 == 0 and number % 7 ==0):
       return print('PlingPlangPlong')
    else: 
       if (number % 3 == 0 and number % 5 == 0):
           return print("PlingPlang")
       elif (number % 3 == 0 and number % 7 == 0):
           return print("PlingPlong")
       elif(number % 5 == 0 and number % 7 == 0):
           return print("PlangPlong")
       else:
           if(number % 3 == 0):
               return print("Pling")
           elif(number % 5 == 0):
               return print("Plang")
           elif(number % 7 == 0):
               return print("Plong")
           else: 
               return print(number)
   
    
        
    
