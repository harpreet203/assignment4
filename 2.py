username = "python"
password = "rules"
attempts = 0

while attempts < 5:
    user_input_username = input("Enter username: ")
    user_input_password = input("Enter password: ")

    if user_input_username == username and user_input_password == password:
        print("Welcome!")
        break
    else:
        print("Invalid username or password. Please try again.")
        attempts += 1

if attempts == 5:
    print("Access denied.")
