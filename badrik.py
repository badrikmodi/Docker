def isIPv4Address(inputString):
    s=inputString.split('.')
    if len(s)!=4:
        return False
    for elem in s:
        if len(elem)==0:
            return False
        if not elem.isdigit():
            return False
        if not 0<=int(elem)<=255:
            return False
    return True

print(isIPv4Address("265.153.123.231"))
