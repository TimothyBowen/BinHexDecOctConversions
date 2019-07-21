def binHex(number):
    calced = hex(int(number, 2))
    if len(calced[2:]) < 2:
        return "0x0" + calced[2:]
    else:
        return calced


def binDec(number):
    return int(number, 2)


def hexBin(number):
    return bin(int(number, 16))[2:].zfill(8)


def hexDec(number):
    return int(number, 16)


def decBin(number):
    return bin(int(number))[2:].zfill(8)


def decHex(number):
    calced = hex(int(number))
    if len(calced[2:]) < 2:
        return "0" + calced
    else:
        return calced


def testOnOne():
    print("Binary to Hexadecimal: 00000001 =", binHex("00000001"))
    print("Binary to Decimal: 00000001 =", binDen("00000001"))
    print("Hexadecimal to Binary: 01 =", hexBin("01"))
    print("Hexadecimal to Decimal: 01 =", hexDen("01"))
    print("Decimal to Binary: 1 =", denBin("1"))
    print("Decimal to Hexadeciaml: 1 =", denHex("1"))


if __name__ == '__main__':
    testOnOne()