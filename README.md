# FromBulletScreenToUID

This is a tiny python application used to find the UID of the bullet screen sender by inputing the bullet screen content and the **cid** of the video. 

The technique used include the `requests` module, the `crc32` function from `zlib` module and the `https://comment.bilibili.com/{cid}.xml` API. Since the UID of the bullet screen sender is hashed by CRC32, we need to make CRC Table to get the UID. The outstanding point here is that the CRC Table uses three-level-hex retrieval to speed up the searching process, up to a 4,096 times faster than not using it.

> CRC32 is a checksum/hashing algorithm that is very commonly used in kernels and for Internet checksums. It is very similar to the MD5 checksum algorithm. 

### How to use it?

1. install the corresponding modules

    `pip install bs4`
    
    `pip install lxml`
    
    `pip install requests`
    
2. run the `makeCRCTable.py` to get the CRC Table files.

3. run the `bilibiliFromBulletScreenToUID.py` to get start to use.
