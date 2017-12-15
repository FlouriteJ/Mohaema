def _dict_sim(_address):
	"""input_dictionary_without_characteristic"""
	_file_ori=open(_address,'rU',encoding = 'utf-8')
	_list_ori=_file_ori.readlines()
	_file_ori.close()
	_dict_ori={}
	for i in range(len(_list_ori)):
		_list_ori[i]=_list_ori[i].strip('\n')
		k=_list_ori[i].split()
		_dict_ori[k[0]]=int(k[1])
	return _dict_ori
	
_dict_ori=_dict_sim('dictionary.dic')