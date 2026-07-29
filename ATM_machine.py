#writing complete notes and making of oops in python 

class BankAccount:
    #constructor 
    '''
    i didnt learn this concept in any book or any tutor , 
    why we use __init__ method 
    what is function vs method 
    
    so basically a constructor is a special method which is executes 
    automatically when we make a object()[variable in python] of a class
     
    eg : 
     if we write 
      class Car:
         def __init__(self):
             print("Hello")
              
    a=Car()
    the output will be :"Hello"
     here a -->> object of class Car
      Car-->> class() '''
    def __init__(self, account_number, name, pin, balance):
        self.account_number = account_number
        self.name = name
        self.__pin = pin              # Private Attribute
        self.__balance = balance      # Private Attribute

        '''generally we use data/attribute in private form 
        in the class table representation we use '-' sign to represent 
        private attribute and '+' sign for public (they are generally)

        so basic doubt was that why did i put __ (double underscore) before 
        pin and balance , the reason is encapsulation , it mean that ke koi 
        v outside the class ko direct access nahi milna chahiye to change 
        the value , like agar mai likhu atm.__balance = 999999 from outside 
        the class it wont work becoz python automatically renames it 
        internally (name mangling) so it becomes hidden

        public attribute = anyone can acess and chnage it directly 
        private attribute = only class ke andar ke method hi acess/chnage 
        kar sakte hai , outside walo ko sirf get_balance() jaisा method 
        use karna padega'''

    #Getter
    def get_balance(self):
        '''
        this is called a GETTER method , its whole job is just to "get" 
        and return the private value safely without letting outside code 
        touch it directly , agar hum __balance ko public rakhte to koi v 
        bahar se seedha value change kr sakta tha jo galat hai for a bank 
        account
        '''
        return self.__balance

    #Deposit Method
    def deposit(self, amount):
        '''
        deposit -> simply add krta hai amount ko balance mai , but pehle 
        check karta hai ki amount>0 honi chahiye warna it dont make sense 
        to deposit negative money

        note : hum direct self.__balance +=amount kar paye kyuki ye method 
        class ke ANDAR likha hai , agar ye method class ke bahar hota to 
        private hone ki waja se acess nahi milta
        '''
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Available Balance: ₹{self.__balance}")
        else:
            print("Invalid amount.")

    #Withdraw Method
    def withdraw(self, amount):
        '''
        withdraw -> thoda different , yaha 2 condition check hoti hai
        1) amount should be positive 
        2) amount should not be greater than available balance 
           (varna balance negative ho jayega jo real life mai possible 
            nahi hai)
        '''
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.__balance:
            print("Insufficient Balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Available Balance: ₹{self.__balance}")

    #Change PIN
    def change_pin(self):
        '''
        change_pin basically ek if-else hai , pehle purana pin match 
        karvate hai warna koi v bahar ka bnda apna pin change kr dega , 
        match hua to naya pin le kr __pin ko update kr dete hai , yaha 
        v encapsulation ka use hai kyuki __pin direct edit nahi hota 
        bahar se
        '''
        old_pin = input("Enter Old PIN: ")

        if old_pin == self.__pin:
            new_pin = input("Enter New PIN: ")
            self.__pin = new_pin
            print("PIN Changed Successfully.")
        else:
            print("Incorrect Old PIN.")

    #Verify PIN
    def verify_pin(self):
        '''
        ye method return krta hai True/False (boolean) , entered pin ko 
        seedha __pin se compare kr rhe hai , issi ka use hum niche login 
        wale while loop mai kar rhe honge
        '''
        entered_pin = input("Enter ATM PIN: ")
        return entered_pin == self.__pin

    #Displaying Account Details
    def display_details(self):
        print("\n------ Account Details ------")
        print("Account Number :", self.account_number)
        print("Account Holder :", self.name)


class ATM(BankAccount):
    '''
    class ATM(BankAccount):  ---> ye line hi INHERITANCE hai

    matlab ATM class BankAccount ki saari property aur method already 
    "inherit" kar leti hai bina dobara likhe , real life mai socho jaise 
    beta apne father ke kuch property/qualities already le kar paida 
    hota hai , usko naya sikhna nahi padta

    BankAccount = Parent class (also called Base/Super class)
    ATM = Child class (also called Derived/Sub class)

    isliye jab maine atm = ATM(...) banaya , usko deposit() , withdraw() 
    sab already milgaya BankAccount se , maine sirf extra 
    mini_statement() aur menu() naye add kiye ATM class mai , ye hi to 
    fayda hai inheritance ka , code repeat nahi karna padta
    '''

    #Polymorphism(Method Overriding)
    def display_details(self):
        '''
        polymorphism ka mtlb "many forms" , yaha jo type use hua hai use 
        METHOD OVERRIDING bolte hai

        dekho BankAccount class ke andar bhi display_details() tha , aur 
        yaha ATM class ke andar v display_details() hai (same naam , 
        same method signature) , but dono ka kaam alag hai , jab hum 
        atm.display_details() likhte hai to python child class(ATM) wala 
        version run karta hai na ki parent(BankAccount) wala

        python hamesha pehle child class mai dekhta hai agar method mil 
        jaye to wahi use kr leta hai , parent tak jaata hi nahi , isko 
        hi bolte hai OVERRIDING
        '''
        print("\n========== ATM ACCOUNT ==========")
        print("Account Holder :", self.name)
        print("Account Number :", self.account_number)
        print("Balance         : ₹", self.get_balance())
        print("=================================")

    def mini_statement(self):
        '''
        ye ek naya method hai jo sirf ATM class mai hai (BankAccount mai 
        nahi tha) , isliye ye BankAccount ka object call nahi kr sakta , 
        sirf ATM ka object hi mini_statement() ko access kr payega
        '''
        print("\n------ MINI STATEMENT ------")
        print("Account Holder :", self.name)
        print("Account Number :", self.account_number)
        print("Available Balance : ₹", self.get_balance())

    def menu(self):
        '''
        menu() ek while True loop hai jo tab tak chalta rahega jab tak 
        user khud "7" (exit) na dabaye , har choice ek if-elif ladder se 
        handle ho raha hai , note kro ki menu khud koi naya kaam nahi kr 
        raha , wo sirf already bane hue method (deposit,withdraw,etc) ko 
        CALL kr raha hai , isse code clean rehta hai
        '''
        while True:

            print("\n============================")
            print("      ATM MAIN MENU")
            print("============================")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. Mini Statement")
            print("6. Account Details")
            print("7. Exit")

            choice = input("Enter Your Choice: ")

            if choice == "1":
                print(f"Available Balance: ₹{self.get_balance()}")

            elif choice == "2":
                amount = float(input("Enter Deposit Amount: "))
                self.deposit(amount)

            elif choice == "3":
                amount = float(input("Enter Withdrawal Amount: "))
                self.withdraw(amount)

            elif choice == "4":
                self.change_pin()

            elif choice == "5":
                self.mini_statement()

            elif choice == "6":
                self.display_details()

            elif choice == "7":
                print("\nThank You for using our ATM.")
                break

            else:
                print("Invalid Choice.")


#MAIN PROGRAMMING 

print("=================================")
print("       WELCOME TO XYZ BANK")
print("=================================")

#exampel Account
'''
yaha maine ATM class ka OBJECT bnaya hai naam se "atm" , ye important 
hai samjhna ki maine BankAccount ka object nahi bnaya , ATM ka bnaya 
kyuki ATM already saara BankAccount wala data v le lega (inheritance 
ki waja se) + apna extra menu(),mini_statement() v milega

class = ek BLUEPRINT hai , khud se koi real cheez nahi
object = jab hum blueprint se real cheez bana lete hai jise hum use 
kr sakte hai , yaha "atm" hi wo real usable object hai
'''
atm = ATM(
    account_number="1234567890",
    name="Atharva Mohite",
    pin="1234",
    balance=50000
)

#Login
'''
attempt = 3 se start hota hai , jab tak attempt>0 hai loop chalta 
rahega , andar verify_pin() call horaha hai (jo True/False return 
krta hai) , agar True mila to login successful ho kr menu() open ho 
jayega aur break lag jayega loop se

agar pin galat gya to attempt -=1 hoga , jab attempt 0 tak pahuch 
jayega to "Card Blocked" show hoga , ye ek real ATM machine jaisa hi 
security concept hai jo maine yaha implement kiya
'''
attempt = 3

while attempt > 0:

    if atm.verify_pin():
        print("\nLogin Successful.")
        atm.menu()
        break

    else:
        attempt -= 1

        if attempt == 0:
            print("\nATM Card Blocked.")
        else:
            print(f"Incorrect PIN. Attempts Left: {attempt}")