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
def main(): 
    atm = ATM()
    while True:
          print("\n- MENU ATM")
          print("1. Login")
          print("2. Check balance")
          print("3. Withdraw")
          print("4. Deposit")
          print("5. Log out")
          print("6. Exit")
          choice = input ("Choose function: ")
          if choice == '1':
              pin input ("Enter PIN: ")
              atm.login(pin)
          elif choice == '2':
              atm.check_balance()
          elif choice == '3':
              amount = float(input("Enter the amount to withdraw: ")) 
              atm.withdraw (amount)
          elif choice == '4':
              amount = float (input ("Enter amount to deposit: ")) 
              atm.deposit(amount)
          elif choice == '5':
              atm.logout ()
          elif choice == '6':
              print("Exit program...")
              break
          else:
              print("Invalid selection. Please try again.")
if name == "_main_":
   main()
      
