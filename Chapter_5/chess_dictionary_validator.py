def isValidChessBoard(dict):
    num=[]
    stri=[]
    for i in dict.keys():
        n=int(i[0])
        num.append(n)
        s=i[1]
        stri.append(s)
    black=[]
    white=[]
    for i in dict.values():
        if i[0]=='b':
            black.append(i[1:])
        else:
            white.append(i[1:])
    v=['a','b','c','d','e','f','g','h']
    w=[1,2,3,4,5,6,7,8]
    for i in range(len(num)):
        if num[i] not in w:
            return False
        else:
            if stri[i] not in v:
                return False
            else:
                pass
    if len(black)>16 or len(white)>16:
        return False
    else:
        pass
    kb=black.count("king")
    kw=white.count("king")
    if kb!=1 or kw!=1:
        return False
    else:
        pass
    qb=black.count("queen")
    qw=white.count("queen")
    if qb>1 or qw>1:
        return False
    else:
        pass
    pb=black.count("pawn")
    pw=white.count("pawn")
    if pb>8 or pw>8:
        return False
    else:
        return True

        
dict={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
if isValidChessBoard(dict):
  print("Yes, the chessboard is valid.")

else:
  print("No")