from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import generate
import interface,sys


class myDialog(interface.Ui_MainWindow):
    def __init__(self,Dialog):
        super().setupUi(Dialog)
        self.pushButton.clicked.connect(self.synthesis)
        self.pushButton_2.clicked.connect(self.tongbu)
        self.fyr = {
            "度小美": 0,
            "度小宇": 1,
            "度逍遥": 3,
            "度丫丫": 4
        }
        self.gs = {
            "wav":6,
            "mp3":3
        }
 
    def synthesis(self):
        # 转换的文本
        TEXT = self.textEdit.toPlainText()
        # 发音人
        PER = self.fyr[self.comboBox.currentText()]
        # 语速
        # print(dir(self.spinBox))
        SPD = self.spinBox.value()
        # 音调
        PIT = self.spinBox_2.value()
        # 音量
        VOL = self.spinBox_3.value()
        # 格式
        AUE = self.gs[self.comboBox_2.currentText()]
        # 文件名
        filename = self.lineEdit.text() + "."

        setting = {
            'TEXT': TEXT,
            'PER': PER,
            'SPD': SPD,
            'PIT': PIT,
            'VOL': VOL,
            'AUE': AUE,
            "filename": filename
        }
        generate.Generate(setting)

    def tongbu(self):
        data = self.textEdit.toPlainText()
        self.lineEdit.setText(data[:5])
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = myDialog(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())