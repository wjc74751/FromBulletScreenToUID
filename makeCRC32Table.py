from zlib import crc32
import os

CRCTableFiles = []

os.mkdir("FromBulletScreenToUID-main/CRCTable") #二级检索
for j in range(1,10):
    os.mkdir(f"FromBulletScreenToUID-main/CRCTable/{j}")
    CRCTableFiles.append([])
    for k in range(10):
        os.mkdir(f"FromBulletScreenToUID-main/CRCTable/{j}/{k}")
        CRCTableFiles[j-1].append(open(f"FromBulletScreenToUID-main/CRCTable/{j}/{k}/CRCTable.txt","w"))
    
for i in range(0,100000000):
    crc32Value = crc32(str(i).encode('utf-8'))
    CRCTableFiles[int(str(crc32Value)[0])-1][int(str(crc32Value)[1])].write(str(crc32Value) + "," + str(i) + "\n")
    finishRate = i/100000000
    if (i%10000 == 0):
        print(finishRate)



            
            

     