
class CheckingAccount:
    
    def __init__(self, fname, lname, streetAddress,
                 city, state, zipCode, accountNumber, balance):
        self.fname = fname
        self.lname = lname
        self.streetAddress = streetAddress
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.accountNumber = accountNumber
        self._balance = float(balance) #underscored to indicate private variable
    
    #the getters and the setters of the instance variables.       
    def getFname(self):
        return self.fname
    
    def setFname(self, fname):
        self.fname = fname
        return self.fname
    
    def getLname(self):
        return self.lname
    
    def setLname(self, lname):
        self.lname = lname
        return self.lname
    
    def getstreetAddress(self):
        return self.streetAddress
    
    def setstreetAddress(self, streetAddress):
        self.streetAddress = streetAddress
        return self.streetAddress
    
    def getCity(self):
        return self.city
    
    def setCity(self, city):
        self.city = city
        return self.city
    
    def getState(self):
        return self.state
    
    def setState(self, state):
        self.state = state
        return self.state
    
    def getZipCode(self):
        return self.zipCode
    
    def setZipCode(self, zipCode):
        self.zipCode = zipCode
        return self.zipCode
    
    def printFullName(self):
        return print("{} {}".format(self.fname, self.lname))
    
    def printFullAddress(self):
        return print("{}, {}, {}, {}".format(self.streetAddress, self.city, self.state, self.zipCode))
    
    def getAccountNumber(self):
        return self.accountNumber
    
    def setAccountNumber(self, accountNumber):
        self.accountNumber = accountNumber
        return self.accountNumber
          
    #the bank's perspective, when you deposit money to them, it will be credited to your account.
    def creditBalance(self, amountCredited):
        self._balance = self._balance + amountCredited
        return self._balance
    #the bank's perspective, when you withdraw your money from them, it will be debited from your account.
    def debitBalance(self, amountDebited):
        self._balance = self._balance - amountDebited
        return self._balance
    
    def printData(self):
        print(self.accountNumber, end='\t\t\t')
        print(self.fname, end='\t\t\t')
        print(self.lname, end='\t\t\t')
        print('{:,.2f}'.format(self._balance))
        
  

