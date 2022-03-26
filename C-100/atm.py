class atm:
    def __init__(self, cardnumber, pinnumber, balance, withdrawal):
          self.cardnumber = cardnumber
          self.pinnumber = pinnumber
          self.balance = balance
          self.withdrawal = withdrawal
    def balanceEnquiry(self):
        print("The current balance of the account is- " + self.balance)
    def cashWithdrawal(self):
        print("The total cash that has been withdrawn is- " + self.withdrawal)

customer = atm("15235692", "245546", "158900", "1390")
customer.balanceEnquiry()
customer.cashWithdrawal()