
Array = [];

top = 0;


while True:
    User_Choice = input("Please type /push to push a number onto the array or /pop to remove a number from the array: ")
    if User_Choice == "/push" or User_Choice == "/PUSH":
    
        Number_Push = int(input("Please type a number to push: "))
        if Number_Push =< 0:
            print("Number can't be 0!");
        else:
            Array.append(Number_Push);
            print("The address in the array is: " , top , "the value in address is: " , Array[top]);
            print("""

              """)
            print("The top of the array is" , top);
            top +=1;

        
    elif User_Choice == "/pop" or User_Choice == "/POP":
            top-=1;
            print("""

                  """)
            print("The number being popped off the array is: " , Array[top]);
            print("The top of the array is" , top);

        
            

        
    
