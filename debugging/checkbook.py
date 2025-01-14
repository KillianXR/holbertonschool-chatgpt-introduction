class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            # Error handling for non-numeric input
            while True:
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    cb.deposit(amount)
                    break  # Exit the loop once valid input is received
                except ValueError:
                    print("Invalid input. Please enter a valid number for the deposit.")
        elif action.lower() == 'withdraw':
            # Error handling for non-numeric input
            while True:
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    cb.withdraw(amount)
                    break  # Exit the loop once valid input is received
                except ValueError:
                    print("Invalid input. Please enter a valid number for the withdrawal.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()