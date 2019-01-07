#calculate number of letters and digits
sentence = input("Enter the sentence: ")
letters = []
digits = []
digits_0_to_9 =[str(n) for n in range(0,10)]
for char in sentence :
    if char.isupper() or char.islower():
        letters.append(char)
    elif char in digits_0_to_9:
        digits.append(char)
    else:
        continue
print("LETTERS",len(letters))
print("DIGITS",len(digits))

