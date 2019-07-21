# Convert from binary
def binHex(number): # Binary to Hexadecimal
    if len(hex(int(number, 2))[2:]) < 2:
        return "0x0" + hex(int(number, 2))[2:]
    else:
        return hex(int(number, 2))


def binDec(number): # Binary to Decimal
    return int(number, 2)


def binOct(number): # Binary to Octal
    return oct(int(number, 2))


# Convert from hexadecimal
def hexBin(number): # Hexadecimal to Binary
    if len(bin(int(number, 16))[2:]) < 8:
        return bin(int(number,16))[2:].zfill(8)
    else:
        return bin(int(number, 16))[2:]


def hexDec(number): # Hexadecimal to Decimal
    return int(number, 16)


def hexOct(number): # Hexadecimal to Octal
    return oct(int(number, 16))


# Convert from decimal
def decBin(number): # Decimal to Binary
    if len(bin(int(number))[2:]) < 8:
        return bin(int(number))[2:].zfill(8)
    else:
        return bin(int(number))[2:]


def decHex(number): # Decimal to Hexadecimal
    if len(hex(int(number))[2:]) < 2:
        return "0x0" + hex(int(number))[2:]
    else:
        return hex(int(number))


def decOct(number): # Decimal to Octal
    return oct(int(number))


# Convert from octal
def octBin(number): # Octal to Binary
    if len(bin(int(number, 8))[2:]) < 8:
        return bin(int(number, 8))[2:].zfill(8)
    else:
        return bin(int(number, 8))[2:]


def octHex(number): # Octal to Hexadecimal
    if len(hex(int(number, 8))[2:]) < 2:
        return "0x0" + hex(int(number, 8))[2:]
    else:
        return hex(int(number, 8))


def octDec(number): # Octal to Decimal
    return int(number, 8)


def testOnOne():
    # Binary Conversions
    print("Binary to Hexadecimal: 00000001 =", binHex("00000001"))
    print("Binary to Decimal: 00000001 =", binDec("00000001"))
    print("Binary to Octal: 00000001 =", binOct("00000001"))

    print("")

    # Hexadecimal Conversions
    print("Hexadecimal to Binary: 01 =", hexBin("01"))
    print("Hexadecimal to Decimal: 01 =", hexDec("01"))
    print("Hexadecimal to Octal: 01 =", hexOct("FF"))

    print("")

    # Decimal Conversions
    print("Decimal to Binary: 1 =", decBin("1"))
    print("Decimal to Hexadecimal: 1 =", decHex("1"))
    print("Decimal to Octal: 1 =", decOct("1"))

    print("")

    #Octal Conversions
    print("Octal to Binary: 0o1 =", octBin("0o1"))
    print("Octal to Hexadecimal: 0o1 =", octHex("0o1"))
    print("Octal to Decimal: 0o1 =", octDec("0o1"))


if __name__ == '__main__':
    testOnOne()