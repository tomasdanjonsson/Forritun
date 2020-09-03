n = int(input("Enter the length of the sequence: ")) # Do not change this line

for i in range(1, n + 1):
    if i == 1:
        sequence = one = i
    elif i == 2:
        sequence = two = i
    elif i == 3:
        sequence = three = i
    else:
        sequence = one + two + three
        one, two, three = two, three, sequence
print(sequence)