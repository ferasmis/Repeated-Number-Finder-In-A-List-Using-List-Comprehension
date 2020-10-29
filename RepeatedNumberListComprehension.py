## Author: Feras
## Description: A program that finds repeated values in a list

def repeated(myList):
    found = [i for i in myList if myList.count(i) > 1]
    return found
print(repeated([1,2, 45, 67, 45]))
