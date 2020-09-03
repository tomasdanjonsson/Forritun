n = int(input("Enter the length of the sequence: ")) # Do not change this line

for i in range(1, n + 1):   # For Loop
    if i == 1:              # Ef 'i' er jafnt og 1 verður það 1
        sequence = one = i  
    elif i == 2:            # Ef 'i' er jafnt og 2 verður það 2
        sequence = two = i
    elif i == 3:            # Ef 'i' er jafnt og 3 verður það 3
        sequence = three = i
    else:
        sequence = one + two + three    # Sequence er 1 + 2 + 3
        one, two, three = two, three, sequence
    
    print(sequence)