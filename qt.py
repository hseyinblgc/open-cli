# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerefOzPV.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(984, 771)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 640, 941, 61))
        self.horizontalLayout = QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.sendButton = QPushButton(self.verticalLayoutWidget)
        self.sendButton.setObjectName(u"sendButton")
        icon = QIcon(QIcon.fromTheme(u"document-send"))
        self.sendButton.setIcon(icon)
        self.sendButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.sendButton)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 10, 921, 621))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.listWidget.setAutoFillBackground(True)

        self.horizontalLayout_2.addWidget(self.listWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 984, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type Here", None))
        self.sendButton.setText("")
    # retranslateUi