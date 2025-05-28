queue =[None,None,None,None,None]
front = rear =-1

rear += 1
queue[rear] = "회사"
rear += 1
queue[rear] = "솔라"
rear += 1
queue[rear] = "문별"

print("-----------큐-------------")
print('[출구] <--',end = ' ')
for i in rang(0,len(queue),1):
    print(queue[i],end = ' ')
print('<-- [입구]')
