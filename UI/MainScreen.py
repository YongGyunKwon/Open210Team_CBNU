import sys
from PyQt5.QtWidgets import *
import MainUI
from tqdm.notebook import tqdm

from Fuction.function import *
from Fuction.Image_Converter import *

"""
A. 변환후 저장 경로가 반환된다면?
1) 사운드 파일의 이름은 사용자 마음대로 설정할 수 있음(추후 시간있을 때 구현)
2) 반환된 저장 경로를 받아와, 그 경로를 이용해 Sound_FileList에 파일 이름만 띄워줌

B. 변환후 저장 경로가 따로 반환되지 않는다면?
1) 사운드 파일의 이름은 무조건 시각 파일의 이름과 같게 설정
2) 사운드 파일의 경로를 변환 전후에 상관없이, 미리 받아온 경로를 통해 뒤에 사운드 파일 이름을 붙여 경로를 만듦 
->    받아온 경로/시각파일이름-(시각 파일의 확장자)+(음성 파일의 확장자)   
ex> C:/Users/ehdrb/Desktop/veiwfile.pdf-(pdf)+(mp3)
"""


# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, MainUI.Ui_Dialog):
    num = 17  # 문자열에 들어간 지워야 될 확장자 이름의 크기
    strlen = 0  # 문자열 출력할 때, 0~strlen까지 출력
    FileType = ""  # 시각파일형식
    SoundType = ""  # 음성파일형식
    PDF_name = ""  # 시각파일이름
    Sound_Name = ""  # 음성파일이름
    File_Path = []  # 시각파일을 저장할 경로
    Sound_Path = ""  # 음성파일을 저장할 경로
    Temp_Path = []  # 음성파일을 저장할 경로를 임시로 저장
    i = 0  # 추가된 시각파일의 개수
    Trans_list = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 파일 선택 버튼에 기능을 연결하는 코드
        self.AddFileBtn.clicked.connect(self.Push_AddButton)
        self.TransFileBtn.clicked.connect(self.Push_TransFileButton)
        self.DeleteFileBtn.clicked.connect(self.Push_DeleteButton)
        self.Save_path_setting.clicked.connect(self.SavePath)
        # self.PreviewButton.clicked.connect(self.Preview)
        self.HowToBtn.clicked.connect(self.HowTo)

    ##파일 추가 버튼 동작 메서드## #완료
    # FilePath 라는 변수안에 경로 추가 되있음
    def Push_AddButton(self):
        err = self.Select_FileType()
        if self.FileType == "File Format":
            self.warning_1()
        if err:
            self.PDF_FileList.addItem(self.PDF_name[:self.strlen])
            print(self.PDF_FileList.currentItem())
        print(self.File_Path)

    ##시각 파일의 형식에 따른 처리##
    def Select_FileType(self):
        self.FileType = self.FileTypeBox.currentText()  # 파일형식선택
        if self.FileType == "PDF":
            self.num = 17
            self.File_Path += QFileDialog.getOpenFileName(self, 'Open file', '/', "PDF Files (*.pdf)")
            if self.File_Path[-1] == '':
                del self.File_Path[-1]
                del self.File_Path[-1]
                return 0
            self.PDF_name = ''.join(self.File_Path).split('/')[-1]
            self.strlen = len(self.PDF_name) - self.num
        elif self.FileType == "DOCX":
            self.num = 19
            self.File_Path += QFileDialog.getOpenFileName(self, 'Open file', '/', "DOCX Files (*.docx)")
            if self.File_Path[-1] == '':
                del self.File_Path[-1]
                del self.File_Path[-1]
                return 0
            self.PDF_name = ''.join(self.File_Path).split('/')[-1]
            self.strlen = len(self.PDF_name) - self.num
        elif self.FileType == "JPG":
            self.num = 17
            self.File_Path += QFileDialog.getOpenFileName(self, 'Open file', '/', "JPG Files (*.jpg)")
            if self.File_Path[-1] == '':
                del self.File_Path[-1]
                return 0
            self.PDF_name = ''.join(self.File_Path).split('/')[-1]
            self.strlen = len(self.PDF_name) - self.num
        elif self.FileType == "PNG":
            self.num = 17
            self.File_Path += QFileDialog.getOpenFileName(self, 'Open file', '/', "PNG Files (*.png)")
            if self.File_Path[-1] == '':
                del self.File_Path[-1]
                return 0
            self.PDF_name = ''.join(self.File_Path).split('/')[-1]
            self.strlen = len(self.PDF_name) - self.num
        else:
            return 0
        return 1

    ##파일 변환 버튼 동작 메서드##
    def Push_TransFileButton(self):
        err = 1
        self.SoundType = self.SoundTypeBox.currentText()  # 파일형식선택
        if self.SoundType == "File Format":
            self.warning_2()
            err = 0
        if self.Sound_Path == "":
            self.warning_3()
            err = 0

        if err:
            ###기능 구현 동작과 연결
            if (self.File_Path[1] == 'PDF Files (*.pdf)'):
                '''
                print(self.File_Path[0])
                transtext = read_pdf_file1(self.File_Path[0])
                print(transtext)
                transpath = self.Sound_Path + "/" + self.PDF_name[:self.strlen - 5]
                print(transpath)
                g_tts(transtext, transpath, self.SoundType)
                '''
                print("This is PDF")

                abs = self.File_Path
                print("abs is", abs)
                print("len is", len(abs))

                for j in range(0, len(abs)):
                    print("j is", j)
                    if (j % 2 == 0):
                        print(self.File_Path[j])
                        transtext1 = Image_Converter2(self.File_Path[j])
                        print("This is text1", transtext1)
                        print("Strlen is ", len(self.File_Path[j]))
                        transpath2 = self.File_Path[j]
                        print("Transpath2 is ", transpath2)
                        # transpath1 = self.Sound_Path + "/" + self.PDF_name[:self.strlen - 4]
                        transpath1 = transpath2[:-4].split('/')[-1]
                        self.Trans_list.append(transpath1 + '.' + self.SoundType)
                        print(transpath1)
                        g_tts(transtext1, self.Sound_Path + '/' + transpath1, self.SoundType.lower())
                        print("complete??")
                    print("next")
                self.progressBar.setValue(100)


            elif (self.File_Path[1] == 'JPG Files (*.jpg)'):
                '''
                print(self.File_Path[0])
                transtext1 = image_to_string1(self.File_Path[0])
                print("This is text1", transtext1)
                transpath1 = self.Sound_Path + "/" + self.PDF_name[:self.strlen - 4]
                print(transpath1)

                g_tts(transtext1, transpath1, self.SoundType)
                '''

                print("This is jpg")
                abs = self.File_Path
                print("abs is", abs)
                print("len is", len(abs))

                setval = 20
                for j in range(0, len(abs)):
                    print("j is", j)
                    if (j % 2 == 0):
                        print(self.File_Path[j])
                        transtext1 = image_to_string1(self.File_Path[j])
                        print("This is text1", transtext1)
                        print("Strlen is ", len(self.File_Path[j]))
                        transpath2 = self.File_Path[j]
                        print("Transpath2 is ", transpath2)
                        # transpath1 = self.Sound_Path + "/" + self.PDF_name[:self.strlen - 4]
                        transpath1 = transpath2[:-4].split('/')[-1]  # 순수 파일 이름
                        self.Trans_list.append(transpath1 + '.' + self.SoundType)
                        print(transpath1)
                        g_tts(transtext1, self.Sound_Path + '/' + transpath1, self.SoundType.lower())

                        print("complete??")
                        setval += 20
                        self.progressBar.setValue(setval)
                        print(j, end=' ')
                        print("progress")
                    print("next")
                self.progressBar.setValue(100)

            elif (self.File_Path[1] == 'PNG Files (*.png)'):
                print("This is png")
                '''
                print(self.File_Path[0])
                transtext1 = image_to_string1(self.File_Path[0])
                print(transtext1)
                transpath1 = self.Sound_Path + "/" + self.PDF_name[:self.strlen - 4]
                print(transpath1)
                g_tts(transtext1, transpath1, self.SoundType)
                '''
                abs = self.File_Path
                setval = 20
                for j in range(0, len(abs)):
                    print("j is", j)
                    if (j % 2 == 0):
                        print(self.File_Path[j])
                        transtext1 = image_to_string1(self.File_Path[j])
                        print("This is text1", transtext1)
                        print("Strlen is ", len(self.File_Path[j]))
                        transpath2 = self.File_Path[j]
                        print("Transpath2 is ", transpath2)
                        # transpath1 = self.Sound_Path + "/" + self.PDF_name[:self.strlen - 4]
                        transpath1 = transpath2[:-4].split('/')[-1]
                        self.Trans_list.append(transpath1 + '.' + self.SoundType)
                        print(transpath1)

                        g_tts(transtext1, self.Sound_Path + '/' + transpath1, self.SoundType.lower())
                        print("complete??")
                        setval += 20
                        self.progressBar.setValue(setval)

                    print("next")
                self.progressBar.setValue(100)
                # docx 완료
            elif (self.File_Path[1] == "DOCX Files (*.docx)"):
                '''    
                print(self.File_Path[0])
                transtext = read_docx_file(self.File_Path[0])
                print(transtext)
                transpath = self.Sound_Path + "/" + self.PDF_name[:self.strlen - 5]
                print(transpath)

                g_tts(transtext, transpath, self.SoundType)
                '''
                abs = self.File_Path
                setval = 20
                for j in range(0, len(abs)):
                    print("j is", j)
                    if (j % 2 == 0):
                        print(self.File_Path[j])
                        transtext1 = read_docx_file(self.File_Path[j])
                        print("This is text1", transtext1)
                        print("Strlen is ", len(self.File_Path[j]))
                        transpath2 = self.File_Path[j]
                        print("Transpath2 is ", transpath2)
                        # transpath1 = self.Sound_Path + "/" + self.PDF_name[:self.strlen - 4]
                        transpath1 = transpath2[:-5].split('/')[-1]
                        self.Trans_list.append(transpath1 + '.' + self.SoundType)
                        print(transpath1)

                        g_tts(transtext1, self.Sound_Path + '/' + transpath1, self.SoundType.lower())
                        print("complete??")
                        setval += 20
                        self.progressBar.setValue(setval)

                    print("next")
                self.progressBar.setValue(100)

            self.ShowFile()  # 기능 구현 코드(파일 변환 코드)에서 변환이 완료되면 변환된 파일 표시

    ##불러온 파일 삭제 동작 메서드## #완료
    def Push_DeleteButton(self):
        if self.File_Path == []:
            return
        item = self.PDF_FileList.currentItem()
        if (item == None):
            return
        N = 2 * self.PDF_FileList.currentRow()  # 선택된 항목이 몇 번째인지 반환
        self.PDF_FileList.takeItem(self.PDF_FileList.row(item))  # ListWidget에서 삭제
        del self.File_Path[N]  # 리스트에서 파일 삭제
        del self.File_Path[N]  # 리스트에서 파일의 확장자 삭제
        ###기능 구현 동작과 연결

    def SavePath(self):
        self.Sound_Path = QFileDialog.getExistingDirectory(self, 'Open Folder', 'c:/')  # Sound_Path에 저장할 경로 저장
        self.SavePathEDT.setPlainText(self.Sound_Path)  # 설정된 저장경로를 LineEdit 박스에 표시

    ##불러온 파일 표시하는 메서드 -> 파일변환버튼 함수에서 불러와야 될~
    def ShowFile(self):
        for j in self.Trans_list:
            self.Sound_FileList.addItem(j)
            print(self.Sound_FileList.currentItem())

    def Preview(self):
        files = self.File_Path[0]
        Image_Converter(files)

    ##경고문 띄우기
    def warning_1(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("문서파일의 형식을 정해주십시오")
        msg.setWindowTitle("Warning")
        msg.exec_()

    def warning_2(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("음성파일의 형식을 정해주십시오")
        msg.setWindowTitle("Warning")
        msg.exec_()

    def warning_3(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("저장경로를 설정해 정해주십시오")
        msg.setWindowTitle("Warning")
        msg.exec_()

    # 사용방법
    def HowTo(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("""
        1. 변환할 문서파일의 형식 설정
        2. 변환될 음성파일의 형식과 저장할 경로 설정
        3. + 버튼 클릭해 변환하려는 문서파일 추가
        4. 문서파일이 잘못 추가됐을 떄 - 버튼을 클릭해 삭제
        5. 가운데 <-> 변환버튼 클릭해 변환
        6. 변환의 검사가 필요하면 미리보기 버튼 클릭
        """)
        msg.setWindowTitle("HowTo")
        msg.exec_()


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()