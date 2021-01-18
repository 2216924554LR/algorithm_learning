def baseConvert(base, num):
    convertString = "0123456789ABCDE"
    if num >= base:
        return baseConvert(base, num//base) + convertString[num%base]
    return convertString[num]

if __name__ == "__main__":
    num = 123456
    print(baseConvert(16, 123456))
