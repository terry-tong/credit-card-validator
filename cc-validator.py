def luhn_algorithm():
    cc = input("Please enter your 16-digit credit card number: ")
    check = list(cc)
    issuer = 0
    n = len(check) - 2
    while n >= 0:
        check[n] = int(check[n]) * 2
        if check[n] >= 10:
            sumDigits = 0
            for digit in str(check[n]):
                sumDigits += int(digit)
            check[n] = str(sumDigits)
        check[n] = str(check[n])
        n -= 2
    checkSum = 0
    for digit in ''.join(check):
        checkSum += int(digit)
    if checkSum % 10 == 0:
        valid = True
        if cc[0] == "4":
            issuer = "Visa"
        if cc[0] == "5" and cc[1] in "12345":
            issuer = "Mastercard"
        print("This credit card is valid and is issued by {}.".format(issuer))
    else:
        valid = False
        print("This credit card is invalid.")


luhn_algorithm()
