class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} has been deposited.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"${amount} has been withdrawn.")
            else:
                print("Insufficient balance for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

# Create a bank account instance
my_account = BankAccount("5491647", 0)

# Main program loop
print("Welcome to the Bank Account Management System!")
while True:
    # Prompt user to enter account number
    entered_account_number = input("Please enter your account number: ")
    
    # Verify account number
    if entered_account_number == my_account.account_number:
        print("\nSelect an option:")
        print("a) Deposit money")
        print("b) Withdraw money")
        print("c) Check balance")
        print("d) Exit")
        
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == 'a':
            # Deposit money
            try:
                amount = float(input("Enter amount to deposit: $"))
                my_account.deposit(amount)
            except ValueError:
                print("Invalid amount entered. Please try again.")
                
        elif choice == 'b':
            # Withdraw money
            try:
                amount = float(input("Enter amount to withdraw: $"))
                my_account.withdraw(amount)
            except ValueError:
                print("Invalid amount entered. Please try again.")
                
        elif choice == 'c':
            # Check balance
            my_account.check_balance()
        
        elif choice == 'd':
            # Exit program
            print("Thank you for using the Bank Account Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
    else:
        print("Incorrect account number. Please try again.")

    print("\n")  # Add space between iterations for readability
