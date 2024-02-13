class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number
    def send_money(self, amount, receipt):
        if self.account_balance >= amount:
           self.account_balance -= amount
           print(f"{amount} KES sent to {receipt} successfully")
        else:
            print("insufficient amount to send money")

class PersonalMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_no):
        super().__init__(account_balance, phone_number)
        self.id_no = id_no
    def buy_airtime(self, amount):
        self.account_balance -= amount
        print(f"{amount} KES airtime bought")
class BusinessMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_name):
        super().__init__(account_balance, phone_number)
        self.business_name = business_name
    def till_paid(self, amount):
        self.account_balance += amount
        print(f"{amount} KES till_paid by customer")

personal = PersonalMpesa(2000, 798935410, 34576789)
personal.send_money(1200, 23344678)
personal.buy_airtime(100)

