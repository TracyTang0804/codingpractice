# PlayfairCipherdecrypt
CIPHER = (("D", "A", "V", "I", "O"),
          ("Y", "N", "E", "R", "B"),
          ("C", "F", "G", "H", "K"),
          ("L", "M", "P", "Q", "S"),
          ("T", "U", "W", "X", "Z"))
# find_letter function should input a letter and return a tuple with row and column index in the cipher
import numpy as np
import re
CIPHERarr=np.array(CIPHER)
def find_letter(a):
    result=np.where(CIPHERarr==a)
    listofIndices= list(zip(result[0],result[1]))
    for indice in listofIndices:
          return indice
def decrypt(astring):
    duallist = re.findall('..', astring)
    for i in range(len(duallist)):
        firstrow = find_letter(duallist[i][0])[0]
        firstcol = find_letter(duallist[i][0])[1]
        secondrow = find_letter(duallist[i][1])[0]
        secondcol = find_letter(duallist[i][1])[1]
        if firstrow == secondrow:  # Row case
            newfirst = CIPHER[firstrow][firstcol - 1]
            newsecond = CIPHER[secondrow][secondcol - 1]
        elif firstcol == secondcol:  # Column case
            newfirst = CIPHER[firstrow - 1][firstcol]
            newsecond = CIPHER[secondrow - 1][secondcol]
        else:  # Rectangular case
            newfirst = CIPHER[firstrow][secondcol]
            newsecond = CIPHER[secondrow][firstcol]
        duallist[i] = newfirst + newsecond
    return "".join(duallist)
print(decrypt("QLGRQTVZIBTYQZ"))
