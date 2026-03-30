class BankAccount:

    def __init__(self, owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.owner}: поповнення на {amount}")
        else:
            print("Сума має бути більше 0")

    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"{self.owner} недостатньо коштів!")
        elif amount <= 0:
            print("Сума має бути більше 0")
        else:
            self.__balance -= amount
            print(f"{self.owner}: успішно знято: {amount}")

    def get_balance(self):
        return self.__balance


acc1 = BankAccount("Олег", 1000)
acc2 = BankAccount("Єва", 100)
acc3 = BankAccount("Саша", 86)


acc1.deposit(100)
acc1.withdraw(10)
print(acc1.get_balance())
print()
acc2.deposit(220)
acc2.withdraw(50)
print(acc2.get_balance())
print()
acc3.deposit(190)
acc3.withdraw(10)
print(acc3.get_balance())
print()