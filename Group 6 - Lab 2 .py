def bills(dollar):

    money = dollar // 1
    
    hundreds = money // 100
    fifties = (money - hundreds * 100) // 50
    twenties = (money - hundreds * 100 - fifties * 50) // 20
    tens = (money - hundreds * 100 - fifties * 50 - twenties * 20) // 10
    fives = (money - hundreds * 100 - fifties * 50 - twenties * 20 - tens * 10) // 5
    ones = (money - hundreds * 100 - fifties * 50 - twenties * 20 - tens * 10 - fives * 5) // 1

    decimal = dollar - money

    quarter = (decimal * 100) // 25
    dimes = (decimal * 100 - quarter * 25) // 10
    nickel = (decimal * 100 - quarter * 25 - dimes * 10) // 5
    penny = (decimal * 100 - quarter * 25 - dimes * 10 - nickel * 5) // 1

    print("$", dollar, "- hundreds:", int(hundreds), ", fifties:", int(fifties), ", twenties:",
          int(twenties), ", tens:", int(tens), ", fives:", int(fives), ", ones:", int(ones),
          "\nquarters:", int(quarter), ",dimes:", int(dimes), "nickels:", int(nickel), ",pennies:", int(penny))

bills(787.19)
bills(100.93)
bills(1.75)
