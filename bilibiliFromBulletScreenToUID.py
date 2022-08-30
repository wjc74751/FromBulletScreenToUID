import requests
from bs4 import BeautifulSoup

CRCTableFiles = []

CRCTableFiles.append(open("FromBulletScreenToUID-main/CRCTable/OneLenCRCTable.txt", "r"))
for j in range(1,16):
    CRCTableFiles.append([])
    CRCTableFiles[j].append(open(f"FromBulletScreenToUID-main/CRCTable/{j}/TwoLenCRCTable.txt", "r"))
    for k in range(16):
        CRCTableFiles[j].append([])
        CRCTableFiles[j][k+1].append(open(f"FromBulletScreenToUID-main/CRCTable/{j}/{k}/ThreeLenCRCTable.txt", "r"))
        for l in range(16):
            CRCTableFiles[j][k+1].append(open(f"FromBulletScreenToUID-main/CRCTable/{j}/{k}/{l}/CRCTable.txt","r"))

        
cid=input("cid:")
targetBulletScreen = input("bulletScreen:")
url=f'https://comment.bilibili.com/{cid}.xml' #网络刷新
headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'}
res=requests.get(url,headers=headers)
res.encoding=res.apparent_encoding
html = BeautifulSoup(res.text,'lxml')
bulletScreens = html.find_all('d')
for i in range(len(bulletScreens)):
    if (targetBulletScreen == bulletScreens[i].text):
        print("found target bulletScreen")
        hashedUID =  bulletScreens[i].attrs['p'].split(",")[6] #stredHex
        if (len(hashedUID) < 2):
            for line in CRCTableFiles[0]:
                if (line.split(",")[0] == hashedUID):
                    UID = (line.split(",")[1])
                    print("found target UID")
                    print("UID: " + UID) 
                    break
        elif (len(hashedUID) < 3):
            for line in CRCTableFiles[int(hashedUID[0],16)][0]:
                if (line.split(",")[0] == hashedUID[1:]):
                    UID = (line.split(",")[1])
                    print("found target UID")
                    print("UID: " + UID) 
                    break
        elif (len(hashedUID) < 4):
            for line in CRCTableFiles[int(hashedUID[0],16)][int(hashedUID[1],16)+1][0]:
                if (line.split(",")[0] == hashedUID[2:]):
                    UID = (line.split(",")[1])
                    print("found target UID")
                    print("UID: " + UID) 
                    break
        else:
            for line in CRCTableFiles[int(hashedUID[0],16)][int(hashedUID[1],16)+1][int(hashedUID[2],16)+1]:
                if (line.split(",")[0] == hashedUID[3:]):
                    UID = int(line.split(",")[1],16)
                    print("found target UID")
                    print("UID: " + str(UID)) #想借用我同学自我介绍时的一句话：我来这里就是想卷死在坐的各位 812803012
                    break
        
