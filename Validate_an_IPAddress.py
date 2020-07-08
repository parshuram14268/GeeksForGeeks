def isValidIP(s):
    arr=list(map(str,s.split(".")))
    if len(arr)!=4:
        return False
    else:
        for i in arr:
            if not i.isdigit():
                return False
            x=int(i)
            if x>255 or x<0:
                return False
            if len(i)!=len(str(x)):
                return False
    return True
