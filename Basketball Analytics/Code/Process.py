import os, csv

#Calculate points team scored while on court
def plus(x):
    print(x)

#Calculate points scored against while on court
def minus(x):
    print(x)

def printAllFileNames():
    for filename in os.listdir("../Games/"):
        plus(filename)
        minus(filename)
        break

if __name__ == "__main__":
    printAllFileNames()
