# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'init.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(680, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(680, 480))
        Form.setMaximumSize(QSize(680, 480))
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        Form.setFont(font)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 666, 461))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u".AppleSystemUIFont"])
        font1.setPointSize(65)
        font1.setBold(True)
        self.label.setFont(font1)

        self.horizontalLayout_10.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_9.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_9.addWidget(self.label_2)

        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_9.addItem(self.verticalSpacer_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_12 = QSpacerItem(133, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u".AppleSystemUIFont"])
        font2.setPointSize(20)
        self.label_3.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalSpacer_10 = QSpacerItem(133, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_6 = QSpacerItem(50, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.addItem("1학년")
        self.comboBox.addItem("2학년")
        self.comboBox.addItem("3학년")
        self.comboBox.addItem("본관 특별실")
        self.comboBox.addItem("후관 특별실")
        self.comboBox.addItem("기타 특별실")
        self.comboBox.addItem("과학동")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_8.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
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
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setMinimumSize(QSize(130, 10))
        self.comboBox_2.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_8.addWidget(self.comboBox_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.comboBox_4 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_4.addItem("1학년")
        self.comboBox_4.addItem("2학년")
        self.comboBox_4.addItem("3학년")
        self.comboBox_4.addItem("본관 특별실")
        self.comboBox_4.addItem("후관 특별실")
        self.comboBox_4.addItem("기타 특별실")
        self.comboBox_4.addItem("과학동")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_8.addWidget(self.comboBox_4)

        self.comboBox_3 = QComboBox(self.verticalLayoutWidget)
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
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setMinimumSize(QSize(130, 10))
        self.comboBox_3.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_8.addWidget(self.comboBox_3)

        self.horizontalSpacer_7 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(150, 50))
        self.pushButton.setMaximumSize(QSize(150, 50))

        self.horizontalLayout_7.addWidget(self.pushButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_14)





        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)





        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_15)



        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_16)






        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setFamilies([u".AppleSystemUIFont"])
        font3.setPointSize(50)
        self.label_5.setFont(font3)

        self.horizontalLayout.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Navigation", None))
        self.label.setText(QCoreApplication.translate("Form", u"Welcome", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Seoul HS Navation System", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Start Point", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"End Point", None))


        self.pushButton.setText(QCoreApplication.translate("Form", u"Find", None))

        self.label_5.setText("")
    # retranslateUi

