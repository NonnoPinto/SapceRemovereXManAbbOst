import string

def spaceRemover(iban: string):
    ibanNoSpace: string = ""
    for i in iban:
        if i!=' ': ibanNoSpace += i
    print(ibanNoSpace)
    return ibanNoSpace