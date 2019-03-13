from ui import *
from PyQt5.QtCore import Qt
from dblp_crawler import *


def selected(checkbox, flag):
    # flag 0:A, 1:B, 2:C
    print("state changed")
    state = checkbox.checkState()
    print(state)
    print(checkbox.text())
    if state == Qt.Checked:
        index = window.toolBox.currentIndex()
        print('selected in page' + index)
        info = window.two_d_checkbox_list
        t_list = info[index][flag]
        c_list = info[index][flag+3]
        lists = [t_list, c_list]
        for item in lists:
            checkbox = item[0]
            # short_title = item[1]
            # full_title = item[2]
            # href = item[3]
            checkbox.setChecked()


def push_crawl_button():
    print('print button')
    journal_links = []
    conference_links = []
    link_list = window.checkbox_link_list
    type_list = window.checkbox_type_list
    checkbox_list = window.checkbox_list
    for i in range(len(checkbox_list)):
        if checkbox_list[i].checkState() == Qt.Checked:
            if type_list[i] == 0:
                journal_links.append(link_list[i])
            else:
                conference_links.append(link_list[i])
    # print("journal links: ")
    # print(journal_links)
    # print("conference links: ")
    # print(conference_links)

    journal_titles = []
    for journal_link in journal_links:
        volume_links = crawl_volume_links_from_journal(journal_url=journal_link, year=1)
        for volume_link in volume_links:
            journal_titles.append(crawl_titles(url=volume_link, keywords=['graph']))

    conference_titles = []
    for conference_link in conference_links:
        content_links = crawl_contents_links_from_conference(conference_url=conference_link, year=1)
        for content_link in content_links:
            conference_titles.append(crawl_titles(url=content_link, keywords=['graph']))

    print("journal titles: ")
    print(journal_titles)
    print("conference titles: ")
    print(conference_titles)


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

    for a_checkbox in window.checkbox_a_list:
        a_checkbox.stateChanged.connect(lambda: selected(a_checkbox, 0))
    # for b_checkbox in window.checkbox_b_list:
    #     b_checkbox.stateChanged.connect(selected(1))
    # for c_checkbox in window.checkbox_c_list:
    #     c_checkbox.stateChanged.connect(selected(2))

    sys.exit(app.exec_())

