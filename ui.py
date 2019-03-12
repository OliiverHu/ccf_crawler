# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from ccf_name_crawler import update_info
import xlrd


# noinspection PyArgumentList
class UIMainWindow(object):

    def __init__(self, MainWindow):
        super().__init__()
        # length of the excel file
        self.length = 10
        self.xl_file = xlrd.open_workbook('ccf_names&links.xls')
        self.checkbox_list = []
        self.two_d_checkbox_list = [[None]*6 for col in range(self.length)]
        self.checkbox_link_list = []

        # main window size policy
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('home.png'))
        MainWindow.resize(750, 900)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(1)
        size_policy.setVerticalStretch(1)
        size_policy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(size_policy)

        # menu bar related items init
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuUpdate = QtWidgets.QMenu(self.menubar)
        self.menuUpdate.setObjectName("menuUpdate")

        self.menuFilter = QtWidgets.QMenu(self.menubar)
        self.menuFilter.setObjectName("menuFilter")

        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
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
        # self.pushButton.clicked.connect()

        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setObjectName("toolBox")

        # self.page = QtWidgets.QWidget()
        # self.page.setObjectName("page")
        #
        # self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        # self.gridLayout_2.setObjectName("gridLayout_2")
        #
        # self.checkBox_3 = QtWidgets.QCheckBox(self.page)
        # self.checkBox_3.setObjectName("checkBox_3")
        # self.gridLayout_2.addWidget(self.checkBox_3, 0, 0, 1, 1)
        #
        # self.checkBox_8 = QtWidgets.QCheckBox(self.page)
        # self.checkBox_8.setObjectName("checkBox_8")
        # self.gridLayout_2.addWidget(self.checkBox_8, 1, 0, 1, 1)
        #
        # self.checkBox_9 = QtWidgets.QCheckBox(self.page)
        # self.checkBox_9.setObjectName("checkBox_9")
        # self.gridLayout_2.addWidget(self.checkBox_9, 2, 0, 1, 1)
        #
        # self.checkBox_2 = QtWidgets.QCheckBox(self.page)
        # self.checkBox_2.setObjectName("checkBox_2")
        # self.gridLayout_2.addWidget(self.checkBox_2, 3, 0, 1, 1)
        #
        # self.page2 = QtWidgets.QWidget()
        # self.page2.setObjectName("page2")
        #
        # self.gridLayout_3 = QtWidgets.QGridLayout(self.page2)
        # self.gridLayout_3.setObjectName("gridLayout_3")
        #
        # self.checkBox_4 = QtWidgets.QCheckBox(self.page2)
        # self.checkBox_4.setObjectName("checkBox_4")

        # set the layout of Crawl button
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer_item1)
        self.horizontalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer_item2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        # # page 1 of toolBox
        self.toolBox.setCurrentIndex(0)  # default: start at the first page
        # self.page.setGeometry(QtCore.QRect(0, 0, 658, 546))
        # self.toolBox.addItem(self.page, "")
        #
        # # page 2 of toolBox
        # self.page2.setGeometry(QtCore.QRect(0, 0, 658, 546))
        # self.gridLayout_3.addWidget(self.checkBox_4, 0, 0, 1, 1)
        # self.toolBox.addItem(self.page2, "")
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.set_length()
        self.setup_menu(MainWindow)
        self.setup_toolbox_tab()
        self.translate_ui(MainWindow)
        self.xlrd_reader()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def set_length(self):
        try:
            # xl_file = xlrd.open_workbook('ccf_names&links.xls')
            table = self.xl_file.sheet_by_index(0)
            cols = table.ncols
            self.length = int(cols / 3)
        except FileNotFoundError:
            self.length = 10

    def xlrd_reader(self):
        table = self.xl_file.sheet_by_index(0)
        item_count = -1
        for i in range(self.length):  # traverse tabs(cols)
            row_count = table.col_values(3 * i + 1)
            while row_count[-1] == '':
                row_count.pop()
            k = 0  # count the blank cell in xlfile in order to distinguish from name to name
            at_list = []
            bt_list = []
            ct_list = []
            ac_list = []
            bc_list = []
            cc_list = []
            for j in range(len(row_count)):  # traverse rows
                if table.cell_value(j, 3 * i + 1) == '':
                    k += 1
                else:
                    item_count += 1
                if k == 1 or k == 5:
                    pass
                elif k == 2:
                    if table.cell_value(j, 3 * i) != 'A' and 'B' and 'C':
                        at_list.append([self.checkbox_list[item_count], table.cell_value(j, 3 * i),
                                        table.cell_value(j, 3 * i + 1), table.cell_value(j, 3 * i + 2)])
                elif k == 3:
                    if table.cell_value(j, 3 * i) != 'A' and 'B' and 'C':
                        bt_list.append([self.checkbox_list[item_count], table.cell_value(j, 3 * i),
                                        table.cell_value(j, 3 * i + 1), table.cell_value(j, 3 * i + 2)])
                elif k == 4:
                    if table.cell_value(j, 3 * i) != 'A' and 'B' and 'C':
                        ct_list.append([self.checkbox_list[item_count], table.cell_value(j, 3 * i),
                                        table.cell_value(j, 3 * i + 1), table.cell_value(j, 3 * i + 2)])
                elif k == 6:
                    if table.cell_value(j, 3 * i) != 'A' and 'B' and 'C':
                        ac_list.append([self.checkbox_list[item_count], table.cell_value(j, 3 * i),
                                        table.cell_value(j, 3 * i + 1), table.cell_value(j, 3 * i + 2)])
                elif k == 7:
                    if table.cell_value(j, 3 * i) != 'A' and 'B' and 'C':
                        bc_list.append([self.checkbox_list[item_count], table.cell_value(j, 3 * i),
                                        table.cell_value(j, 3 * i + 1), table.cell_value(j, 3 * i + 2)])
                elif k == 8:
                    if table.cell_value(j, 3 * i) != 'A' and 'B' and 'C':
                        cc_list.append([self.checkbox_list[item_count], table.cell_value(j, 3 * i),
                                        table.cell_value(j, 3 * i + 1), table.cell_value(j, 3 * i + 2)])
            self.two_d_checkbox_list[i][0] = at_list
            self.two_d_checkbox_list[i][1] = bt_list
            self.two_d_checkbox_list[i][2] = ct_list
            self.two_d_checkbox_list[i][3] = ac_list
            self.two_d_checkbox_list[i][4] = bc_list
            self.two_d_checkbox_list[i][5] = cc_list
            # print(item_count) this var is right
        # print(self.two_d_checkbox_list)
        # print(self.checkbox_list)


    def setup_menu(self, MainWindow):
        # menubar of the mainwindow
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 26))

        MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow) what is status bar?
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        # set the functionality of Exit menu item
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setStatusTip('Exit application')
        self.actionExit.triggered.connect(MainWindow.close)

        # set the functionality of Update menu item
        self.actionUpdate.setShortcut('Ctrl+U')
        self.actionUpdate.triggered.connect(update_info)

        # binding sub menu to menuFile
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        # binding sub menu to menuUpdate
        self.menuUpdate.addAction(self.actionUpdate)

        # binding sub menu to menuFilter
        self.menuFilter.addAction(self.actionFilter)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuUpdate.menuAction())
        self.menubar.addAction(self.menuFilter.menuAction())

    def setup_toolbox_tab(self):
        length = self.length
        # length = 1
        ccf_table = self.xl_file.sheet_by_index(0)
        # ft = tkinter.font.Font(family='Fixdsys', size=14, weight=tkinter.font.BOLD)
        # label = Label(canvas, text=ccf_table.cell_value(0, 3 * start_pos), anchor=NW, font=ft)
        # label.pack(side=TOP, padx=5, pady=5)

        for i in range(int(length)):
            page = QtWidgets.QWidget()
            page.setObjectName("page")
            # gridLayout = QtWidgets.QGridLayout()
            # gridLayout.setObjectName("gridLayout")

            self.setup_checkbox(i, page)
            page.setGeometry(QtCore.QRect(0, 0, 658, 546))
            self.toolBox.addItem(page, ccf_table.cell_value(0, 3 * i))

    def setup_checkbox(self, col_index, tab):
        ccf_table = self.xl_file.sheet_by_index(0)
        start_pos = col_index
        gridLayout2 = QtWidgets.QGridLayout(tab)

        title = ccf_table.cell_value(0, 3 * start_pos)
        label = QtWidgets.QLabel()
        label.setText(title)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setFont(QtGui.QFont("Roman times", 20, QtGui.QFont.Bold))
        gridLayout2.addWidget(label, 0, 0, 1, 1)

        row_count = ccf_table.col_values(3 * start_pos + 1)
        while row_count[-1] == '':
            row_count.pop()
        # print(len(row_count))
        flag = 0
        # checkbox_list = []
        for i in range(1, len(row_count)+1):
            # print(ccf_table.cell_value(i, 3*start_pos+1))
            if ccf_table.cell_value(i-1, 3*start_pos+1) == '':
                flag += 1
                if flag == 1:
                    label = QtWidgets.QLabel()
                    label.setText("期刊")
                    label.setAlignment(QtCore.Qt.AlignCenter)
                    label.setFont(QtGui.QFont("Roman times", 15, QtGui.QFont.Bold))
                    gridLayout2.addWidget(label, i, 0, 1, 1)
                elif flag == 2:
                    checkbox = QtWidgets.QCheckBox("A类", tab)
                    checkbox.setObjectName("A")

                    '''change only one certain widget in the app'''
                    # checkbox.setStyleSheet("font: 15pt")
                    checkbox.setFont(QtGui.QFont("Roman times", 18, QtGui.QFont.Bold))
                    gridLayout2.addWidget(checkbox, i, 0, 1, 1)
                elif flag == 3:
                    checkbox = QtWidgets.QCheckBox("B类", tab)
                    checkbox.setObjectName("B")
                    checkbox.setFont(QtGui.QFont("Roman times", 18, QtGui.QFont.Bold))
                    gridLayout2.addWidget(checkbox, i, 0, 1, 1)
                elif flag == 4:
                    checkbox = QtWidgets.QCheckBox("C类", tab)
                    checkbox.setObjectName("C")
                    checkbox.setFont(QtGui.QFont("Roman times", 18, QtGui.QFont.Bold))
                    gridLayout2.addWidget(checkbox, i, 0, 1, 1)
                elif flag == 5:
                    label = QtWidgets.QLabel()
                    label.setText("会议")
                    label.setAlignment(QtCore.Qt.AlignCenter)
                    label.setFont(QtGui.QFont("Roman times", 15, QtGui.QFont.Bold))
                    gridLayout2.addWidget(label, i, 0, 1, 1)
                elif flag == 6:
                    checkbox = QtWidgets.QCheckBox("A类", tab)
                    checkbox.setObjectName("A")
                    checkbox.setFont(QtGui.QFont("Roman times", 18, QtGui.QFont.Bold))
                    gridLayout2.addWidget(checkbox, i, 0, 1, 1)
                elif flag == 7:
                    checkbox = QtWidgets.QCheckBox("B类", tab)
                    checkbox.setObjectName("B")
                    checkbox.setFont(QtGui.QFont("Roman times", 18, QtGui.QFont.Bold))
                    gridLayout2.addWidget(checkbox, i, 0, 1, 1)
                else:
                    checkbox = QtWidgets.QCheckBox("C类", tab)
                    checkbox.setObjectName("C")
                    checkbox.setFont(QtGui.QFont("Roman times", 18, QtGui.QFont.Bold))
                    gridLayout2.addWidget(checkbox, i, 0, 1, 1)
            else:
                checkbox = QtWidgets.QCheckBox(ccf_table.cell_value(i-1, 3*start_pos+1), tab)
                checkbox.setObjectName("checkBox" + str(i-1))
                checkbox.setStyleSheet("font: 10pt")
                self.checkbox_list.append(checkbox)
                self.checkbox_link_list.append(ccf_table.cell_value(i-1, 3*start_pos+2))
                gridLayout2.addWidget(checkbox, i, 0, 1, 1)
        # print(self.checkbox_list)

    def translate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CCF Crawler"))
        self.pushButton.setText(_translate("MainWindow", "Crawl"))
        # self.checkBox_3.setText(_translate("MainWindow", "name of conference or transaction1"))
        # self.checkBox_8.setText(_translate("MainWindow", "name of conference or transaction2"))
        # self.checkBox_9.setText(QtCore.QCoreApplication.translate("MainWindow", "name of conference or transaction3"))
        # self.checkBox_2.setText(_translate("MainWindow", "name of conference or transaction4"))
        # self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "name of category1"))
        # self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        # self.toolBox.setItemText(self.toolBox.indexOf(self.page2), _translate("MainWindow", "name of category2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuUpdate.setTitle(_translate("MainWindow", "Update"))
        self.menuFilter.setTitle(_translate("MainWindow", "Filter"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionFilter.setText(_translate("MainWindow", "Filter"))


'''to change the font of all same kind of widgets in the app GLOBAL'''
# StyleSheet = '''
# QCheckBox {
#     spacing: 3px;
#     font-size:20px;     /* <--- */
# }
#
# QCheckBox::indicator {
#     width:  33px;
#     height: 33px;
# }
# '''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    '''to change the font of all same kind of widgets in the app GLOBAL'''
    # app.setStyleSheet(StyleSheet)

    # noinspection PyArgumentList
    MainWindow = QtWidgets.QMainWindow()
    window = UIMainWindow(MainWindow)
    window.__init__(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
