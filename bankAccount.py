import datetime


class TimeZone:
    def __init__(self):
        self.local_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.utc_time = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def trans_time():
        return datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d%H%M%S")


class BankAccount(TimeZone):

    def __init__(self, account_number, first_name, last_name, t_id=0, t_type=''):
        super(BankAccount, self).__init__()
        self.t_type = t_type
        self.id = t_id
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.balance = float(0)

    def current_balance(self):
        return "%.2f" % self.balance

    def deposit_amount(self, deposit):
        self.balance += deposit
        print(f"Amount deposited:{deposit}")
        print(f"Balance in account:{self.current_balance()}")

    def withdraw_amount(self, withdraw):
        if withdraw <= self.balance:
            self.balance -= withdraw
            print(f"Amount withdraw successful for {withdraw}")
            print(f"Balance in account:{self.current_balance()}")
        else:
            print(f"Balance is insufficient for withdraw of {withdraw}")

    def interest_rate(self, interest_rate):
        self.balance = self.balance + (self.balance * (interest_rate / 100))
        print(f"New balance after interest rate:{self.current_balance()}")

    def trans_id(self):
        self.id += 1
        return self.id

    def confirmation_code(self):
        return self.t_type + '-' + str(self.account_number) + '-' + str(self.trans_time()) + '-' + str(self.trans_id())

    def transaction_type(self):
        while self.t_type not in ('D', 'W', 'I', 'X'):
            self.t_type = input("Enter the transaction type D for Deposit,W for Withdraw,I for Interest,X for Decline:")
            if self.t_type == 'D':
                return self.deposit_amount(float(input("Enter the deposit amount:")))
            elif self.t_type == 'W':
                return self.withdraw_amount(float(input("Enter the withdraw amount:")))
            elif self.t_type == 'I':
                return self.interest_rate(float(input("Enter the interest percentage:")))
            elif self.t_type == 'X':
                print("Declined Transaction")

    def __str__(self):
        print(f"Accoun number: {self.account_number}"
              f"\nFirst Name: {self.first_name}"
              f"\nLast Name: {self.last_name}"
              f"\nBalance: {self.current_balance()}"
              f"\nLocal Time: {self.local_time}"
              f"\nUTC Time: {self.utc_time}"
              f"\nConfirmation Code: {self.confirmation_code()}")


my_bank = BankAccount(12345, 'Arun', 'B')
print(my_bank.local_time)
print(f"Initial Balance: {my_bank.balance}")
print(f"{'# * 15'} Transaction Starts {'#' * 15}")
my_bank.transaction_type()
print("-" * 20 + "STATEMENT" + "-" * 20)
my_bank.__str__()
print("-" * 40)
print(f"\n{'#' * 15} Transaction Ends {'#' * 15}")
var = True
while var:
    b = input("Do you like to do another transaction Y/N:")
    if b in ('Y', 'y'):
        my_bank.t_type = ''
        my_bank.transaction_type()
        print("-" * 20 + "STATEMENT" + "-" * 20)
        my_bank.__str__()
        print("-" * 40)
        print(f"\n{'#' * 15} Transaction Ends {'#' * 15}")
    elif b in ('N', 'n'):
        var = False
        break
    else:
        continue
