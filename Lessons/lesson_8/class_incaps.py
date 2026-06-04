
class Bank:
    GLOBAL_BALANCE = 100
    def __init__(self, name):
        self.name = name
        self.__balance = 0
        self.is_true = True


    def __deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def add_money_and_return_balance(self, amount):
        print(self.get_balance())
        self.__deposit(amount)
        print(self.get_balance())



bank_1 = Bank('Private')
bank_1.__balance = 234

# print(bank_1.__getattribute__('balance'))
bank_1.add_money_and_return_balance(100)
bank_1.add_money_and_return_balance(100)
print(Bank.__mro__)
# print(bank_1.is_true)
# bank_1._is_true = False
# print(bank_1.is_true)
#
# print(bank_1.get_balance())
# bank_1.deposit(15)
#
# print(bank_1.get_balance())
class BankStaff(Bank):
    pass
class BankAccount(Bank):
    #__call__
    #__new__
    # def __init__(self):
    pass
    #__del__

print(BankAccount('Private').GLOBAL_BALANCE)
print(BankAccount.__mro__)
print(BankAccount('Private').name)

class GlobalBalance(BankAccount, BankStaff):
    pass
print(GlobalBalance.__mro__)