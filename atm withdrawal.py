amount = int(input("Enter withdrawal amount: "))

if amount % 100 == 0:
    print("Dispensing", amount)
else:
    print("Invalid amount")
