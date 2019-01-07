#Write a program that calculates and prints the value according to formula
#formula is Q= squareroot of [(2*C*D)/H] WHERE C=50 and H=30
from math import sqrt
C = 50
H = 30
try:
    sequence = input("Enter values in comma-separated format: ")
    
    D_values = sequence.split(",")

    D_list = []
    for value in D_values:
        intvalue = int(value)
        D_list.append(intvalue)
    L_squares = []
    print("Input sequence is ",sequence)

    for D in D_list:
        answer = (2*C*D)/H
        L_squares.append(answer)

    accurateresults = []
    integerresults = []
    for item in L_squares:
        accurateresults.append(sqrt(item))
        integerresults.append(int(sqrt(item)))
    print("Accurate squareroots are : ")
    for element in accurateresults:
        print(element,end=",")
    print("\nInteger squareroots are : ")
    for element in integerresults:
        print(element,end= ",")
    print("\n")

except:
    print("you have entered in wrong format please Enter number in the format 100,150,180")
