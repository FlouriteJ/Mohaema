# -*- coding:utf-8 -*-
from collections import Counter
_file_=open("mixture.txt","r+")
biglist=_file_.readlines()
bigstring=""
for items in biglist:
    for i in items:
        if i in ["！", "？", "《", "》", "：", "；", "“", "”", "‘", "’", "，", "。", "【", "】", "、", "——","』","●","（","）","…"]:
            items=items.replace(i,"")
    bigstring += items.strip("\n！、‘；，。？《》“”：’【】……")
biglist2=bigstring.split()
for items in biglist2:
    items=items.strip(" ")
bigdict=Counter(biglist2)
bigdict2 = sorted(bigdict.items(),key = lambda  asd : asd[1] ,reverse = True)
dic_file=open("mixture_dict.txt","w")
for elements in bigdict2:
    dic_file.write(elements[0] + "  " + str(elements[1]) + "\n")
dic_file.close()
_file_.close()

