class Bank:
    bank_name = "National Bank"  #

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  

    def show_details(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")

user1 = Bank("Ali")
user2 = Bank("Sara")

user1.show_details()
user2.show_details()

Bank.change_bank_name("Global Trust Bank")

user1.show_details()
user2.show_details()
