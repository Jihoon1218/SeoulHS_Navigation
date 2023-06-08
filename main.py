import os
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QMessageBox)
from PySide6.QtCore import Signal
from start import Ui_Form
import ctypes
from graphic import way
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)

cal = ctypes.cdll.LoadLibrary("./algorithm.so")
value = cal.pr

translate = {"2-6": 1, "2-7": 2, "2-8": 3, "2-9": 4, "2-10": 5, "2학년부": 6, "정준명스마트교실": 7, "2-11": 8, "2-12": 9,
             "2-13": 10,
             "2-14": 11, "2-5": 12, "2-4": 13, "2-3": 14, "2-2": 15, "2-1": 16, "1학년부": 17, "꿈가람재": 18, "1-1": 19,
             "1-2": 20, "1-3": 21, "진로활동실": 22,
             "1-14": 23, "1-13": 24, "1-12": 25, "1-11": 26, "1-10": 27, "1-9": 28, "1-8": 29, "1-7": 30, "1-6": 31,
             "1-5": 32, "1-4": 33,
             "휴게실(여)": 34, "인쇄실": 35, "평가관리실": 36, "성적처리실": 37, "본관휴게실": 38, "제1교무실": 39, "중앙현관": 40, "행정실": 41,
             "교장실": 42, "본관회의실": 43, "서고": 44, "방송실": 45,"문서고":46,"삼일탑":47, "AI 융합교실": 48, "정보 교과실": 49, "과학정보부": 50,
             "리소스룸": 51, "수학교실 a": 52, "음악실": 53, "화학 교과교실": 54, "화학 실험실": 55, "화학,생명과학 준비실": 56,
             "시약실": 57, "지능형 과학실": 58, "생명과학 실험실": 59, "영어전용교실": 60, "수업나눔카페": 61, "물리 실험실": 62, "물리 교과교실": 63,
             "물리,지구과학 준비실": 64, "과학교사 연구실": 65, "지구과학 교과교실": 66, "지구과학 실험실": 67, "3학년부": 68, "미술실2": 69, "미술 연구실": 70,
             "미술실1": 71, "후관 현관": 72, "제2교무실": 73, "후관회의실": 74, "후관휴게실": 75,
             "수학교실B": 76, "3-8": 77, "3-9": 78, "3-10": 79, "3-11": 80,
             "3-12": 81, "3-13": 82, "3-14": 83, "3-7": 84, "3-6": 85, "3-5": 86, "3-4": 87, "3-3": 88, "3-2": 89,
             "3-1": 90, "성찰교실": 91, "동아리실": 92, "시설관리실": 93,
             "당직실": 94, "보건실": 95, "특수학급교실": 96, "휴게실(남)": 97, "특수교사실": 99, "Wee클래스": 100, "진로상담부": 101, "구내매점": 102,
             "학생회의실": 103, "급식실(1층)": 104, "급식실(2층)": 105, "급식실(3층)": 106, "서온빛1": 107, "서온빛2": 108, "서온빛3": 109,
             "자습실": 115, "도서관": 114, "인왕관 화장실": 111, "시청각실": 113, "학부모회": 112, "학부모아카데미": 110}

class Start(QWidget, Ui_Form):
    on = Signal()

    def __init__(self, parent=None):
        super(Start, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.button_event(True))
        self.comboBox.currentIndexChanged.connect(self.selection_1)
        self.comboBox_4.currentIndexChanged.connect(self.selection_2)

    def keyPressEvent(self, e):
        if (e.key() == 16777220) or (e.key() == 43):
            self.button_event(True)

    def selection_1(self):
        if self.comboBox.currentIndex() == 0:
            self.comboBox_2.clear()
            self.comboBox_2.addItem("1-1")
            self.comboBox_2.addItem("1-2")
            self.comboBox_2.addItem("1-3")
            self.comboBox_2.addItem("1-4")
            self.comboBox_2.addItem("1-5")
            self.comboBox_2.addItem("1-6")
            self.comboBox_2.addItem("1-7")
            self.comboBox_2.addItem("1-8")
            self.comboBox_2.addItem("1-9")
            self.comboBox_2.addItem("1-10")
            self.comboBox_2.addItem("1-11")
            self.comboBox_2.addItem("1-12")
            self.comboBox_2.addItem("1-13")
            self.comboBox_2.addItem("1-14")
        elif self.comboBox.currentIndex() == 1:
            self.comboBox_2.clear()
            self.comboBox_2.addItem("2-1")
            self.comboBox_2.addItem("2-2")
            self.comboBox_2.addItem("2-3")
            self.comboBox_2.addItem("2-4")
            self.comboBox_2.addItem("2-5")
            self.comboBox_2.addItem("2-6")
            self.comboBox_2.addItem("2-7")
            self.comboBox_2.addItem("2-8")
            self.comboBox_2.addItem("2-9")
            self.comboBox_2.addItem("2-10")
            self.comboBox_2.addItem("2-11")
            self.comboBox_2.addItem("2-12")
            self.comboBox_2.addItem("2-13")
            self.comboBox_2.addItem("2-14")
        elif self.comboBox.currentIndex() == 2:
            self.comboBox_2.clear()
            self.comboBox_2.addItem("3-1")
            self.comboBox_2.addItem("3-2")
            self.comboBox_2.addItem("3-3")
            self.comboBox_2.addItem("3-4")
            self.comboBox_2.addItem("3-5")
            self.comboBox_2.addItem("3-6")
            self.comboBox_2.addItem("3-7")
            self.comboBox_2.addItem("3-8")
            self.comboBox_2.addItem("3-9")
            self.comboBox_2.addItem("3-10")
            self.comboBox_2.addItem("3-11")
            self.comboBox_2.addItem("3-12")
            self.comboBox_2.addItem("3-13")
            self.comboBox_2.addItem("3-14")
        elif self.comboBox.currentIndex() == 3:
            self.comboBox_2.clear()
            self.comboBox_2.clear()
            self.comboBox_2.addItem("휴게실(여)")
            self.comboBox_2.addItem("인쇄실")
            self.comboBox_2.addItem("평가관리실")
            self.comboBox_2.addItem("성적처리실")
            self.comboBox_2.addItem("본관휴게실")
            self.comboBox_2.addItem("제1교무실")
            self.comboBox_2.addItem("중앙현관")
            self.comboBox_2.addItem("행정실")
            self.comboBox_2.addItem("교장실")
            self.comboBox_2.addItem("본관회의실")
            self.comboBox_2.addItem("서고")
            self.comboBox_2.addItem("방송실")
            self.comboBox_2.addItem("문서고")
            self.comboBox_2.addItem("1학년부")
            self.comboBox_2.addItem("꿈가람재")
            self.comboBox_2.addItem("정준명스마트교실")
            self.comboBox_2.addItem("2학년부")
            self.comboBox_2.addItem("진로활동실")
        elif self.comboBox.currentIndex() == 4:
            self.comboBox_2.clear()
            self.comboBox_2.addItem("미술실2")
            self.comboBox_2.addItem("미술 연구실")
            self.comboBox_2.addItem("미술실1")
            self.comboBox_2.addItem("후관 현관")
            self.comboBox_2.addItem("제2교무실")
            self.comboBox_2.addItem("후관회의실")
            self.comboBox_2.addItem("후관휴게실")
            self.comboBox_2.addItem("수학교실B")
            self.comboBox_2.addItem("성찰교실")
            self.comboBox_2.addItem("동아리실")
            self.comboBox_2.addItem("3학년부실")
        elif self.comboBox.currentIndex() == 5:
            self.comboBox_2.clear()
            self.comboBox_2.addItem("보건실")
            self.comboBox_2.addItem("특수학급교실")
            self.comboBox_2.addItem("휴게실(남)")
            self.comboBox_2.addItem("특수교사실")
            self.comboBox_2.addItem("Wee클래스")
            self.comboBox_2.addItem("진로상담부")
            self.comboBox_2.addItem("구내매점")
            self.comboBox_2.addItem("학생회의실")
            self.comboBox_2.addItem("삼일탑")
            self.comboBox_2.addItem("급식실(1층)")
            self.comboBox_2.addItem("급식실(2층)")
            self.comboBox_2.addItem("급식실(3층)")
            self.comboBox_2.addItem("서온빛")
            self.comboBox_2.addItem("서온빛1")
            self.comboBox_2.addItem("서온빛2")
            self.comboBox_2.addItem("서온빛3")
            self.comboBox_2.addItem("자습실")
            self.comboBox_2.addItem("도서관")
            self.comboBox_2.addItem("인왕관 화장실")
            self.comboBox_2.addItem("학부모아카데미")
            self.comboBox_2.addItem("시청각실")
            self.comboBox_2.addItem("학부모회")
        elif self.comboBox.currentIndex() == 6:
            self.comboBox_2.clear()
            self.comboBox_2.addItem("물리 실험실")
            self.comboBox_2.addItem("물리 교과교실")
            self.comboBox_2.addItem("물리,지구과학 준비실")
            self.comboBox_2.addItem("과학교사 연구실")
            self.comboBox_2.addItem("지구과학 교과교실")
            self.comboBox_2.addItem("지구과학 실험실")
            self.comboBox_2.addItem("화학 교과교실")
            self.comboBox_2.addItem("화학 실험실")
            self.comboBox_2.addItem("화학,생명과학 준비실")
            self.comboBox_2.addItem("시약실")
            self.comboBox_2.addItem("지능형 과학실")
            self.comboBox_2.addItem("생명과학 실험실")
            self.comboBox_2.addItem("AI 융합교실")
            self.comboBox_2.addItem("정보 교과실")
            self.comboBox_2.addItem("과학정보부")
            self.comboBox_2.addItem("리소스룸")
            self.comboBox_2.addItem("수학교실 a")
            self.comboBox_2.addItem("음악실")
            self.comboBox_2.addItem("영어전용교실")
            self.comboBox_2.addItem("수업나눔카페")
        else:
            self.comboBox_2.clear()

    def selection_2(self):
        if self.comboBox_4.currentIndex() == 0:
            self.comboBox_3.clear()
            self.comboBox_3.addItem("1-1")
            self.comboBox_3.addItem("1-2")
            self.comboBox_3.addItem("1-3")
            self.comboBox_3.addItem("1-4")
            self.comboBox_3.addItem("1-5")
            self.comboBox_3.addItem("1-6")
            self.comboBox_3.addItem("1-7")
            self.comboBox_3.addItem("1-8")
            self.comboBox_3.addItem("1-9")
            self.comboBox_3.addItem("1-10")
            self.comboBox_3.addItem("1-11")
            self.comboBox_3.addItem("1-12")
            self.comboBox_3.addItem("1-13")
            self.comboBox_3.addItem("1-14")
        elif self.comboBox_4.currentIndex() == 1:
            self.comboBox_3.clear()
            self.comboBox_3.addItem("2-1")
            self.comboBox_3.addItem("2-2")
            self.comboBox_3.addItem("2-3")
            self.comboBox_3.addItem("2-4")
            self.comboBox_3.addItem("2-5")
            self.comboBox_3.addItem("2-6")
            self.comboBox_3.addItem("2-7")
            self.comboBox_3.addItem("2-8")
            self.comboBox_3.addItem("2-9")
            self.comboBox_3.addItem("2-10")
            self.comboBox_3.addItem("2-11")
            self.comboBox_3.addItem("2-12")
            self.comboBox_3.addItem("2-13")
            self.comboBox_3.addItem("2-14")
        elif self.comboBox_4.currentIndex() == 2:
            self.comboBox_3.clear()
            self.comboBox_3.addItem("3-1")
            self.comboBox_3.addItem("3-2")
            self.comboBox_3.addItem("3-3")
            self.comboBox_3.addItem("3-4")
            self.comboBox_3.addItem("3-5")
            self.comboBox_3.addItem("3-6")
            self.comboBox_3.addItem("3-7")
            self.comboBox_3.addItem("3-8")
            self.comboBox_3.addItem("3-9")
            self.comboBox_3.addItem("3-10")
            self.comboBox_3.addItem("3-11")
            self.comboBox_3.addItem("3-12")
            self.comboBox_3.addItem("3-13")
            self.comboBox_3.addItem("3-14")
        elif self.comboBox_4.currentIndex() == 3:
            self.comboBox_3.clear()
            self.comboBox_3.addItem("휴게실(여)")
            self.comboBox_3.addItem("인쇄실")
            self.comboBox_3.addItem("평가관리실")
            self.comboBox_3.addItem("성적처리실")
            self.comboBox_3.addItem("본관휴게실")
            self.comboBox_3.addItem("제1교무실")
            self.comboBox_3.addItem("중앙현관")
            self.comboBox_3.addItem("행정실")
            self.comboBox_3.addItem("교장실")
            self.comboBox_3.addItem("본관회의실")
            self.comboBox_3.addItem("서고")
            self.comboBox_3.addItem("방송실")
            self.comboBox_3.addItem("문서고")
            self.comboBox_3.addItem("1학년부")
            self.comboBox_3.addItem("꿈가람재")
            self.comboBox_3.addItem("정준명스마트교실")
            self.comboBox_3.addItem("2학년부")
            self.comboBox_3.addItem("진로활동실")
        elif self.comboBox_4.currentIndex() == 4:
            self.comboBox_3.clear()
            self.comboBox_3.addItem("미술실2")
            self.comboBox_3.addItem("미술 연구실")
            self.comboBox_3.addItem("미술실1")
            self.comboBox_3.addItem("후관 현관")
            self.comboBox_3.addItem("제2교무실")
            self.comboBox_3.addItem("후관회의실")
            self.comboBox_3.addItem("후관휴게실")
            self.comboBox_3.addItem("수학교실B")
            self.comboBox_3.addItem("성찰교실")
            self.comboBox_3.addItem("동아리")
            self.comboBox_3.addItem("3학년부실")
        elif self.comboBox_4.currentIndex() == 5:
            self.comboBox_3.clear()
            self.comboBox_3.addItem("보건실")
            self.comboBox_3.addItem("특수학급교실")
            self.comboBox_3.addItem("휴게실(남)")
            self.comboBox_3.addItem("특수교사실")
            self.comboBox_3.addItem("Wee클래스")
            self.comboBox_3.addItem("진로상담부")
            self.comboBox_3.addItem("구내매점")
            self.comboBox_3.addItem("학생회의실")
            self.comboBox_3.addItem("삼일탑")
            self.comboBox_3.addItem("급식실(1층)")
            self.comboBox_3.addItem("급식실(2층)")
            self.comboBox_3.addItem("급식실(3층)")
            self.comboBox_3.addItem("서온빛")
            self.comboBox_3.addItem("서온빛1")
            self.comboBox_3.addItem("서온빛2")
            self.comboBox_3.addItem("서온빛3")
            self.comboBox_3.addItem("자습실")
            self.comboBox_3.addItem("도서관")
            self.comboBox_3.addItem("인왕관 화장실")
            self.comboBox_3.addItem("학부모아카데미")
            self.comboBox_3.addItem("시청각실")
            self.comboBox_3.addItem("학부모회")
        elif self.comboBox_4.currentIndex() == 6:
            self.comboBox_3.clear()
            self.comboBox_3.addItem("물리 실험실")
            self.comboBox_3.addItem("물리 교과교실")
            self.comboBox_3.addItem("물리,지구과학 준비실")
            self.comboBox_3.addItem("과학교사 연구실")
            self.comboBox_3.addItem("지구과학 교과교실")
            self.comboBox_3.addItem("지구과학 실험실")
            self.comboBox_3.addItem("화학 교과교실")
            self.comboBox_3.addItem("화학 실험실")
            self.comboBox_3.addItem("화학,생명과학 준비실")
            self.comboBox_3.addItem("시약실")
            self.comboBox_3.addItem("지능형 과학실")
            self.comboBox_3.addItem("생명과학 실험실")
            self.comboBox_3.addItem("AI 융합교실")
            self.comboBox_3.addItem("정보 교과실")
            self.comboBox_3.addItem("과학정보부")
            self.comboBox_3.addItem("리소스룸")
            self.comboBox_3.addItem("수학교실 a")
            self.comboBox_3.addItem("음악실")
            self.comboBox_3.addItem("영어전용교실")
            self.comboBox_3.addItem("수업나눔카페")
        else:
            self.comboBox_3.clear()

    def button_event(self, bool):
        if True:
            if bool:
                f = open("test.txt", 'r')
                one_text = self.comboBox_2.currentText()
                two_text = self.comboBox_3.currentText()
                value(int(translate[str(one_text)]), int(translate[str(two_text)]))
                Line = f.readline()
                pos = []
                tmp = 0
                for i in Line:
                    if i == ' ':
                        pos.append(tmp)
                        tmp = 0
                    else:
                        tmp = int(str(tmp) + str(i))
                way(pos)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Start()
    login.show()
    app.exec()
