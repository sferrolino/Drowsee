import sys
import fileinput


#initalize valid users
users = [["sarah","admin", 1000.00],["sylvie","buy-standard", 2000.00],["zohaib","full-standard", 3000.00]]

#daily transaction file
f = open("dailyfile.txt", "w")
#MISCELLANEOUS FUNCTIONS:

#returns index where user shows up in 2d array
def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return i

def check_current_user(x):
    if x in [i[0] for i in users]:
        return True
    else:
        return False
#login
def login():
    print("Welcome to the Event Ticketing System!")
    username = input("To login, please enter your username: ")
    #Check if username is in the database
    if username in [i[0] for i in users]:
        #if username is valid: 
        print("Welcome " + username)
        #get the index of where they appear in the list
        index = index_2d(users, username)
        #pass arg of valid session types for user
        options(users[index][1], username)

    #else print error message


#logout
def logout():
    print("Goodbye")
    f.close()

#buy   
def buy():
    print("How many tickets do you want to buy?: ")


#sell
def sell():

    print("")

#refund
def refund(x):
    if x == "admin":
        buyer = input("Enter BUYER'S username: ")
        while(not check_current_user(buyer)):
            buyer = input("Please enter a valid username: ")
            check_current_user(buyer)
        buyerIndex = index_2d(users, buyer)

        seller = input("Enter SELLER'S username: ")
        while(not check_current_user(seller)):
            seller = input("Please enter a valid username: ")
            check_current_user(seller)

        sellerIndex = index_2d(users, seller)

        credit = input("Enter amount of credit to refund: ")
        while (not float(credit)):
            credit = input("Enter a valid amount of credit to refund: ")

        #do the refund 
        #new buyer balance
        users[buyerIndex][2] = users[buyerIndex][2] + float(credit)
        
        #new seller balance
        users[sellerIndex][2] = users[sellerIndex][2] - float(credit)

        #write to file
        f.write("05 "+ users[buyerIndex][0]+ " " + users[sellerIndex][0] + " " + str(float(credit)) +"\n")
        print("Refund successful!")
        options(x)
    else:
        print("Permission denied")
        options(x)


#add credit
def addCredit(x, y):
    if x == "admin":
        userName = input("Enter username to add credit to: ")
        while(not check_current_user(userName)):
            userName = input("Please enter a valid username to add credit to: ")
            check_current_user(userName)

        index = index_2d(users, userName)

        credit = input("Enter amount of credit to add: ")
        while (not float(credit)):
            credit = input("Enter a valid amount of credit to add: ")

        while (float(credit) > 1000.00):
            print("Amount must not be more than $1000.00")
            credit = input("Enter amount of credit to add: ")
        
        #add the credit  
        users[index][2] = users[index][2] + float(credit)

        #write to file 
        f.write("06 " + users[index][0] + " AA " + str(float(credit))+ "\n")

        #success
        print("Credit added successfully!")
        options(x,y)

    elif x == "full-standard":
        credit = input("Enter amount of credit to add: ")
        while (float(credit) > 1000.00):
            print("Amount must not be more than $1000.00")
            credit = input("Enter amount of credit to add: ")
        
        #add the credit
        index = index_2d(users, y)
        users[index][2] = users[index][2] + float(credit)
        #wrtie to file
        f.write("06 " + y + " FS " + str(float(credit)))
        print("Credit added successfully!")
        options(x,y)
    else:
        print("Permission denied")
        options(x,y)

#session type
def options(x, y):
    #initialize variables
    userType = x
    userName = y
    #check what type of user they are to determine valid transaction items
    if userType == "admin":
        transactionItems = ["buy", "create", "sell", "addcredit","logout","delete","refund"]
    elif userType == "full-standard":
        transactionItems = ["buy", "sell", "addcredit", "logout"]
    elif userType == "buy-standard":
        transactionItems = ["buy","logout"]
    else:
        transactionItems = ["sell","logout"]
    

    session = input("Enter session type [" + "/".join(transactionItems) + "]: ")

    if session == "buy":
        buy()
    
    elif session == "logout":
        logout()

    elif session == "refund":
        refund(userType)

    elif session == "addcredit":
        addCredit(userType, userName)

    else:
        print("Please enter a valid session type or type logout")
        options(userType)


#main
login()



