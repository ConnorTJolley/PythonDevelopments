#Connor Jolley
#Vending Machine Program
#24/1/2014

import time

Change = 0
Balance = 0
Machine_Balance = 50
Deposit_Ammount = 0
Withdraw_Ammount = 0

Cold_Sold = 0
Hot_Sold = 0

Cold_Cost = 0.50
Hot_Cost = 0.75

Hot_Proffit = Hot_Sold * Hot_Cost
Hot_Proffit=int(Hot_Proffit * 100) / 100.0

Cold_Proffit = Cold_Sold * Cold_Cost
Cold_Proffit=int(Cold_Proffit * 100) / 100.0

C1_Stock = 50
C2_Stock = 50
C3_Stock = 50
H1_Stock = 50
H2_Stock = 50
H3_Stock = 50

Cost_Cold = 0.22
Cost_Hot = 0.35



while True:

    CMD = 0
    Money_Needed_Left = 0
    Money_Needed = 0
    Choice = ""
    
    Stock_Check = ""
    Stock_Select = ""
    Stock_Add = 0

    print("""
         __________________________________________________________
        |                                                          |
        |           _Widget Drinks_ Drink Despencer!               | 
        |                                                          |
        |                                                          |
        |            Cold Drinks!             Hot Drinks!          |
        |                                                          |
        |        C1. WD Coca Cola £0.50  H1. WD Tea £0.75          |
        |        C2. WD Die Cola £0.50   H2. WD Coffee £0.75       |
        |        C3. WD Orange £0.50     H3. WD Chocolate £0.75    |
        |                                                          |
        |                                                          |
        |                         F1. Help!                        |
        |                         F2. Manual!                      |
        |__________________________________________________________|

         """)

    Choice=input("Please select an item: ")
    if Choice == "c1" or Choice == "C1":
        Balance=float(input("Please Insert £0.50 -- £"))
        if Balance == Cold_Cost:
            time.sleep(1)
            print("""
                 _________________________
                |                         |
                |Please collect your item.|
                |_________________________| 

                """)


            C1_Stock -= 1
            Cold_Sold += 1
            time.sleep(1)

        elif Balance > Cold_Cost:
            Change = Balance - Cold_Cost
            Change=int(Change * 100) / 100.0
            print("Your change is £", Change,"Please collect your Item!")
            Machine_Balance += Balance - Change
            Change=int(Change * 100) / 100.0
            C1_Stock -= 1
            Cold_Sold += 1
            time.sleep(1)

        elif Balance < Cold_Cost:
            Money_Needed = Cold_Cost - Balance
            Money_Needed_Left = Money_Needed_Left + Money_Needed
            Money_Needed_Left=int(Money_Needed_Left * 101) / 100.0
            print("You need to insert £", Money_Needed_Left,"then you can recieve your item")
            time.sleep(1)
            

    elif Choice == "c2" or Choice == "C2":
        Balance=float(input("Please Insert £0.50 -- £"))
        if Balance == Cold_Cost:
            time.sleep(1)
            print("""
                 _________________________
                |                         |
                |Please collect your item.|
                |_________________________| 

                """)


            C2_Stock -= 1
            Cold_Sold += 1
            time.sleep(1)

        elif Balance > Cold_Cost:
            Change = Balance - Cold_Cost
            Change=int(Change * 100) / 100.0
            print("Your change is £", Change,"Please collect your Item!")
            Machine_Balance += Balance - Change
            C2_Stock -= 1
            Cold_Sold += 1
            time.sleep(1)

        elif Balance < Cold_Cost:
            Money_Needed = Cold_Cost - Balance
            Money_Needed_Left = Money_Needed_Left + Money_Needed
            Money_Needed_Left=int(Money_Needed_Left * 101) / 100.0
            print("You need to insert £", Money_Needed_Left,"then you can recieve your item")
            time.sleep(1)


    elif Choice == "c3" or Choice == "C3":
        Balance=float(input("Please Insert £0.50 -- £"))
        if Balance == Cold_Cost:
            time.sleep(1)
            print("""
                 _________________________
                |                         |
                |Please collect your item.|
                |_________________________| 

                """)


            C3_Stock -= 1
            Cold_Sold += 1
            time.sleep(1)

        elif Balance > Cold_Cost:
            Change = Balance - Cold_Cost
            Change=int(Change * 100) / 100.0
            print("Your change is £", Change,"Please collect your Item!")
            Machine_Balance += Balance - Change
            C3_Stock -= 1
            Cold_Sold += 1
            time.sleep(1)

        elif Balance < Cold_Cost:
            Money_Needed = Cold_Cost - Balance
            Money_Needed_Left = Money_Needed_Left + Money_Needed
            Money_Needed_Left=int(Money_Needed_Left * 101) / 100.0
            print("You need to insert £", Money_Needed_Left,"then you can recieve your item")
            time.sleep(1)


    elif Choice == "h1" or Choice == "H1":
        Balance=float(input("Please Insert £0.75 -- £"))
        if Balance == Hot_Cost:
            time.sleep(1)
            print("""
                 _________________________
                |                         |
                |Please collect your item.|
                |_________________________| 

                """)


            H1_Stock -= 1
            Hot_Sold += 1

            time.sleep(1)

        elif Balance > Hot_Cost:
            Change = Balance - Hot_Cost
            Change=int(Change * 100) / 100.0
            print("Your change is £", Change,"Please collect your Item!")
            Machine_Balance += Balance - Change
            H1_Stock -= 1
            Hot_Sold += 1
            time.sleep(1)

        elif Balance < Hot_Cost:
            Money_Needed = Cold_Cost - Balance
            Money_Needed_Left = Money_Needed_Left + Money_Needed
            Money_Needed_Left=int(Money_Needed_Left * 101) / 100.0
            print("You need to insert £", Money_Needed_Left,"then you can recieve your item")
            time.sleep(1)


    elif Choice == "h2" or Choice == "H2":
        Balance=float(input("Please Insert £0.75 -- £"))
        if Balance == Hot_Cost:
            time.sleep(1)
            print("""
                 _________________________
                |                         |
                |Please collect your item.|
                |_________________________| 

                """)


            H2_Stock -= 1
            Hot_Sold += 1
            time.sleep(1)

        elif Balance > Hot_Cost:
            Change = Balance - Hot_Cost
            Change=int(Change * 100) / 100.0
            print("Your change is £", Change,"Please collect your Item!")
            Machine_Balance += Balance - Change
            H2_Stock -= 1
            Hot_Sold += 1
            time.sleep(1)

        elif Balance < Hot_Cost:
            Money_Needed = Cold_Cost - Balance
            Money_Needed_Left = Money_Needed_Left + Money_Needed
            Money_Needed_Left=int(Money_Needed_Left * 101) / 100.0
            print("You need to insert £", Money_Needed_Left,"then you can recieve your item")
            time.sleep(1)


    elif Choice == "h3" or Choice == "H3":
        Balance=float(input("Please Insert £0.75 -- £"))
        if Balance == Hot_Cost:
            time.sleep(1)
            print("""
                 _________________________
                |                         |
                |Please collect your item.|
                |_________________________| 

                """)


            H3_Stock -= 1
            Hot_Sold += 1
            time.sleep(1)

        elif Balance > Hot_Cost:
            Change = Balance - Hot_Cost
            Change=int(Change * 100) / 100.0
            print("Your change is £", Change,"Please collect your Item!")
            Machine_Balance += Balance - Change
            H3_Stock -= 1
            Hot_Sold += 1
            time.sleep(1)

        elif Balance < Hot_Cost:
            Money_Needed = Cold_Cost - Balance
            Money_Needed_Left = Money_Needed_Left + Money_Needed
            Money_Needed_Left=int(Money_Needed_Left * 101) / 100.0
            print("You need to insert £", Money_Needed_Left,"then you can recieve your item")
            time.sleep(1)

    
    if Choice == "f1" or Choice == "F1":
            print("""
                          ____________________________________
                         |                                    |
                         |          Instructions.             |
                         |                                    |
                         | To use the program                 |
                         | you have to make a selection       |
                         | of what item you want to buy       |
                         | an example is (C1), then you       |
                         | click Enter and then input your    |
                         | money, like so (1.00)              |
                         |                                    |
                         |                                    |
                         |____________________________________|
                    
                      """)
            input("Press Enter to continue: ")

    elif Choice == "f2" or Choice == "F2":
            print("""
                          ______________________________________
                         |                                      |
                         |              Manual.                 |
                         |                                      |
                         |  The drinks dispenser comes with     |
                         |  a control panel that allows you     |
                         |  to execute different commands that  |
                         |  will alter the dispenser, you can   |
                         |  input money to be used for change   |
                         |  for when people have entered too    |
                         |  much money for the item, you can    |
                         |  also check stock, profit and other  |
                         |  variables, to get onto this control |
                         |  panel, there is a password in the   |
                         |  box that comes with the machine,    |
                         |  you enter the password on the       |      
                         |  select item screen.                 |
                         |______________________________________|
                         """)
            input("Press Enter to continue: ")

            time.sleep(1)

    elif Choice == "ZNt":
        print("""
         __________________________________________________________
        |                                                          |
        |                   Control Panel                          | 
        |                                                          |
        |                1. Show Machine Balance                   |
        |                2. Top-Up Machine Balance                 |
        |                3. Withdraw Machine Balance               |
        |                4. Show Stock of an Item                  |
        |                5. Add Stock of an Item                   |
        |__________________________________________________________|

         """)
        CMD=int(input("What command would you like to execute: "))
        if CMD == 1:
            print(Machine_Balance)
            time.sleep(2.5)

        elif CMD == 2:
            Deposit_Ammount=float(input("Enter amount to deposit: £"))
            time.sleep(1.5)
            Machine_Balance += Deposit_Ammount
            print("The new machine balance is: £", Machine_Balance)
            time.sleep(2.5)

        elif CMD == 3:
            Withdraw_Ammount=float(input("Enter amount to withdraw: £"))
            time.sleep(1.5)
            Machine_Balance -= Withdraw_Ammount
            print("The new machine balance is: £", Machine_Balance)
            time.sleep(0.3)
            input("Press Enter to restart: ")
            time.sleep(2)

        elif CMD == 4:
            Stock_Check=input("Select an item to view stock, C1-C3 or H1-H3: ")

            if Stock_Check == "a1" or Stock_Check == "A1":
                time.sleep(1)
                print("WD Cola stock is", A1_Stock)

            elif Stock_Check == "a2" or Stock_Check == "A2":
                time.sleep(1)
                print("WD Diet Cola stock is", A2_Stock)

            elif Stock_Check == "a3" or Stock_Check == "A3":
                time.sleep(1)
                print("WD Orange stock is", A3_Stock)

            elif Stock_Check == "a4" or Stock_Check == "A4":
                time.sleep(1)
                print("WD Tea stock is", A4_Stock)

            elif Stock_Check == "a5" or Stock_Check == "A5":
                time.sleep(1)
                print("WD Coffee stock is", A5_Stock)

            elif Stock_Check == "a6" or Stock_Check == "A6":
                time.sleep(1)
                print("WD Chocolate stock is", A6_Stock)

        elif CMD == 5:
                Stock_Select=input("Please select the item you want to add stock too from C1-C3 or H1-H3: ")
                if Stock_Select == "c1" or Stock_Select == "c1":
                    time.sleep(0.5)
                    Stock_Add = int(input("Please enter the amount you are adding: "))

                    if C1_Stock + Stock_Add <= 50:
                        C1_Stock += Stock_Add
                        print("The stock has been updated... The stock is now ", C1_Stock, "/ 50.")

                    else:
                        Stock_Used = 50-A1_Stock
                        print("Error: You can only add ", Stock_Used, " more. The stock is currently ", C1_Stock, "/ 50.")

                elif Stock_Select == "c2" or Stock_Select == "C2":
                    time.sleep(0.5)
                    Stock_Add = int(input("Please enter the amount you are adding: "))

                    if C2_Stock + Stock_Add <= 50:

                        
                        C2_Stock += Stock_Add
                        print("The stock has been updated... The stock is now ", C2_Stock, "/50.")

                    else:

                        Stock_Used = 50-C2_Stock
                        print("Error: You can only add ", Stock_Used, " more. The stock is currently ", C2_Stock, "/ 50.")

                        

            

            

            
                
        
        
        
        


        
                
