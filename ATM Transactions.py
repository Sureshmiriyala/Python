# ATM Class
class ATM:
    def __init__(self):
        self.balance = 0
        self.pin = None

    def create_pin(self):
        # Create a 4-digit PIN
        self.pin = input("Create a 4-digit PIN: ")
        while len(self.pin) != 4 or not self.pin.isdigit():
            print("Invalid PIN. Please enter a 4-digit numeric PIN.")
            self.pin = input("Create a 4-digit PIN: ")
        print("PIN created successfully!")

    def deposit(self, amount):
        if self.pin is None:
            print("Please create a PIN first.")
        else:
            if amount > 0:
                self.balance += amount
                print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
            else:
                print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if self.pin is None:
            print("Please create a PIN first.")
        else:
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
            elif amount <= 0:
                print("Invalid withdrawal amount. Please enter a positive amount.")
            else:
                print("Insufficient funds.")

    def check_balance(self):
        if self.pin is None:
            print("Please create a PIN first.")
        else:
            print(f"Your account balance is ₹{self.balance}")


# Main Program
def main():
    atm = ATM()

    while True:
        print("\nATM Menu:")
        print("1. Create PIN")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.create_pin()
        elif choice == "2":
            amount = float(input("Enter the deposit amount: ₹"))
            atm.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: ₹"))
            atm.withdraw(amount)
        elif choice == "4":
            atm.check_balance()
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
