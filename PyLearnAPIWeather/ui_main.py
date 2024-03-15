# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(469, 712)
        icon = QIcon()
        icon.addFile(u"images/weather-forecast-tablet-16486.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color:rgb(100,100, 100);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.search = QPushButton(self.centralwidget)
        self.search.setObjectName(u"search")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        font.setItalic(True)
        self.search.setFont(font)
        self.search.setStyleSheet(u"background-color:rgb(150,150, 150);")

        self.gridLayout.addWidget(self.search, 0, 1, 1, 1)

        self.textbox = QLineEdit(self.centralwidget)
        self.textbox.setObjectName(u"textbox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textbox.sizePolicy().hasHeightForWidth())
        self.textbox.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.textbox.setFont(font1)
        self.textbox.setStyleSheet(u"background-color:rgb(170,170, 170);")
        self.textbox.setReadOnly(False)

        self.gridLayout.addWidget(self.textbox, 0, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 7)
        self.gridLayout.setColumnStretch(0, 7)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(28)
        font2.setItalic(True)
        self.label_4.setFont(font2)
        self.label_4.setPixmap(QPixmap(u"images/weather-forecast-16484.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setIndent(-1)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(16)
        font3.setItalic(True)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(12)
        font4.setItalic(True)
        self.label_2.setFont(font4)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 469, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Weather", None))
        self.search.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.textbox.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"cloudy", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"62%", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"4.2 km/h", None))
    # retranslateUi

