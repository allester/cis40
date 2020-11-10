def dec_to_bin(dec):

    bin = str(dec % 2)

    while dec > 1:

        dec = dec // 2

        bin = str(dec % 2) + bin

    print(bin)

dec_to_bin(0)
dec_to_bin(9)
dec_to_bin(73)
dec_to_bin(354)
