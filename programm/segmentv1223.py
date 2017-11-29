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



#浼欎即绮剧鏄簩鍗佸浗闆嗗洟鏈€瀹濊吹鐨勮储瀵屻€傛垜浠櫧鐒跺浗鎯呬笉鍚屻€佸彂灞曢樁娈典笉鍚屻€侀潰涓寸殑鐜板疄鎸戞垬涓嶅悓锛屼絾鎺ㄥ姩缁忔祹澧為暱鐨勬効鏈涚浉鍚岋紝搴斿鍗辨満鎸戞垬鐨勫埄鐩婄浉鍚岋紝瀹炵幇鍏卞悓鍙戝睍鐨勬啩鎲浉鍚屻€傚彧瑕佹垜浠潥鎸佸悓鑸熷叡娴庣殑浼欎即绮剧锛屽氨鑳藉鍏嬫湇涓栫晫缁忔祹鐨勬儕娑涢獓娴紝寮€杈熸湭鏉ュ闀跨殑宕柊鑸▼銆?
#绗笁锛岄潰瀵瑰綋鍓嶆寫鎴橈紝鎴戜滑搴旇瀹屽杽鍏ㄧ悆缁忔祹娌荤悊锛屽く瀹炴満鍒朵繚闅溿€備簩鍗佸浗闆嗗洟搴旇涓嶆柇瀹屽杽鍥介檯璐у竵閲戣瀺浣撶郴锛屼紭鍖栧浗闄呴噾铻嶆満鏋勬不鐞嗙粨鏋勶紝鍏呭垎鍙戞尌鍥介檯璐у竵鍩洪噾缁勭粐鐗瑰埆鎻愭鏉冧綔鐢ㄣ€傚簲璇ュ畬鍠勫叏鐞冮噾铻嶅畨鍏ㄧ綉锛屽姞寮哄湪閲戣瀺鐩戠銆佸浗闄呯◣鏀躲€佸弽鑵愯触棰嗗煙鍚堜綔锛屾彁楂樹笘鐣岀粡娴庢姉椋庨櫓鑳藉姏銆備粖骞达紝鎴戜滑閲嶅惎浜嗕簩鍗佸浗闆嗗洟鍥介檯閲戣瀺鏋舵瀯宸ヤ綔缁勶紝甯屾湜缁х画鍚戝墠鎺ㄨ繘锛屼笉鏂彁楂樻湁鏁堟€с€?
#鍥介檯绋庢敹
#鍙嶈厫璐ラ鍩熷悎浣?

#鐢佃鐢佃瘽浼氳鏁扮櫨娆?
"""
銆€銆€涔犺繎骞冲拰褰附濯涘湪杩庡鍘呭悓璐靛浠竴涓€鎻℃墜锛屼簰鑷撮棶鍊欍€備範杩戝钩鍜屽江涓藉獩鍚屽鏂逛唬琛ㄥ洟鍥㈤暱鍙婇厤鍋跺湪瀹ゅ鑽夊潽鍚堝奖鐣欏康銆?
銆€銆€涔犺繎骞冲拰褰附濯涢個璐靛浠竴璧凤紝娌挎箹杈瑰皬璺极姝ュ墠琛岋紝杈硅蛋杈硅皥锛岀瑧璇泩鐩堛€傜幇鍦烘紨濂忥紝涓濈鎮犳壃锛屾儏鏅氦铻嶃€傚湪娆㈠揩鐨勮繋瀹炬洸涓紝涔犺繎骞冲拰褰附濯涘悓璐靛浠鍏ュ浼氬巺銆?
銆€銆€涔犺繎骞冲彂琛ㄨ嚧杈烇紝浠ｈ〃涓浗鏀垮簻鍜屼腑鍥戒汉姘戠儹鐑堟杩庡悇浣嶈吹瀹剧殑鍒版潵銆備範杩戝钩琛ㄧず锛屾澀宸炵礌鏈夆€滀汉闂村ぉ鍫傗€濈編瑾夛紝婀栧厜灞辫壊锛屼汉鏂囩編鏅紝淇嬀鐨嗘槸銆傝仈閫氳繖浜涚編鏅殑锛屾槸涓€搴у骇鍘嗗彶鎮犱箙銆侀€犲瀷浼樼編鐨勬ˉ銆傛湰灞婂嘲浼氫細鏍囩殑璁捐鐏垫劅灏辨潵婧愪簬姝ゃ€?
銆€銆€涔犺繎骞冲己璋冿紝浜屽崄鍥介泦鍥㈠氨瀹涜嫢涓€搴фˉ锛岃澶у浠庡洓闈㈠叓鏂硅蛋鍒颁簡涓€璧枫€傝繖鏄竴搴у弸璋婁箣妗ワ紝閫氳繃杩欓噷鎴戜滑鎶婂弸璋婄殑绉嶅瓙鎾悜鍏ㄧ悆銆傝繖鏄竴搴у悎浣滀箣妗ワ紝閫氳繃杩欓噷鎴戜滑鍏卞晢澶ц锛屽姞寮哄崗璋冿紝娣卞寲鍚堜綔锛岃皨姹傚叡璧€傝繖鏄竴搴ф湭鏉ヤ箣妗ワ紝閫氳繃杩欓噷鎴戜滑鍚屽懡杩愩€佸叡鎮ｉ毦锛屾惡鎵嬪墠琛岋紝鍏卞悓杩庢帴鏇村姞缇庡ソ鐨勬槑澶┿€?
銆€銆€涔犺繎骞冲己璋冿紝鎴戜滑姹囪仛鏉窞锛屾壙杞界潃鍚勫浗浜烘皯鐨勫帤鏈涘拰鏈熷緟銆傛垜浠负浜嗗叡鍚岀殑浣垮懡鑰屾潵锛岃鏋勫缓鍒涙柊銆佹椿鍔涖€佽仈鍔ㄣ€佸寘瀹圭殑涓栫晫缁忔祹锛屽紩棰嗘柊涓€杞己鍔插闀裤€傛垜浠负浜嗘洿绱у瘑鐨勪紮浼村叧绯昏€屾潵锛岃绉夋寔鍏辫耽鐞嗗康锛屼笉鏂杩涚悊瑙ｏ紝鎵╁ぇ鍏辫瘑锛屽嚌鑱氬悎鍔涖€傛垜浠负浜嗕汉绫诲懡杩愬叡鍚屼綋鐨勬効鏅€屾潵锛岃寮曢涓栫晫鍓嶈繘姝ヤ紣锛屽甫鍔ㄥ叏鐞冨彂灞曟疆娴侊紝涓哄疄鐜颁汉绫诲叡鍚岀箒鑽ｅ拰杩涙浣滃嚭鏇村ぇ璐＄尞銆?
銆€銆€瀹翠細鍚庯紝涔犺繎骞冲拰褰附濯涘悓璐靛浠竴鍚屼箻鑸癸紝鍓嶅線瑗挎箹宀虫箹瑙傜湅涓婚涓恒€婃渶蹇嗘槸鏉窞銆嬬殑鏂囪壓鏅氫細銆?
"""
#銆€鍥藉涓诲腑涔犺繎骞充富鎸佷細璁苟鑷村紑骞曡緸銆?鏂板崕绀捐鑰呮潕娑涙憚
#浜岄浂涓€鍏勾浜旀湀鍗佷簲鏃ユ垜浠幓涓婂