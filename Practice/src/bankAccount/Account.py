class Account:
    def __init__(self, account_name, account_type, account_number, pin):
        self.account_name = account_name
        self.account_type = account_type
        self.account_number = account_number
        self.pin = pin
        self.bank = "first_bank"
        self.nin = "12345678985"

    def __repr__(self):
        return f"""
        This is {self.account_name} account.
        Account type is {self.account_type}.
        Account number is {self.account_number}
        Bank type is {self.bank}
        """


account = Account("Favour", "Current", "225687", "1234")

print(account)
account2 = Account("Daddy GO", "Savings", "3232445", "0000")
print(account2)
