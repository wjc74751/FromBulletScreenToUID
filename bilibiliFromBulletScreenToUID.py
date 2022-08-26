import requests
from bs4 import BeautifulSoup

CRCTableFiles = []

for j in range(1,10):
    CRCTableFiles.append([])
    for k in range(10):
        CRCTableFiles[j-1].append(open(f"FromBulletScreenToUID-main/CRCTable/{j}/{k}/CRCTable.txt","r"))

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
        hashedUID =  int(eval("0x"+bulletScreens[i].attrs['p'].split(",")[6]))
        for line in CRCTableFiles[int(str(hashedUID)[0])-1][int(str(hashedUID)[1])]:
            if (int(line.split(",")[0]) == hashedUID):
                UID = (line.split(",")[1])
                print("found target UID")
                print("UID: " + UID) 
                break
        
