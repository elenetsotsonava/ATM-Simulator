class Account:
    """Base class for all account types."""

    def __init__(self, cust_id):
        """Initializes the account with a customer ID."""
        self.cust_id = cust_id


class CheckingAccount(Account):
    """Represents a checking account."""

    def __init__(self, cust_id, deposit_amount):
        """Initializes a checking account with a customer ID and initial deposit amount."""
        super().__init__(cust_id)
        self.amount = deposit_amount

    def deposit(self, deposit_amount):
        """Deposits a specified amount into the checking account."""
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        """Withdraws a specified amount from the checking account if sufficient funds are available."""
        if self.amount >= withdraw_amount:
            self.amount -= withdraw_amount
        else:
            print("Error! Cannot withdraw larger than what you have.")

    def display_amount(self):
        """Displays the current balance of the checking account."""
        print(f"Current balance: ${self.amount:.2f}")


class SavingsAccount(Account):
    """Represents a savings account."""

    def __init__(self, cust_id, deposit_amount):
        """Initializes a savings account with a customer ID and initial deposit amount."""
        super().__init__(cust_id)
        self.amount = deposit_amount

    def deposit(self, deposit_amount):
        """Deposits a specified amount into the savings account."""
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        """Withdraws a specified amount from the savings account if sufficient funds are available."""
        if self.amount >= withdraw_amount:
            self.amount -= withdraw_amount
        else:
            print("Error! Cannot withdraw larger than what you have.")

    def display_amount(self):
        """Displays the current balance of the savings account."""
        print(f"Current balance: ${self.amount:.2f}")


class BusinessAccount(Account):
    """Represents a business account."""

    def __init__(self, cust_id, deposit_amount):
        """Initializes a business account with a customer ID and initial deposit amount."""
        super().__init__(cust_id)
        self.amount = deposit_amount

    def deposit(self, deposit_amount):
        """Deposits a specified amount into the business account."""
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        """Withdraws a specified amount from the business account if sufficient funds are available."""
        if self.amount >= withdraw_amount:
            self.amount -= withdraw_amount
        else:
            print("Error! Cannot withdraw larger than what you have.")

    def display_amount(self):
        """Displays the current balance of the business account."""
        print(f"Current balance: ${self.amount:.2f}")


def initialise_objects():
    """Initializes account objects for testing."""
    global accounts
    accounts = {
        1: CheckingAccount(1, 2567.50),   # Customer 1: Checking account with initial balance
        2: SavingsAccount(2, 12890.01),   # Customer 2: Savings account with initial balance
        3: BusinessAccount(2, 14500.40),   # Customer 2: Business account with initial balance
    }


if __name__ == '__main__':
    initialise_objects()  # Set up accounts
    isSessionOn = True  # Control variable for the ATM session

    while isSessionOn:
        print("Welcome to 24-hour ATM service.")
        customerID = input("Enter your customer id number: ")

        # Validate customer ID input
        try:
            customerID = int(customerID)  # Convert input to an integer
        except ValueError:
            print("Invalid input. Please enter a numeric customer ID.")
            continue

        # Check if the customer ID exists in the accounts
        if customerID in accounts:
            account = accounts[customerID]  # Retrieve the corresponding account
            isAccountSessionOn = True  # Control variable for the account session

            while isAccountSessionOn:
                print("\nHow may I help you?")
                print("Press 1 for balance view.")
                print("Press 2 for withdrawals.")
                print("Press 3 to exit.")

                action_value = input("Please enter your choice: ")

                # View account balance
                if action_value == '1':
                    account.display_amount()

                # Withdraw funds from account
                elif action_value == '2':
                    amnt_to_withdraw = input("Enter the amount to withdraw: ")

                    # Validate withdrawal amount input
                    try:
                        amnt_to_withdraw = float(amnt_to_withdraw)  # Convert input to a float
                        account.withdraw(amnt_to_withdraw)  # Attempt to withdraw the specified amount
                    except ValueError:
                        print("Invalid input. Please enter a numeric amount.")

                # Exit the account session
                elif action_value == '3':
                    isAccountSessionOn = False
                    print("Thank you for using the 24-hour ATM service. Have a pleasant day.")

                # Handle invalid action inputs
                else:
                    print("Invalid choice. Please try again.")

        # Handle case when the customer ID is not found
        else:
            print("Cannot find your record. Please try again.")
