def isStackFull() :
    global SIZE,stack,top
    if(top >= SIZE-1):
        return True
    else :
        return False

def push(data):
    global SIZE,stack,top
    if(isStackFull()):
        print("스택이 꽉 찼습니다")
        return
    top += 1
    stack[top] = data

SIZE = 5
stack = ["커피","녹차","꿀물","모카",None]
top = 3 # top = 4 True

print(stack)
push("게토레이")
print(stack)
push("환타")

    
