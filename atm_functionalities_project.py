
balance = 0
def credit(amount):
    global balance
    if amount <= 0:
        print("Please enter a positive amount.")
    else:
        balance += amount
        print(f"${amount} credited to your account.")
    
def debit(amount):
    global balance
    if amount <= 0:
        print("Please enter a positive amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"${amount} debited from your account.")

def check_bal():
    print(f"Your current balance is: ${balance}")
     
while True:
    print("\nATM Menu:")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        amount = float(input("Enter amount to credit: "))
        credit(amount)
    elif choice == '2':
        amount = float(input("Enter amount to debit: "))
        debit(amount)
    elif choice == '3':
        check_bal()
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
