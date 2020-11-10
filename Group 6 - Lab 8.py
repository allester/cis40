def bin_to_dec():

    bin = input("Enter a string of binary digits : ")[::-1]
    
    dec = 0

    for power in range(len(bin)):

        if bin[power] == "1":

            dec += 2 ** power

    print(dec)

def oct_to_dec():

    oct = input("Enter a string of octal digits : ")[::-1]

    dec = 0

    for power in range(len(oct)):

        
        dec += 8 ** power * int(oct[power])

    print(dec)

def hex_to_dec():

    hex = input("Enter a string of hexadecimal digits : ")[::-1]

    dec = 0

    char = {"A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15}

    for power in range(len(hex)):

        if hex[power] in char:

            dec += 16 ** power * char[hex[power]]

        else:
            
            dec += 16 ** power * int(hex[power])

    print(dec)
    
option = input("Enter 'b' for binary or 'o' for octal or 'h' for hexadecimal: ")

while True:
    
    if option == 'b':
        bin_to_dec()
        break

    elif option == 'o':
        oct_to_dec()
        break

    elif option == 'h':
        hex_to_dec()
        break
    
    else:
        print("Invalid input")
    


