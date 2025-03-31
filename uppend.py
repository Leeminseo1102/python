katok = []
def add_data(friend) :
    katok.append(None)
    klen = len(katok)
    katok[klen -1] = friend

count = 0

while True:

    count = count + 1

    if count > 5:

        break
    
    name = input("카톡 친구 입력: ")


    add_data(name)

    print(katok)


