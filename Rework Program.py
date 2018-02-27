#Connor J
#15/06/2017
#New System for Data Structures

################################################################# Start of Program #################################################################
Choice=""
x=0
quecount = 0

import base64 #Encryption
from pprint import pprint #Display
from codecs import encode
import sys
from random import randint

################################################################# Stack Section #################################################################
class Person:

    def __init__(self, ID, fname, lname, password, memorableword):
        self.ID = ID
        self.fname = fname
        self.lname = lname
        self.password = password
        self.memorableword = memorableword
		
def fullname(self):
    return "%s %s" % (self.fname, self.lname)
	
	
People=[]


        #getattr(myobject, "a")
        #means same as myobject.a

def Push():        

        
        
        ID2=input("Please enter the person's ID: ")
        fname2=input("Please enter the person's First Name: ")
        lname2=input("Please enter the person's Last Name: ")
        password2=input("Please type in a Password: ")
        memorableword2=input("Please enter a memorable word: ")

        memwordseperate = list(memorableword2)

        memorablewordlength=len(memwordseperate)-1

        num1 = randint(0, memorablewordlength)
        num2 = randint(0, memorablewordlength)
        num3 = randint(0, memorablewordlength)
        
        print("A letter has been chosen from your memorable word: " , memwordseperate[num1])
        print("A letter has been chosen from your memorable word: " , memwordseperate[num2])
        print("A letter has been chosen from your memorable word: " , memwordseperate[num3])
    
        
        EditPassword=""
        EncryptedPass=""
        #Create empty Variables
        EditPassword=password2
        #Get password attribute from self and store in a variable

        #EncryptedPass = encode(EditPassword, "base64")

        EncryptedPass = password2[::-2]

        #use base64 encryption for the variable EditPassword and store it into variabled Encrypted Pass
        print("Password has been encrypted to: " , EncryptedPass , " original password was: " , EditPassword)
        #Print message showing encrypted password compared to original password using decoding to display it

        password2=EncryptedPass
        
        person=Person(ID=ID2,fname=fname2,lname=lname2,password=password2,memorableword=memorableword2)
        #Inconsistent indent    

        #person is a variable of the object Person with the values being set in the initialiser using the input statements above   
        print("ID: ", person.ID)
        print("First Name: ", person.fname)
        print("Last Name: ", person.lname)
        print("Password: ", person.password)
        print("Memorable Word: ", person.memorableword)
        #Testing the results of the previous inputs
        
        People.insert(0,person)
        
        #Inserts the person into index 0 in the stack called "Stack"  
        print("Inserted details successfully!")
        Stack()
            
        #Meant to initialise the password encryption 
def Pop():

    #check if length of stack is = to 0 (empty) if it is then print out there's no-one to remove
    Length=len(People)
    
    if(Length == 0):
        print("There are no people in the stack to remove!")
    else:
        #Else, if it's not empty then pop the last one off
        print("Element Deleted from Stack!")
        People.pop()
        
        Stack()
    #Go back to menu
        
def Display():
    #Check if length of stack is equal to 0 (empty)
    Length=len(People)
    
    if(Length == 0):
        print("Can't display stack as it is empty!")
    elif(Length >= 1):
        i = 0
        while i < Length:
            print(People[i])
            i += 1
    
def Stack():
    StackChoice=""
    print("""

         ________________________
        |                        |
        |                        |
        |         Stack          |
        |                        |
        |       1. Push          |
        |       2. Pop           |
        |    3. Display Stack    |
        |                        |
        |      0. Main Menu      |     
        |                        |
        |________________________|

          """)
    StackChoice=int(input("Please choose an option: "))
    if(StackChoice==1):
        Push()
    elif(StackChoice==2):
        Pop()
    elif(StackChoice==3):
                Display()
    elif(StackChoice==0):
        Menu()
    else:
        print("Not an option!")
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Stack Menu ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^







#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv Queue Menu vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

class Person:
    
    People = []
    
    def __init__(self, ID, fname, lname, password, memorableword):

        self.ID = ID
        self.fname = fname
        self.lname = lname
        self.password = password
        self.memorableword = memorableword
            
    def fullname(self):
        
        return "%s %s" % (self.fname, self.lname)
        
Queue=[]



    #Open Stack Menu again
def Enqueue():        
        
        global quecount
        
        ID2=input("Please enter the person's ID: ")
        fname2=input("Please enter the person's First Name: ")
        lname2=input("Please enter the person's Last Name: ")
        password2=input("Please type in a Password: ")
        memorableword2=input("Please enter a memorable word: ")

        memwordseperate = list(memorableword2)

        memorablewordlength=len(memwordseperate)-1

        num1 = randint(0, memorablewordlength)
        num2 = randint(0, memorablewordlength)
        num3 = randint(0, memorablewordlength)
        
        print("A letter has been chosen from your memorable word: " , memwordseperate[num1])
        print("A letter has been chosen from your memorable word: " , memwordseperate[num2])
        print("A letter has been chosen from your memorable word: " , memwordseperate[num3])

        EditPassword=""
        EncryptedPass=""
        #Create empty Variables
        EditPassword=password2
        #Get password attribute from self and store in a variable

        #EncryptedPass = encode(EditPassword, "base64")

        EncryptedPass = EditPassword[::2] 

        #use base64 encryption for the variable EditPassword and store it into variabled Encrypted Pass
        print("Password has been encrypted to: " , EncryptedPass , " original password was: " , EditPassword)
        #Print message showing encrypted password compared to original password using decoding to display it
        
        person=Person(ID=ID2,fname=fname2,lname=lname2,password=password2,memorableword=memorableword2)  
        #person is a variable of the object Person with the values being set in the initialiser using the input statements above   
        print("ID: ", person.ID)
        print("First Name: ", person.fname)
        print("Last Name: ", person.lname)
        print("Password: ", person.password)
        print("Memorable Word: ", person.memorableword)
        Last=quecount
        Queue.insert(Last,person)
        
        quecount += 1
        
	#Inserts the person into the last element of the queue
        print("Inserted details successfully!")

def Dequeue():	
	#check if length of Queue is = to 0 (empty) if it is then print out there's no-one to remove
	if(len(Queue) == 0):
		print("There are no people in the Queue to remove!")
	else:
		#Else, if it's not empty then pop the first one off
		Queue.pop(0)
		print("Removed the first person from the queue!")	
	Menu()
	#Go back to menu
def Displayqueue():	
	#Check if length of Queue is equal to 0 (empty)
	if(len(Queue) == 0):
		print("Can't display Queue as it is empty!")
	else:
	#If it's not, for each index in the Queue, v is each element
	    pprint("Memory Location: ",Queue)
	    print(person.ID)
	    print(person.fname)
	    print(person.lname)
	    print(person.password)
	    print(person.memorableword)
		#for i, v enumerate(Stack):
		#	print(i,v)
		#Meant to display each record in the Queue and the index of that person in the Queue      
def QueueMenu():
    QueueChoice=""    
    print("""

         ________________________
        |                        |
        |         Queue          |
        |                        |
        |       1. EnQueue       |
        |       2. DeQueue       |
        |    3. Display Queue    |
        |                        |
        |      0. Main Menu      |     
        |________________________|

          """)
    QueueChoice=int(input("Please choose an option: "))
    if(QueueChoice==1):
        Enqueue()
    elif(QueueChoice==2):
        Dequeue()
    elif(QueueChoice==3):
        Displayqueue()
    elif(QueueChoice==0):
        Menu()
    else:
        print("Not an option!")
################################################################# Main Menu Section #################################################################
def Menu():
    print("""

         ________________________
        |                        |
        |                        |
        |       Main Menu        |
        |                        |
        |       1. Stack         |
        |       2. Queue         |
        |                        |
        |       0. Close         |     
        |                        |
        |________________________|
          """)
    Choice=int(input("Please choose an option: "))
    if(Choice==1):
        Stack()
    elif(Choice==2):
        QueueMenu()
    elif(Choice==0):
        quit()
    else:
        print("Not an option!")
        
while x==0:
    Menu()
