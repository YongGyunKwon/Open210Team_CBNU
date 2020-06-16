# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.ui확장자파일\MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(785, 455)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Exe/icon/실행아이콘.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(64, 74, 86);")
        Dialog.setFixedSize(785, 455)
        # Dialog.setSizeGripEnabled(False)
        # Dialog.setModal(False)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(30, 350, 291, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.TransFileBtn = QtWidgets.QPushButton(Dialog)
        self.TransFileBtn.setGeometry(QtCore.QRect(350, 220, 91, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 74, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 74, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 74, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 74, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 74, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 74, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 74, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 74, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 74, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.TransFileBtn.setPalette(palette)
        self.TransFileBtn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.TransFileBtn.setStyleSheet("\n"
"image: url(:/Main/icon/변환아이콘.png)")
        self.TransFileBtn.setText("")
        self.TransFileBtn.setAutoDefault(False)
        self.TransFileBtn.setDefault(False)
        self.TransFileBtn.setFlat(True)
        self.TransFileBtn.setObjectName("TransFileBtn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(590, 90, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("image: url(:/Main/icon/음성파일아이콘.png)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 100, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("image: url(:/Main/icon/시각파일아이콘.png)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.DeleteFileBtn = QtWidgets.QPushButton(Dialog)
        self.DeleteFileBtn.setGeometry(QtCore.QRect(80, 100, 41, 41))
        self.DeleteFileBtn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.DeleteFileBtn.setAutoFillBackground(False)
        self.DeleteFileBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Main/ButtonImage/DeleteIMG2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeleteFileBtn.setIcon(icon1)
        self.DeleteFileBtn.setIconSize(QtCore.QSize(30, 30))
        self.DeleteFileBtn.setCheckable(False)
        self.DeleteFileBtn.setAutoRepeat(False)
        self.DeleteFileBtn.setAutoDefault(False)
        self.DeleteFileBtn.setDefault(False)
        self.DeleteFileBtn.setFlat(True)
        self.DeleteFileBtn.setObjectName("DeleteFileBtn")
        self.PDF_FileList = QtWidgets.QListWidget(Dialog)
        self.PDF_FileList.setGeometry(QtCore.QRect(30, 150, 291, 181))
        self.PDF_FileList.setStyleSheet("color: rgb(255, 255, 255);")
        self.PDF_FileList.setDragDropOverwriteMode(False)
        self.PDF_FileList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.PDF_FileList.setAlternatingRowColors(False)
        self.PDF_FileList.setObjectName("PDF_FileList")
        self.Sound_FileList = QtWidgets.QListWidget(Dialog)
        self.Sound_FileList.setGeometry(QtCore.QRect(470, 150, 291, 181))
        self.Sound_FileList.setStyleSheet("color: rgb(255, 255, 255);")
        self.Sound_FileList.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.Sound_FileList.setObjectName("Sound_FileList")
        self.FileTypeBox = QtWidgets.QComboBox(Dialog)
        self.FileTypeBox.setGeometry(QtCore.QRect(220, 120, 101, 21))
        self.FileTypeBox.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(63, 102, 139);")
        self.FileTypeBox.setObjectName("FileTypeBox")
        self.FileTypeBox.addItem("")
        self.FileTypeBox.addItem("")
        self.FileTypeBox.addItem("")
        self.FileTypeBox.addItem("")
        self.FileTypeBox.addItem("")
        self.Save_path_setting = QtWidgets.QPushButton(Dialog)
        self.Save_path_setting.setGeometry(QtCore.QRect(20, 400, 131, 31))
        self.Save_path_setting.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(63, 102, 139);")
        self.Save_path_setting.setObjectName("Save_path_setting")
        self.PreviewButton = QtWidgets.QPushButton(Dialog)
        self.PreviewButton.setGeometry(QtCore.QRect(660, 350, 93, 28))
        self.PreviewButton.setStyleSheet("background-color: rgb(63, 102, 139);\n"
"color: rgb(255, 255, 255);")
        self.PreviewButton.setObjectName("PreviewButton")
        self.SoundTypeBox = QtWidgets.QComboBox(Dialog)
        self.SoundTypeBox.setGeometry(QtCore.QRect(660, 120, 101, 21))
        self.SoundTypeBox.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(63, 102, 139);")
        self.SoundTypeBox.setObjectName("SoundTypeBox")
        self.SoundTypeBox.addItem("")
        self.SoundTypeBox.addItem("")
        self.SoundTypeBox.addItem("")
        self.AddFileBtn = QtWidgets.QPushButton(Dialog)
        self.AddFileBtn.setGeometry(QtCore.QRect(30, 100, 41, 41))
        self.AddFileBtn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.AddFileBtn.setStyleSheet("")
        self.AddFileBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Main/ButtonImage/AddIMG2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddFileBtn.setIcon(icon2)
        self.AddFileBtn.setIconSize(QtCore.QSize(30, 30))
        self.AddFileBtn.setCheckable(False)
        self.AddFileBtn.setAutoDefault(False)
        self.AddFileBtn.setDefault(False)
        self.AddFileBtn.setFlat(True)
        self.AddFileBtn.setObjectName("AddFileBtn")
        self.SavePathEDT = QtWidgets.QTextBrowser(Dialog)
        self.SavePathEDT.setGeometry(QtCore.QRect(160, 400, 461, 30))
        self.SavePathEDT.setStyleSheet("color: rgb(255, 255, 255);")
        self.SavePathEDT.setUndoRedoEnabled(True)
        self.SavePathEDT.setReadOnly(True)
        self.SavePathEDT.setOverwriteMode(False)
        self.SavePathEDT.setObjectName("SavePathEDT")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 81, 71))
        self.label_2.setStyleSheet("image: url(:/Main/icon/충북대(흰배경).png)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 30, 441, 41))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.HowToBtn = QtWidgets.QPushButton(Dialog)
        self.HowToBtn.setGeometry(QtCore.QRect(730, 20, 41, 41))
        self.HowToBtn.setStyleSheet("")
        self.HowToBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Main/icon/QuestionMark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HowToBtn.setIcon(icon3)
        self.HowToBtn.setIconSize(QtCore.QSize(28, 28))
        self.HowToBtn.setFlat(True)
        self.HowToBtn.setObjectName("HowToBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Text To Sound"))
        self.progressBar.setFormat(_translate("Dialog", "%p%"))
        self.FileTypeBox.setItemText(0, _translate("Dialog", "File Format"))
        self.FileTypeBox.setItemText(1, _translate("Dialog", "PDF"))
        self.FileTypeBox.setItemText(2, _translate("Dialog", "DOCX"))
        self.FileTypeBox.setItemText(3, _translate("Dialog", "JPG"))
        self.FileTypeBox.setItemText(4, _translate("Dialog", "PNG"))
        self.Save_path_setting.setText(_translate("Dialog", "저장 경로 설정"))
        self.PreviewButton.setText(_translate("Dialog", "미리보기"))
        self.SoundTypeBox.setItemText(0, _translate("Dialog", "File Format"))
        self.SoundTypeBox.setItemText(1, _translate("Dialog", "MP3"))
        self.SoundTypeBox.setItemText(2, _translate("Dialog", "WAV"))
        self.label_4.setText(_translate("Dialog", "충북대학교 소프트웨어학과"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
