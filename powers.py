def powers(num):

    width = 25

    for i in range(50):

        print(str(num ** i).rjust(width))

num = int(input("Enter the exponent: "))

powers(num)

