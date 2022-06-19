# example from lecture 3 slide 46
message = [0,1,1,0,1,1,1]
genarator = [1,0,1,1]

messageLen = len(message)
genaratorLen = len(genarator)
for i in range(messageLen-genaratorLen+1):
    if message[i] == 1:
        for j in range(genaratorLen):
            message[i+j] = message[i+j] ^ genarator[j]
    print(message)
res = message[-genaratorLen+1:]
print(res)
