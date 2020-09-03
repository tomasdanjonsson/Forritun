num_int = int(input("Input a number: "))    # Do not change this line

max_int = 0    # Fasti

while num_int >= 0:    # Meðan num_int er stærra eða jafnt og 0, heldur keyrslan áfram.
    if max_int < num_int:    # Ef max_int er minna en num_int..
        max_int = num_int    # ..verður max_int jafnt og num_int.
    num_int = int(input('Input a number: '))

print("The maximum is", max_int)    # Do not change this line
