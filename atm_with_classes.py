class atm():
    def __init__(self, bank_name, balance =0, pin = "1234"):
        self.bank = bank_name
        self.__balance = balance
        self.__pin = pin
    
    def __authenticate(self, pin):
        return self.__pin == pin
    
    def check_bal(self, pin):
        if self.__authenticate(pin):
            print(f"Your current balance is: ${self.__balance}")
        else:
            print("Invalid PIN! Access Denied")

    def credit(self, amount,pin):
        if self.__authenticate(pin):
            if amount <= 0:
                print("Please enter a positive amount.")
            else:
                self.__balance += amount
                print(f"${amount} credited to your account.")
            self.check_bal(pin)
        else:
            print("Invalid PIN! Access Denied")

    def debit(self,amount,pin):
        if self.__authenticate(pin):
            if amount <= 0:
                print("Please enter a positive amount.")
            elif amount > self.__balance:
                print("Insufficient balance.")
            else:
                self.__balance -= amount
                print(f"${amount} debited from your account.")
            self.check_bal(pin)
        else:
            print("Invalid PIN! Access Denied")

    def pin_change(self, old_pin, new_pin):
        if self.__authenticate(old_pin):
            if len(new_pin)==4 and new_pin.isdigit():
                self.__pin = new_pin
                print("PIN Changed successfully!")
            else:
                print("Invalid PIN format! PIN must be 4 digits")
        else:
            print("Invalid PIN! Access Denied")


print("\nWelcome to the secure banking...")
atm_obj = atm("SBI")
while True:
    print(f"\n {atm_obj.bank} ATM Menu:")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. PIN Change")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        pin = input("Enter your PIN: ")
        amount = float(input("Enter amount to credit: "))
        atm_obj.credit(amount,pin)
    elif choice == '2':
        pin = input("Enter your PIN: ")
        amount = float(input("Enter amount to debit: "))
        atm_obj.debit(amount,pin)
    elif choice == '3':
        pin = input("Enter your PIN: ")
        atm_obj.check_bal(pin)
    elif choice == '4':
        old_pin = input("Enter your current PIN: ")
        new_pin = input("Enter your new PIN: ")
        atm_obj.pin_change(old_pin, new_pin)
    elif choice == '5':
        print(f"Thank you for using the {atm_obj.bank} ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")



