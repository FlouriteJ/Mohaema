# Mohaema 中文分词系统

## 介绍
这是基于字典和规则的中文分词项目，可以支持快速且准确的中文分词，同时可以根据新文本和旧字典生成新字典，也通过PyQt支持UI界面显示。

详细介绍和算法可在report/下找到。

## 使用方法

### Python程序内部调用

```
from moha import segment
segment("艺术是什么")

#函数返回 "艺术  是  什么"

```

### 命令行调用

```
python moha.py "伙伴精神是二十国集团最宝贵的财富"
# 伙伴  精神  是  二十国  集团  最  宝贵  的  财富

python moha.py [infile] [outfile]
# 可以在outfile文件下写入对infile的分词结果
```
### Contents

Path | Content
------------ | -------------
/programm/project.py | main programm (note: cannot run without PyQt4)
/data | all the work aimed at G20 corpus
/lex | lex-building
/report | project report
/data/segtest.txt | testing-corpus mentioned in report
/data/G20_3.txt | corpus from G20

[@FlouriteJ](https://github.com/FlouriteJ)

2017/01/10
