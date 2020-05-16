# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ehdrb\PycharmProjects\Open210Team_CBNU\UI\MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(800, 500)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(40, 450, 281, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.SelectFileBtn = QtWidgets.QPushButton(Dialog)
        self.SelectFileBtn.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.SelectFileBtn.setObjectName("SelectFileBtn")
        self.PreviewButton = QtWidgets.QPushButton(Dialog)
        self.PreviewButton.setGeometry(QtCore.QRect(680, 450, 93, 28))
        self.PreviewButton.setObjectName("PreviewButton")
        self.TransFileBtn = QtWidgets.QPushButton(Dialog)
        self.TransFileBtn.setGeometry(QtCore.QRect(340, 30, 120, 40))
        self.TransFileBtn.setObjectName("TransFileBtn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 50, 75, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(590, 50, 75, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.DeleteFileBtn = QtWidgets.QPushButton(Dialog)
        self.DeleteFileBtn.setGeometry(QtCore.QRect(330, 80, 31, 28))
        self.DeleteFileBtn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.DeleteFileBtn.setText("")
        self.DeleteFileBtn.setDefault(False)
        self.DeleteFileBtn.setFlat(False)
        self.DeleteFileBtn.setObjectName("DeleteFileBtn")
        self.PDF_FileList = QtWidgets.QListWidget(Dialog)
        self.PDF_FileList.setGeometry(QtCore.QRect(30, 80, 291, 351))
        self.PDF_FileList.setDragDropOverwriteMode(False)
        self.PDF_FileList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.PDF_FileList.setAlternatingRowColors(True)
        self.PDF_FileList.setObjectName("PDF_FileList")
        self.Mp3_FileList = QtWidgets.QListWidget(Dialog)
        self.Mp3_FileList.setGeometry(QtCore.QRect(480, 80, 291, 351))
        self.Mp3_FileList.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.Mp3_FileList.setObjectName("Mp3_FileList")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SelectFileBtn.setText(_translate("Dialog", "파일선택"))
        self.PreviewButton.setText(_translate("Dialog", "미리보기"))
        self.TransFileBtn.setText(_translate("Dialog", "Mp3 변환 시작"))
        self.label.setText(_translate("Dialog", "PDF 파일"))
        self.label_3.setText(_translate("Dialog", "MP3 파일"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
