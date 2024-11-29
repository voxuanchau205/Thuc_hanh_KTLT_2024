class ATM:
     def init (self, balance=0):
         self.balance=balance
         self.is_logged_in=False
         self.pin = "1234" 
     def login (self, entered_pin):
         if entered_pin == self.pin:
            seft.is_logged in True
            print("Login successful!")
         else:
            print("Incorrect PIN! Please try again.")
                  
     def check_balance (self):
         if self.is_logged_in:
            print (f"Your account balance is: (self.balance) VND")
         else:
            print("Please login first.")
     def deposit (self, amount):
         if self.is_logged_in:
             self.balance + amount
             print (f"Successfully sent (amount) VND. Current balance: (self.balance) VND")
         else:
             print("Please login first.")
     def logout (self):
         self.is_logged_in = False
         print ("Logged out successfully.")
