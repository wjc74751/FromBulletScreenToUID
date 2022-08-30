import re
from zlib import crc32
import os

CRCTableFiles = []

os.mkdir("FromBulletScreenToUID-main/CRCTable") #二级检索
CRCTableFiles.append(open("FromBulletScreenToUID-main/CRCTable/OneLenCRCTable.txt", "w"))
for j in range(1,16):
    os.mkdir(f"FromBulletScreenToUID-main/CRCTable/{j}")
    CRCTableFiles.append([])
    CRCTableFiles[j].append(open(f"FromBulletScreenToUID-main/CRCTable/{j}/TwoLenCRCTable.txt", "w"))
    for k in range(16):
        os.mkdir(f"FromBulletScreenToUID-main/CRCTable/{j}/{k}")
        CRCTableFiles[j].append([])
        CRCTableFiles[j][k+1].append(open(f"FromBulletScreenToUID-main/CRCTable/{j}/{k}/ThreeLenCRCTable.txt", "w"))
        for l in range(16):
            os.mkdir(f"FromBulletScreenToUID-main/CRCTable/{j}/{k}/{l}")
            CRCTableFiles[j][k+1].append(open(f"FromBulletScreenToUID-main/CRCTable/{j}/{k}/{l}/CRCTable.txt","w"))
print("Finished making folders")

for i in range(0,1000000000):
    crc32Value = hex(crc32(str(i).encode('utf-8')))[2:]
    hexedI = hex(i)[2:]
    if (len(crc32Value) < 2):
        CRCTableFiles[0].write(crc32Value + "," + hexedI + "\n")
    elif (len(crc32Value) < 3):
        CRCTableFiles[int(crc32Value[0],16)][0].write(crc32Value[1:] + "," + hexedI + "\n")
    elif (len(crc32Value) < 4):
        CRCTableFiles[int(crc32Value[0],16)][int(crc32Value[1],16)+1][0].write(crc32Value[2:] + "," + hexedI + "\n")
    else:
        CRCTableFiles[int(crc32Value[0],16)][int(crc32Value[1],16)+1][int(crc32Value[2],16)+1].write(crc32Value[3:] + "," + hexedI + "\n")
    finishRate = i/1000000000
    if (i%100000 == 0):
        print(finishRate)
