from json import load

def displayHeader():
    print(r"""
        ##########################################################################################
        #                            THE RIGHT ENGLISH DICTIONARY.                               #
        #           Look for any confusing words here and find a clear, concise meaning.         #
        ##########################################################################################
    """)

def requestWord():
    return input("\tEnter a word to search(q to quit): ")

def definations(word,data):
    return data[word]

def openFile(fileName):
    fileIn=open(fileName)
    return load(fileIn)

def displayMeaning(word,data):
    print("\n\nThe word, %s is defined as follows:- \n" % word)
    for i,item in zip(range(1,50),data[word]):
        if i>1:
            print(" Defination %s:\n\t %s\n" % (i, item))
        else:
            print(" Defination:\n\t %s\n" % item)

def checkforWord(word, data):
    if (word in data) == True:
        return True
    else:
        return False
def quitApp():
    print("\n\tThank you for using our app!! You are always welcome...Bye!!\n")
    quit()

def dictionary():
    displayHeader()
    data = openFile("data.json")
    word = requestWord().lower()
    if word == "q":
        quitApp()
    else:
        if checkforWord(word, data)== True:
            defination = definations(word, data)
            displayMeaning(word,data)
        else:
            print('''\n\t\tUNKNOWN WORD '%s'!!!, it is not in the english language 
            \tor CHECK the SPELLING and then try again.\n\n''' % word)
while(True):
    dictionary()