class acc:
    def __init__(self, ownr, blnce):
        self.owner = ownr
        self.balance = blnce
    def deposit(self, deposit_):
        self.balance+=deposit_
    def withdraw(self, withdraw):
        if withdraw<=self.balance:
            self.balance -= withdraw
        else:
            print("malo denyag(((")
    def show(self):
        print(self.balance)

rabotyaga = acc("Fedya", 1000)
rabotyaga.deposit(200)
rabotyaga.show()

rabotyaga.withdraw(300)
rabotyaga.show()

rabotyaga.withdraw(200)
rabotyaga.show()

rabotyaga.withdraw(701)