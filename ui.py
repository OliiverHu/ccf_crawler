# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
# from ccf_name_crawler import update_info


# noinspection PyArgumentList
class UIMainWindow(object):

    def __init__(self):
        super().__init__()

        # main window size policy
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 716)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(1)
        size_policy.setVerticalStretch(1)
        size_policy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(size_policy)

        # menu bar related items init
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuUpdate = QtWidgets.QMenu(self.menubar)
        self.menuFilter = QtWidgets.QMenu(self.menubar)

        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionFilter = QtWidgets.QAction(MainWindow)
        self.actionFilter.setObjectName("actionFilter")

        # main window widgets
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(on_click)

        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setObjectName("toolBox")

        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.checkBox_3 = QtWidgets.QCheckBox(self.page)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_2.addWidget(self.checkBox_3, 0, 0, 1, 1)

        self.checkBox_8 = QtWidgets.QCheckBox(self.page)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_2.addWidget(self.checkBox_8, 1, 0, 1, 1)

        self.checkBox_9 = QtWidgets.QCheckBox(self.page)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_2.addWidget(self.checkBox_9, 2, 0, 1, 1)

        self.checkBox_2 = QtWidgets.QCheckBox(self.page)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 3, 0, 1, 1)

        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.page2)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.checkBox_4 = QtWidgets.QCheckBox(self.page2)
        self.checkBox_4.setObjectName("checkBox_4")

        # set the layout of Crawl button
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer_item1)
        self.horizontalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer_item2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        # page 1 of toolBox
        self.toolBox.setCurrentIndex(0)  # default: start at the first page
        self.page.setGeometry(QtCore.QRect(0, 0, 658, 546))
        self.toolBox.addItem(self.page, "")

        # page 2 of toolBox
        self.page2.setGeometry(QtCore.QRect(0, 0, 658, 546))
        self.gridLayout_3.addWidget(self.checkBox_4, 0, 0, 1, 1)
        self.toolBox.addItem(self.page2, "")
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.setup_menu(MainWindow)
        self.translate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setup_menu(self, MainWindow):
        # menubar of the mainwindow
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile.setObjectName("menuFile")
        self.menuUpdate.setObjectName("menuUpdate")
        self.menuFilter.setObjectName("menuFilter")
        MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow) what is status bar?
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        self.actionImport.setObjectName("actionImport")
        self.actionExport.setObjectName("actionExport")

        # set the functionality of Exit menu item
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setStatusTip('Exit application')
        self.actionExit.triggered.connect(MainWindow.close)

        # set the functionality of Update menu item
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionUpdate.setShortcut('Ctrl+U')
        # self.actionUpdate.triggered.connect(on_click)

        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuUpdate.menuAction())
        self.menubar.addAction(self.menuFilter.menuAction())

    def translate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CCF Crawler"))
        MainWindow.setWindowIcon(QtGui.QIcon("home.jpg"))
        self.pushButton.setText(_translate("MainWindow", "Crawl"))
        self.checkBox_3.setText(_translate("MainWindow", "name of conference or transaction1"))
        self.checkBox_8.setText(_translate("MainWindow", "name of conference or transaction2"))
        self.checkBox_9.setText(_translate("MainWindow", "name of conference or transaction3"))
        self.checkBox_2.setText(_translate("MainWindow", "name of conference or transaction4"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "name of category1"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page2), _translate("MainWindow", "name of category2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuUpdate.setTitle(_translate("MainWindow", "Update"))
        self.menuFilter.setTitle(_translate("MainWindow", "Filter"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionFilter.setText(_translate("MainWindow", "Filter"))


def on_click():
    print("test")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # noinspection PyArgumentList
    MainWindow = QtWidgets.QMainWindow()
    ui = UIMainWindow()
    ui.__init__()
    MainWindow.show()
    sys.exit(app.exec_())
