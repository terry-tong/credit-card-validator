def luhn_algorithm():
    cc = list(input("Please enter your 16-digit credit card number: "))
    n = len(cc) - 2
    while n >= 0:
        cc[n] = int(cc[n]) * 2
        if cc[n] >= 10:
            sumDigits = 0
            for digit in str(cc[n]):
                sumDigits += int(digit)
            cc[n] = str(sumDigits)
        cc[n] = str(cc[n])
        n -= 2
    ccSum = 0
    for digit in ''.join(cc):
        ccSum += int(digit)
    if ccSum % 10 == 0:
        valid = True
        print("This credit card is valid.")
    else:
        valid = False
        print("This credit card is invalid.")

luhn_algorithm()
