# -*- coding:utf-8 -*-
import re
global final_output
def dict_sim(_address):
	"""input_dictionary_without_characteristic"""
	_file_ori=open(_address,'r')
	_list_ori=_file_ori.readlines()
	_file_ori.close()
	_dict_ori={}
	for i in range(len(_list_ori)):
		_list_ori[i]=_list_ori[i].strip('\n')
		k=_list_ori[i].split(" ")
		_dict_ori[k[0]]=int(k[1])
	return _dict_ori


def dict_check34(_str1):
	"""3 words with max length 4"""
	_len=len(_str1)
	_list1=[(i,j,k) for i in range(5) for j in range(5) for k in range(5)]
	_list0=[]
	for i in range(len(_list1)):
		#Take different length
		_current=_list1[i]
		if _len>=sum(_current) and sum(_list1[i])!=0:
			_list2=[]
			_n1=_current[0]
			_n2=_current[1]
			_n3=_current[2]
			_list2.append(_str1[:_n1])
			_list2.append(_str1[_n1:_n1+_n2])
			_list2.append(_str1[_n1+_n2:_n1+_n2+_n3])
		else:
			continue
		n=0
		for j in range(3):
			if _list2[j] in _dict_ori or _list2[j]=="":
				n+=1
		if n==3:
			_list0.append(_list2)
	return(_list0)


def dict_judge1(_str1):
	"""judge the first word"""
	global final_output
	if _str1=="":
		return 'Finished.'
	_list0=dict_check34(_str1)
	#Judge1: Longest
	_list=[]
	_list1=[]
	for i in range(len(_list0)):
		n=0
		for j in range(3):
			n+=len(_list0[i][j])
		_list.append(n)

	_max=max(_list)
	for i in range(len(_list0)):
		if _list[i]==_max:
			while '' in _list0[i]:
				_list0[i].remove('')
			if not _list0[i] in _list1:
				_list1.append(_list0[i])

	#Judge2: Max Average Length
	if len(_list1)==1:
		_list2=_list1
	else:
		_list=[]
		_list2=[]
		for i in range(len(_list1)):
			n=0
			for j in range(len(_list1[i])):
				n+=len(_list1[i][j])
			_list.append(n/len(_list1[i]))

		_max=max(_list)
		for i in range(len(_list1)):
			if _list[i]==_max:
				_list2.append(_list1[i])

	#Judge3: Take Variance for guarantee they're same patern
	if len(_list2)==1:
		_list3=_list2
	else:
		_list=[]
		_list3=[]
		for i in range(len(_list2)):
			n=0
			for j in range(len(_list2[i])):
				n+=len(_list2[i][j])**2
			_list.append(n/len(_list2[i]))

		_max=max(_list)
		for i in range(len(_list2)):
			if _list[i]==_max:
				_list3.append(_list2[i])

	#Judge4: Single Word Frequency
	if len(_list3)==1:
		_list4=_list3
	else:
		_min=4
		for i in range(len(_list3)):
			for j in range(len(_list3[i])):
				if len(_list3[i][j])<_min:
					_min=len(_list3[i][j])
		_list=[]
		_list4=[]
		for i in range(len(_list3)):
			n=0
			for j in range(len(_list3[i])):
				if len(_list3[i][j])==_min:
					n+=_dict_ori[_list3[i][j]]
			_list.append(n)

		_max=max(_list)
		for i in range(len(_list3)):
			if _list[i]==_max:
				_list4.append(_list3[i])

	#Output
	if len(_list4)!=1:
		_list4=_list4[0]
	if len(''.join(_list4[0]))==len(_str1):
		final_output=final_output+('  '.join(_list4[0]))
	else:
		final_output=final_output+_list4[0][0]+'  '
		dict_judge1(_str1[len(_list4[0][0]):])


def dict_para(ori_input):
	"""paragraph_identification"""
	global final_output
	punct={} #punctuation_and_others
	n=0
	ori_inputlist=list(ori_input)
	for i in range(len(ori_inputlist)):
		if ori_inputlist[i] not in _dict_ori:
			punct[n]=ori_inputlist[i]
			ori_inputlist[i]='|'
			n=n+1
	ori_input=''.join(ori_inputlist)
	ori_list=ori_input.split('|')
	final_list=[]
	end_output=''
	for i in range(len(ori_list)):
		final_output=''
		dict_judge1(ori_list[i])
		final_list.append(final_output)
	for i in range(len(punct)):
		end_output=end_output+str(final_list[i])+'  '+str(punct[i])+'  '
	if len(final_list)>len(punct):
		end_output=end_output+str(final_list[len(final_list)-1])+'  '
	return num_n_letter(end_output)


def _main():
	counter=1
	eventual_output=''
	while counter != 0:
		original_input=input()
		if original_input=='':
			counter=0
		else:
			eventual_output=eventual_output+dict_para(original_input)+'\n'
	print(eventual_output)


def num_n_letter(_str):
	_str=re.sub(r"—    —","——", _str)
	_str=re.sub(r"(?<=[一二三四五六七八九十零〇])  (?=[一二三四五六七八九十零〇年月日])","",_str)
	_str=re.sub(r"(?<=[0-9])\s+","", _str)
	_str=re.sub(r"(?<=[a-zA-Z])\s+(?=[0-9a-zA-Z])","", _str)

	return _str.strip(' ')


#Initialization
_dict_ori=dict_sim('dictionary.dic')
#print(_dict_ori)
global final_output
final_output=''


def segment(_str):
    global _dict_ori
    _dict_ori=dict_sim('dictionary.dic')

    eventual_output=''
    _list=_str.split('\n')
    for original_input in _list:
        eventual_output=eventual_output+dict_para(original_input)+'\n'
    if _str=="":
        eventual_output="请输入要分词的文本"
    return eventual_output
