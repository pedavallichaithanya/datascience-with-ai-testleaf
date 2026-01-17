correct_password = "openAI123"

for attempt in range(1, 4):
    entered = input("Enter password: ")

    if entered == correct_password:
        print("Login Successful")
        break
else:
    print("Account Locked")
