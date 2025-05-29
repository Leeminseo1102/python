def isStackFull() :
    global SIZE,stack,top
    if(top >= SIZE-1):
        return True
    else :
        return False

SIZE = 5
stack = ["커피","녹차","꿀물","모카",None]
top = 3 # top = 4 True

print("스텍이 꽉찼는지 여부 ==>", isStackFull())
