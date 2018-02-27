#Connor Jolley
#Stack Data Structure
#22/04/2017
#Assignment 2 Data Structures

#Imported system to terminate the program when an option is selected using sys.exit(0)
import sys

#Name of List used for the stack
MyStack = []

#For a user entered value to be added to stack
ValueToAdd=''



#Predefined max size of the Stack
StackSize = 5

x=0;
#Starts the program in the main menu


y=0

#Created classes for the different data structures, stack and queue to seperate them
class Queue:
        #Defined functions that can be recalled / accessed throghout the system using the main menu
        def Close():
            sys.exit(0)
            #Closes the program

        #Initiates the q=Queue() function called earlier, creating the queue, using q as "self" attaching items to the queue
        def __init__(self):
            self.items = []

        #Enqueue, user enters data that will then be inserted to the data position 0 in the queue
        def Enqueue(self, item):
            self.items.insert(0,item)

        #Dequeue, removes / pops the value from the queue
        def Dequeue(self):
            return self.items.pop()

        #Displays the length of the Queue
        def LengthQueue(self):
            return len(self.items)
            
        def QueueMenu():
            Choice2=int(input("""


                     _________________________________________
                    |                 [Queue]                 |
                    |                                         |
                    |         1. Enqueue                      |
                    |         2. Dequeue                      |
                    |         3. Display Queue                |
                    |         4. Display Length of Queue      |
                    |                                         |
                    |                                         |
                    |         9. Stack Menu                   |
                    |         10. Close Program               |
                    |_________________________________________|

                    Please Select an Option: 
                            """))
            if(Choice2==1):
                Enqueue()
            elif(Choice2==2):
                Dequeue()
            elif(Choice2==3):
                DisplayQueue()
            elif(Choice2==4):
                LengthQueue()
            elif(Choice2==9):
                return
            elif(Choice2==10):
                Close()

        QueueMenu()
#Defined functions that can be recalled / accessed throghout the system using the main menu
def DisplayStack():
    print("Stack currently contains:")

    #For statement will repeat the following actions for each element / "Item" in the stack 
    for Item in MyStack:

        #Tried to perform a check if it's empty first so it doesn't yield an empty result
        if(Item==''):
            print("Stack is empty!")
        else:
            print(Item)


            

#Defined functions that can be recalled / accessed throghout the system using the main menu
def Push(Value):
#First checks if the length of the stack is less than the stack size (5 by default)
 if len(MyStack) < StackSize:
     #If it is less than the stack max size it then follows the next 2 actions before the else
  MyStack.append(Value)
  #appends the value onto the stack (Value is assigned through the PushFunction where it uses the Push(ValueToAdd)
  print("Successfully Inserted ", Value , " onto the stack!")
  #Success Message
 else:
  #This stack is full message was there in-case the pre-check if the stack is full fails.
  print("Stack is full!")


  

#Defined functions that can be recalled / accessed throghout the system using the main menu
def Pop():
#if the length of the stack is greater than 0 then it'll follow the next 5 actions before the else
 if len(MyStack) > 0:
  #Stores the last element of the stack into LastElement variable (-1) as it's a list like structure, so values start at 0 like arrays)
  LastElement = len(MyStack)-1
  #Stores this into PoppingValue variable for use in a print action
  PoppingValue=MyStack[LastElement]
  print("Popping the value: " , PoppingValue , " off the stack!")
  #Pops value off the stack
  MyStack.pop()
  print(PoppingValue , " has been successfully popped off the stack!")
  #Success Message
 else:
  print("Stack is empty.")
  #Displays the stack as being empty




  
#Defined functions that can be recalled / accessed throghout the system using the main menu
def PushFunction():
    #Checks if the length of the stack is less than the max size
    if len(MyStack) < StackSize:
        #if it is, it will follow the next 4 steps
        ValueToAdd=int(input("Please enter a number to insert into the stack: "))
        #Allows user to enter a value themselves to store
        print("You wanted to add: " , ValueToAdd , " onto the Stack")
        #Displays their choice
        Push(ValueToAdd)
        #Passes the value to add data into the Push function predefined earlier in the program
        StackMenu()
        #Calls for the MainMenu function again, continuing the loop
    elif len(MyStack) >= StackSize:
        #If the stack length exceeds the max size (which it shouldn't ever) it will display an error
        print("The Stack is Currently full, please pop a value off before trying to push!")





#Defined functions that can be recalled / accessed throghout the system using the main menu
def MaxSize():
    print("The max size of the stack is predefined to be: " , StackSize ,".")
    #Displays max size of the stack




#Defined functions that can be recalled / accessed throghout the system using the main menu
def StackLength():
    StackLength=len(MyStack)
    #Gets the length of the stack and displays a message containing the length
    print("The Current Size of the Stack is: " , StackLength , ".")




#Defined functions that can be recalled / accessed throghout the system using the main menu
def Close():
    sys.exit(0)
    #Closes the program




#Defined functions that can be recalled / accessed throghout the system
def StackMenu():
    #Choice variable is integer input as it uses numerical values for options, 3 " marks to enable multiline prints to present the program better
    Choice=int(input("""


         _________________________________________
        |                 [STACK]                 |
        |                                         |
        |         1. Push                         |
        |         2. Pop                          |
        |         3. Display Stack                |
        |         4. Display Length of Stack      |
        |         5. Display Max Size of Stack    |
        |                                         |
        |                                         |
        |         9. Queue Menu                   |
        |         10. Close Program               |
        |_________________________________________|

        Please Select an Option: 
                """))
        
                 


    #If statement, followed by elifs for each of the different choices, when a choice is made and matches, the program reffers to the predefined functions earlier in the program, such as PushFunction()
    if(Choice==1):
        PushFunction()
    elif(Choice==2):
        Pop()
    elif(Choice==3):
        DisplayStack()
    elif(Choice==4):
        StackLength()
    elif(Choice==5):
        MaxSize()
    elif(Choice==10):
        Close()
    elif(Choice==9):
        return
        Queue()

    #Was meant to prevent an error from occuring when the user clicks enter on this section without typing anything
    elif(Choice==''):
        print("Value entered was not a number / option!")

#What initites the program and causes the endless loop only closable by the close function from the main menu
while x == 0:
    StackMenu()

    
