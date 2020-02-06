from datetime import datetime

def printDashBoard():
    print("##############################\n\nCalculate and know your age!!!!\n\n##############################\n\n")

def promptInput():
    info = {"names":'sff', "year":0, "month":0, "day":0}

    info["names"] = input("Enter your name: ")
    print("Enter the following information of your birth date: ")
    info["year"] = int(input("Year: "))
    info["month"] = int(input("Month: "))
    info["day"] = int(input("Day: "))

    return info

def ageCalculator():
    printDashBoard()
    info=promptInput()
    dayspassed = datetime.now() - datetime(int(info["year"]), int(info["month"]), int(info["day"]))
    print("%s, %s years have passed since you were born." % (info["names"], str(int(dayspassed.days/365))))

ageCalculator()