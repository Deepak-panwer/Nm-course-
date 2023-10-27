class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        elif amount > self.__account_balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")

    def display_balance(self):
        print(f"Account balance for {self.__account_holder_name}: ${self.__account_balance}")

# Test the BankAccount class
if __name__ == "__main__":
    # Create a BankAccount instance
    my_account = BankAccount("12345", "John Doe", 1000)

    # Display the initial balance
    my_account.display_balance()

    # Deposit some money
    my_account.deposit(500)

    # Withdraw some money
    my_account.withdraw(200)

    # Try to withdraw more money than the balance
    my_account.withdraw(1500)

    # Display the final balance
    my_account.display_balance()
