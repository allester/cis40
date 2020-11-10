num = input("Enter a 4 digit number under 3000: ")
def roman (num):
    thou = ['', 'M', 'MM', 'MMM']
    hund = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    print (thou[int(num[0])] + hund[int(num[1])] + tens[int(num[2])] + ones[int(num[3])])

roman(num)
    
