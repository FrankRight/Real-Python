address = ["Flat Floor Street", "18", "New York"]
pins = {"Mike":1234, "Joe":1111, "Jack":2222}
repeat = "y"

def find_in_file(f):
    myfile = open("fruits.txt")
    fruits = myfile.read()
    fruits = fruits.splitlines()
    if f in fruits:
        return True
    else:
        return False

def requestPinInput():
    return int(input("Enter your pin: "))

def requestFruitInput():
    return input("Enter a fruit: ")

def validateUser():
    pin = requestPinInput()
    if pin in pins.values():
        return True
    else:
        return False

def main():
    print(address[0], address[1])

    if(validateUser() == True):
        fruit = requestFruitInput()
        foundInFile=find_in_file(fruit)
        if foundInFile == True:
            print("Fruit in the file.")
        else:
            print("The fruit is not in the file.")
    else:
        print("Cannot be accessed!!!")
        print("This info can be accessed only by: ")
        for key in pins.keys():
            print(key)

while(repeat == "y" or repeat == "Y"):
    main()
    repeat = input("\nContinue?(y/n): ")

else:
    print("Thankyou! Bye!")