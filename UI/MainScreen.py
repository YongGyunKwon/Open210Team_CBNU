import sys
import MainUI
from PyQt5.QtWidgets import *
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5 import uic


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
#form_class = uic.loadUiType("MainUI.py")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, MainUI.Ui_Dialog) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #파일 선택 버튼에 기능을 연결하는 코드
        self.SelectFileBtn.clicked.connect(self.PushFileSelButton)
        self.TransFileBtn.clicked.connect(self.PushTransFileButton)
        self.DeleteFileBtn.clicked.connect(self.PushDeleteFileButton)
        self.DeleteFileBtn.setStyleSheet('image:url(Button_UI/DeleteBtn.png); border:0px;')


    ##파일 선택 버튼 동작 메서드##
    def PushFileSelButton(self):
        strlen = 0
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/', "PDF Files (*.pdf)")
        fname = ''.join(fname).split('/')[-1]
        strlen = len(fname) - 17
        self.PDF_FileList.addItem(fname[:strlen])
        print(self.PDF_FileList.currentItem())

    ##파일 변환 버튼 동작 메서드##
    def PushTransFileButton(self):
        ###기능 구현 동작과 연결
        pass

    ##불러온 파일 삭제 동작 메서드
    def PushDeleteFileButton(self):
        ###기능 구현 동작과 연결
        pass

    ##불러온 파일 표시하는 메서드
    def ShowFile(self):
        print(self.fname)

        #self.show

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()