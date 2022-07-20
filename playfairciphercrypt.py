# PlayfairCipher
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

def encrypt(astring):
    upperstring=astring.upper()
    rpstring=upperstring.replace('J', 'I')
    rmstring=re.sub(r'[\W\d_]+','',rpstring)
    if len(rmstring)%2 != 0:
        newstring=rmstring+'X'
    else:
        newstring=rmstring
    duallist=re.findall('..',newstring)
    for i in range(len(duallist)):
        if duallist[i][0]==duallist[i][1]:
            c=duallist[i][0]
            duallist[i]=c+"X"
    for i in range(len(duallist)):
        firstrow=find_letter(duallist[i][0])[0]
        firstcol=find_letter(duallist[i][0])[1]
        secondrow=find_letter(duallist[i][1])[0]
        secondcol=find_letter(duallist[i][1])[1]
        if firstrow==secondrow:# Row case
            if firstcol<4 and secondcol <4:
                newfirst=CIPHER[firstrow][firstcol+1]
                newsecond=CIPHER[secondrow][secondcol+1]
            elif firstcol==4 and secondcol==4:
                newfirst=CIPHER[firstrow][0]
                newsecond=CIPHER[secondrow][0]
            elif firstcol==4:
                newfirst=CIPHER[firstrow][0]
                newsecond=CIPHER[secondrow][secondcol+1]
            elif secondcol==4:
                newfirst=CIPHER[firstrow][firstcol+1]
                newsecond=CIPHER[secondrow][0]
        elif firstcol==secondcol:    # Column case
            if firstrow<4 and secondrow <4:
                newfirst=CIPHER[firstrow+1][firstcol]
                newsecond=CIPHER[secondrow+1][secondcol]
            elif firstrow==4 and secondrow==4:
                newfirst=CIPHER[0][firstcol]
                newsecond=CIPHER[0][secondcol]
            elif firstrow==4:
                newfirst=CIPHER[0][firstcol]
                newsecond=CIPHER[secondrow+1][secondcol]
            elif secondrow==4:
                newfirst=CIPHER[firstrow+1][firstcol]
                newsecond=CIPHER[0][secondcol]
        else:                                                                 # Rectangular case
            newfirst=CIPHER[firstrow][secondcol]
            newsecond=CIPHER[secondrow][firstcol]
        duallist[i]=newfirst+newsecond
    return "".join(duallist)
print (encrypt("PS. Hello, worlds"))








