correctPassword = "1234"
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
password = input("Enter your password: ")
confirmPassword = input("Confirm your password: ")

while password != correctPassword:
    print("The password is wrong!")
    password = input("Enter your password: ")

while password != confirmPassword:
    print("The two password are not the same.")
    password = input("Enter your password: ")
    confirmPassword = input("Confirm your password: ")

print("Hello, %s %s" % (firstName, lastName))
print("You are now logged!!")