def format(num):

    string = ""

    length = len(str(num))

    for n in range(length):
    
        string = str(num % (10 ** (n + 1)) // (10 ** n)) + string

        if (n + 1) % 3 == 0 and (n + 1) != length:

            string = "," + string
        
    return string

print(format(1))
print(format(12))
print(format(123))
print(format(1234))
print(format(12345))
print(format(123456))
print(format(1234567))
print(format(12345678))
print(format(123456789))
print(format(1234567890))
print(format(12345678901))
print(format(123456789012))
print(format(1234567890123))



