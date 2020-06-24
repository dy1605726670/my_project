import interface,sys
from aip import AipSpeech
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class myDialog(interface.Ui_MainWindow, QWidget): #
    def __init__(self,Dialog):
        super(myDialog, self).__init__()
        super().setupUi(MainWindow)

        APP_ID = '20476069'
        API_KEY = 'yBUPmW5B55IWdufG84kew2K1'
        SECRET_KEY = 'chcdfHIhXgvE1dHURS41HmhqIR0HZWtA'

        self.client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

        # 绑定按钮
        self.pushButton.clicked.connect(self.synthesis)   # 合成按钮
        self.pushButton_2.clicked.connect(self.tongbu)   # 同步按钮

        self.fyr = {
            "度小美": 0,
            "度小宇": 1,
            "度逍遥": 3,
            "度丫丫": 4,
            "度小娇": 5,
            "度米朵": 103,
            "度博文": 106,
            "度小童": 110,
            "度小萌": 111
        }
        
 
    def synthesis(self):
        # 转换的文本
        TEXT = self.textEdit.toPlainText()
        # 发音人
        PER = self.fyr[self.comboBox.currentText()]
        # 语速
        SPD = self.spinBox.value()
        # 音调
        PIT = self.spinBox_2.value()
        # 音量
        VOL = self.spinBox_3.value()
        # 格式
        AUE = self.comboBox_2.currentText()
        # 文件名
        filename = self.lineEdit.text() + "." + AUE

        result = self.client.synthesis(
            TEXT, 'zh', 1, {
                'vol': VOL,
                'aue':AUE,
                'per':PER,
                'spd':SPD,
                'pit':PIT
            }
        )

        if not isinstance(result, dict):
            with open(filename, 'wb') as f:
                f.write(result)

        QMessageBox.about(self, "成功", "恭喜你生成语音成功, 已经保存到当前文件夹下...") #


    def tongbu(self):
        data = self.textEdit.toPlainText()
        self.lineEdit.setText(data[:5])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = myDialog(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())