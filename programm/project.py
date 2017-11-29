# -*- coding:utf-8 -*-  
import sys
import time
from PyQt4 import QtCore, QtGui, uic
from segmentv1223 import segment
from dictionary import addup
import icon_rc

qtCreatorFile = "project.ui"  # Enter ui-file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        global runtime
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.start.clicked.connect(self.segment0)
        self.Exit.triggered.connect(QtGui.qApp.exit)
        self.Go.triggered.connect(self.segment0)
        self.Clear.triggered.connect(self.ClearMessage)
        self.import_1.triggered.connect(self.FileOpen)
        self.SaveFile.triggered.connect(self.fileSave)
        self.AddFile.clicked.connect(self.FileOpen)
        self.action_Ctrl_Z.triggered.connect(self.Input.undo)
        self.action_Ctrl_Y.triggered.connect(self.Input.redo)
        self.action_Ctrl_C.triggered.connect(self.Input.copy)
        self.action_Ctrl_X.triggered.connect(self.Input.cut)
        self.action_Ctrl_V.triggered.connect(self.Input.paste)
        self.about_.triggered.connect(self.aboutthis)
        self.addword.clicked.connect(self.addup1)
        self.get_help.triggered.connect(self.helper)
        self.space_.triggered.connect(self.switch_pattern_space)
        self.vertical_.triggered.connect(self.switch_pattern_vertical)
        self.left_sider.triggered.connect(self.switch_pattern_left_sider)

    def segment0(self):
        runtime1= time.clock()
        ori_text=self.Input.toPlainText()
        global new_text
        new_text=segment(ori_text)
        new_text.replace("    ","  ")
        self.Output.setText(new_text)
        runtime2= time.clock()
        runtime = runtime2-runtime1-0.1
        self.time_speed.setText('分词完成！'+"耗时:"+str('%.4f'%runtime)+'s     '+'分词速度:'+str('%.4f'%(len(ori_text)/runtime))+"词/s")

    def addup1(self):
        text, ok = QtGui.QInputDialog.getText(self, '添加字典',
            '请输入要添加的词语:')
        if ok:
            re_dict_file = open("dictionary.dic","a")
            re_dict_file.write(text + " " + "1"+"\n")
            re_dict_file.close()
            reply=QtGui.QMessageBox.information(self,'添加成功','已添加至字典！',QtGui.QMessageBox.Ok)
    def ClearMessage(self):
        self.Input.clear()
    def FileOpen(self):
        dlg=QtGui.QFileDialog(self)
        self.filename=dlg.getOpenFileName()
        from os.path import isfile
        if isfile(self.filename):
            file=open(self.filename,'r')
            text=file.readlines()
            self.Input.setText("".join(text))
            file.close()
    def fileSave(self):
        global new_text
        dlg=QtGui.QFileDialog(self)
        self.filename=dlg.getSaveFileName()
        from os.path import isfile
        if self.filename!="":
            save=open(self.filename+'.txt','w')
            save.write(new_text)
            save.close()
    def aboutthis(self):
        reply = QtGui.QMessageBox.information(self,'关于',"Mohaema segmenter"+'\n'+'版本：v1.0'+'\n'+'制作人：张寅青 张超然 秦宇', QtGui.QMessageBox.Ok)
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Notice',"Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:

            event.accept()
        else:
            event.ignore()
    def helper(self):
        reply=QtGui.QMessageBox.question(self,"帮助",'1.在左侧输入要分词的文本，或者选择要分词的txt文件'+'\n'
        +"2.之后点击“开始分词”，在右侧得到结果"+'\n'+'3.在菜单栏中选择“保存文本”将分词后的文本输出成txt文件'+'\n'
        +"4.亦可使用菜单栏命令或者快捷键进行上述操作", QtGui.QMessageBox.Ok)
    def switch_pattern_space(self):
        global new_text
        new_text=new_text.replace('  ','  ')
        new_text=new_text.replace('/','  ')
        new_text=new_text.replace('|','  ')
        self.Output.setText(new_text)
    def switch_pattern_vertical(self):
        global new_text
        new_text=new_text.replace('  ','|')
        new_text=new_text.replace('/','|')
        new_text=new_text.replace('|','|')
        self.Output.setText(new_text)
    def switch_pattern_left_sider(self):
        global new_text
        new_text=new_text.replace('  ','/')
        new_text=new_text.replace('/','/')
        new_text=new_text.replace('|','/')
        self.Output.setText(new_text)










if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()