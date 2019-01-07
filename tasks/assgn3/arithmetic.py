#L1 = ["2","1","+","3","*"]
#L2 = ["4","13","5","/","+"]

def arithmeticExpression(L):
    operators = ["+","-","/","*"]

    
    opList = [x for x in L if x in operators]
    
    

    numList = [int(x) for x in L if x not in operators]
    

    r1=[]
    for item in L:
        op1Index =L.index(opList[0])
        

    
    i = op1Index -2
    
    a =numList[i]
    b = numList[i+1]

    

    if opList[0] == "+":
        r1.append(int(a+b))
        numList.remove(a)
        numList.remove(b)

    elif opList[0] == "-":
        r1.append(int(a-b))
        numList.remove(a)
        numList.remove(b)
        
    elif opList[0] == "*":
        r1.append(int(a*b))
        numList.remove(a)
        numList.remove(b)

    elif opList[0] == "/":
        r1.append(int(a/b))
        numList.remove(a)
        numList.remove(b)

    else :
        return "Check and enter valid operators"
    
    r1.append(opList[1])
    c = int(numList[0])
    r1.append(c)

    if opList[1] == "+":
        result = r1[0]+r1[2]

    elif opList[1] == "-":
        result = r1[0]-r1[2]

    elif opList[1] == "*":
        result = r1[0]*r1[2]

    elif opList[1] == "/":
        result = r1[0]/r1[2]

    else:
        return "Operation is beyond scope"
    return result

print(["2","1","+","3","*"],">>>",arithmeticExpression(["2","1","+","3","*"]))
print(["4","13","5","/","+"],">>>",arithmeticExpression(["4","13","5","/","+"]))
