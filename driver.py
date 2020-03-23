from checkingAccount import *

def main():
    #making a list for the accounts created. 
    acctList =  list()
    print("Create an account and don't forget to input the amount with two decimal places for the balance.")
    #Looping to get input from the user.
    while True:
        try:
            fname = input('\tFirst Name : ')
            lname = input('\tLast Name : ')
            streetAddress = input('\tStreet Address : ')
            city = input('\tCity : ')
            state = input('\tState : ')
            zipCode = input('\tZip Code : ')
            accountNumber = input('\tAccount Number : ')
            balance =  input('\tBeginning Balance : ')
            #appending all created objects to the list.
            acctList.append(CheckingAccount(fname, lname, streetAddress, city,
                                        state, zipCode, accountNumber, balance))
            #Checking to continue to make new objects
            contLoop = input("Would you like to create another account? Yes to continue, or press any key and/or enter to quit.")
            if contLoop == "Yes":
                continue
            else:
                 break
                
        except ValueError:
            print("Input not successful.\nPlease enter amount with two decimal places!")
    #printing the objects created.
    print('Accounts Information')
    print('Account Number\t\tFirst Name\t\tLast Name\t\tBalance')
    for i in range(len(acctList)):
        acctList[i].printData()
        
    #Modifying balance
    while True:
        cont = input("Would you like to do another transaction? (Yes or press any key and enter to quit) ")
        
        if cont == "Yes":
            pass
        else:
            break
        #selecting an object to modify.   
        ind = int(input("Please select account to modify from 1 to {} ".format(len(acctList))))
        #options for transactions - deposit, withdrawal, and change of name.
        opt = input("What would you like to do? Enter 1 - to Deposit, 2 - Withdraw 3 - to Change Name ")
        ind = ind - 1
        if opt == "1":
            while True:
                try:
                    addAmount = float(input("How much would you like to deposit? "))
                    acctList[ind].creditBalance(addAmount)
                    print("Your new balance is \n")
                    acctList[ind].printData()
                    break
                except ValueError:
                    print("Please enter an amount with two decimal places.")
                    
            
        elif opt == "2":
            while True:
                try:
                    lessAmount = float(input("How much would you like to withdraw? "))
                    acctList[ind].debitBalance(lessAmount)
                    print("Your new balance is ")
                    acctList[ind].printData()
                    break
                except ValueError:
                    print("Please enter an amount with two decimal places.")
                    
        else:
            newFname = input("Please enter new First Name: ")
            acctList[ind].setFname(newFname)
            newLname = input("Please enter new Last Name: ")
            acctList[ind].setLname(newLname)
            print("Successfully changed. Your new full name for this account is ")
            acctList[ind].printFullName()
                    
if __name__ == "__main__":
    main()
    
    
        

        






    
    