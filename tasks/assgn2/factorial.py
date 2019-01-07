# Compute factorial of given numbers

num_seq_inp = input("Enter the numbers in comma-separated format : ")
try:
    seq = num_seq_inp.split(",")
    seq = [int(element) for element in seq]
    def factorial(n):
        list_of_num = []
        while n > 0:
            list_of_num.append(n)
            n = n-1
        result = 1
        for num in list_of_num:
            result = result*num
        return result

    print("Given numbers are",end = ",")
    for number in seq:
        print(number,end=",")    
    #print(list(map(lambda x:x ,seq)),end=",")

    print("\nfactorial of given numbers are",end=" ")
    for number in seq :
        print(factorial(number),end=",")
    print("\n")
    #print(list(map(lambda n:factorial(n),seq)),end=",")


except:
    print("enter number in the following format 1,2,8,9")



