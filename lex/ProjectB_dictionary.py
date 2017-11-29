# -*- coding:utf-8 -*-
#dict 1
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
_file_.close()

#dict 2
from collections import Counter
target = open("combine.txt","r+",encoding = "utf-8")
content = target.readlines()
target_file = open("fantastic.txt","w")
string = {}
for i in content:
    string[i.strip("\n")] = 1
target_file.close()
target.close()
string = Counter(string)
combination = dict(string + bigdict)
# create a dictionary
bigdict2 = sorted(combination.items(),key = lambda  asd : asd[1] ,reverse = True)
dic_file=open("mixture_dict.txt","w",encoding="utf-8")
for elements in bigdict2:
    dic_file.write(elements[0] + "   " + str(elements[1]) + "\n")
dic_file.close()

def addup(combination):
    newword = input()
    if newword in combination:
        print("We already have this word")
    else:
        re_dict_file = open("mixture_dict.txt","a",encoding="utf-8")
        re_dict_file.write(newword + "   " + "1")
        re_dict_file.close()
    s = input("Do you want to continue to add new word?(Yes or No)")
    if s == "Yes":
        addup(combination)
    else:
        pass


