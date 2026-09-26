class Bank:
    def __init__(self, code, address):
        self.code = code
        self.address = address

    def getAccounts(self):
        print(f"Nama Bank : {self.code}\nAlamat : {self.address}")

class Customer:
    def __init__(self, name, address, dob, card_number, pin, accounts=None):
        self.name = name
        self.address = address
        self.dob = dob
        self.card_number = card_number
        self.pin = pin
        self.accounts = accounts if accounts is not None else []

    def verifyPassword(self, input_pin):
        return self.pin == input_pin

class Account:
    def __init__(self, number, balance=0):
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print(f"Saldo tidak cukup untuk penarikan Rp{amount:,}!")
            return False

class ATM:
    def __init__(self, location, managedby):
        self.location = location
        self.managedby = managedby 

    def checkBalance(self, account):
        print(f"[ATM - {self.location}] Saldo Akun {account.number}: Rp{account.balance:,}")
        return account.balance

    def deposit(self, account, amount):
        account.deposit(amount)
        print(f"[ATM - {self.location}] Setor tunai Rp{amount:,} ke No Rekening {account.number} berhasil.")

    def withdraw(self, account, amount):
        if account.withdraw(amount):
            print(f"[ATM - {self.location}] Tarik tunai Rp{amount:,} dari No Rekening {account.number} berhasil.")

class ATM_Transactions:
    def __init__(self, transaction_id, date, type, amount, post_balance=0):
        self.transaction_id = transaction_id
        self.date = date
        self.type = type
        self.amount = amount
        self.post_balance = post_balance

    def modifies(self, account):
        if self.type.lower() == "deposit":
            account.deposit(self.amount)
        elif self.type.lower() == "withdraw":
            account.withdraw(self.amount)
        self.post_balance = account.balance
        print(f"Transaksi ID: {self.transaction_id} | Tipe: {self.type} | Jumlah: Rp{self.amount:,} | Saldo Akhir: Rp{self.post_balance:,}")

akun1 = Account(11223344, 1000000)
nasabah1 = Customer("Furqan", "Semarang", "15-05-2003", "5321-1234", "1234", [akun1])
bank1 = Bank("114", "Semarang")
atm1 = ATM("Kampus Udinus", bank1)
trx1 = ATM_Transactions("TRX01", "2026-09-24", "withdraw", 200000)
bank1.getAccounts()
print("Verifikasi PIN:", nasabah1.verifyPassword("1234"))
atm1.checkBalance(akun1)
atm1.withdraw(akun1, 200000)
atm1.deposit(akun1, 500000)
trx1.modifies(akun1)