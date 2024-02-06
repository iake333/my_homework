#დავალება:
# შექმენი საბანკო ანგარიშის კლასი, მომხმარებლის, პაროლის და საწყისი თანხის პარამეტრებით. 
# თანხის შეტანის, გამოტანის და გადარიცხვის, დარჩენილი ნაშთის ჩვენების მეთოდებით.
# __repr__ მეჯიქ მეთოდით.
# პაროლის ცვლადი უნდა იყოს private _ ცვლადი და საჭიროა აკმაყოფილებდეს პირობას: მინიმალური სიმბოლოების ოდენობა _ 8.


class BankAccount:
    def __init__(self, initial_balance=0):
        self.username = input("Enter username: ")
        self.__password = None
        while True:
            password = input("Enter password (must be at least 8 characters): ")
            if len(password) >= 8:
                self.__password = password
                break
            else:
                print("Password must be at least 8 charachter")

        self._balance = initial_balance

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self._balance += amount
        print(f"Deposited {amount} money. New balance: {self._balance}")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdrew {amount} money. New balance: {self._balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self._balance

    def display_balance(self):
        print(f"Current balance: {self._balance}")

    def __repr__(self):
        return f"BankAccount(username={self.username}, balance={self._balance})"

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password

        else:
            print("Password must be at least 8 characters.")


# Example of using the BankAccount class
user_account = BankAccount(initial_balance=500)
print(user_account)
user_account.deposit()
user_account.withdraw()
user_account.display_balance()
