from ui import *
from PyQt5.QtCore import Qt
from dblp_crawler import *


# def change():
#     print('test')
#     if window.checkbox_list[0].checkState() == Qt.Checked:
#         print("checked")
#     else:
#         print("unchecked")


def push_crawl_button():
    # how to distinguish conference and journal, need a label
    print('print button')
    links = []
    link_list = window.checkbox_link_list
    checkbox_list = window.checkbox_list
    for i in range(len(checkbox_list)):
        if checkbox_list[i].checkState() == Qt.Checked:
            links.append(link_list[i])
    print(links)


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

    # connections
    window.pushButton.clicked.connect(push_crawl_button)

    sys.exit(app.exec_())

