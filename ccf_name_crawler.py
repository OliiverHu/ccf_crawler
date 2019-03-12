# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import urllib
import xlwt


def content_list(soup):
    urls = soup.find('ul', class_='g-ul m-snv')
    a = urls.find_all('li', id=True)
    url_new = []
    name_list = []
    for u in a:
        name_list.append(u.get_text())
        href = u.find("a")
        url_new.append(href['href'])
    return url_new, name_list


def bs4_crawler(url_link):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    req = urllib.request.Request(url_link, headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(req)
    content = response.read().decode('UTF-8')
    soup = BeautifulSoup(content, "lxml")
    return soup


def get_title_of_conference_and_transaction(soup):
    list = soup.find('div', class_='g-box1')
    # print(name)
    nickname_a_conf = []
    nickname_a_transac = []
    fullname_a_conf = []
    fullname_a_transac = []
    hrefname_a_conf = []
    hrefname_a_transac = []
    nickname_b_transac = []
    nickname_b_conf = []
    fullname_b_transac = []
    fullname_b_conf = []
    hrefname_b_transac = []
    hrefname_b_conf = []
    nickname_c_transac = []
    nickname_c_conf = []
    fullname_c_transac = []
    fullname_c_conf = []
    hrefname_c_transac = []
    hrefname_c_conf = []
    flag = 0
    abc_abc_list = list.find_all('ul', class_='g-ul x-list3')
    for a in abc_abc_list:
        li = a.find_all('li')
        for things in li:
            target = things.find_all('div')
            # print(target)
            if target[0].get_text() == '序号':
               flag += 1
            else:
                if flag == 1:
                    nickname_a_transac.append(target[1].get_text())
                    fullname_a_transac.append(target[2].get_text())
                    hrefname_a_transac.append(target[4].get_text())
                elif flag == 2:
                    nickname_b_transac.append(target[1].get_text())
                    fullname_b_transac.append(target[2].get_text())
                    hrefname_b_transac.append(target[4].get_text())
                elif flag == 3:
                    nickname_c_transac.append(target[1].get_text())
                    fullname_c_transac.append(target[2].get_text())
                    hrefname_c_transac.append(target[4].get_text())
                elif flag == 4:
                    nickname_a_conf.append(target[1].get_text())
                    fullname_a_conf.append(target[2].get_text())
                    hrefname_a_conf.append(target[4].get_text())
                elif flag == 5:
                    nickname_b_conf.append(target[1].get_text())
                    fullname_b_conf.append(target[2].get_text())
                    hrefname_b_conf.append(target[4].get_text())
                else:
                    nickname_c_conf.append(target[1].get_text())
                    fullname_c_conf.append(target[2].get_text())
                    hrefname_c_conf.append(target[4].get_text())

    return nickname_a_conf, nickname_a_transac, fullname_a_conf, fullname_a_transac, hrefname_a_conf, hrefname_a_transac, nickname_b_transac, nickname_b_conf, fullname_b_transac, fullname_b_conf, hrefname_b_transac, hrefname_b_conf, nickname_c_transac, nickname_c_conf, fullname_c_transac, fullname_c_conf, hrefname_c_transac, hrefname_c_conf


def update_info():
    ccf_homepage = "https://www.ccf.org.cn"
    ccf_url = "https://www.ccf.org.cn/xspj/gyml/"  # set all sorts of urls and links here

    soup = bs4_crawler(ccf_url)
    content_url, content_name = content_list(soup)
    xl_file = xlwt.Workbook()
    table = xl_file.add_sheet('表格1', cell_overwrite_ok=True)
    # could get all the url and name information of conference and transaction in ccf lists

    # print(content_url)
    # print(content_name)
    for i in range(1, len(content_url)-1):
        url_ = ccf_homepage + content_url[i]
        test_soup = bs4_crawler(url_)
        nickname_a_conf, nickname_a_transac, fullname_a_conf, fullname_a_transac, hrefname_a_conf, hrefname_a_transac, nickname_b_transac, nickname_b_conf, fullname_b_transac, fullname_b_conf, hrefname_b_transac, hrefname_b_conf, nickname_c_transac, nickname_c_conf, fullname_c_transac, fullname_c_conf, hrefname_c_transac, hrefname_c_conf = get_title_of_conference_and_transaction(soup=test_soup)
        # length = len(fullname_a_transac) + len(fullname_a_conf) + len(fullname_b_conf) +
        # len(fullname_b_transac) + len(fullname_c_conf) + len(fullname_c_transac)
        line_count = 0
        for j in range(8):
            if j == 0:
                table.write(line_count, 3 * i - 3, (content_name[i]))
                line_count += 1  # = 1
            if j == 1:
                table.write(line_count, 3 * i - 3, "A")
                line_count += 1  # = 2
                for k in range(len(fullname_a_transac)):
                    table.write(line_count, 3 * i - 3, nickname_a_transac[k])
                    table.write(line_count, 3 * i - 2, fullname_a_transac[k])
                    table.write(line_count, 3 * i - 1, hrefname_a_transac[k])
                    line_count += 1
            if j == 2:
                table.write(line_count, 3 * i - 3, "B")
                line_count += 1
                for k in range(len(fullname_b_transac)):
                    table.write(line_count, 3 * i - 3, nickname_b_transac[k])
                    table.write(line_count, 3 * i - 2, fullname_b_transac[k])
                    table.write(line_count, 3 * i - 1, hrefname_b_transac[k])
                    line_count += 1
            if j == 3:
                table.write(line_count, 3 * i - 3, "C")
                line_count += 1
                for k in range(len(fullname_c_transac)):
                    table.write(line_count, 3 * i - 3, nickname_c_transac[k])
                    table.write(line_count, 3 * i - 2, fullname_c_transac[k])
                    table.write(line_count, 3 * i - 1, hrefname_c_transac[k])
                    line_count += 1
            if j == 4:
                table.write(line_count, 3 * i - 3, (content_name[i]))
                line_count += 1
            if j == 5:
                table.write(line_count, 3 * i - 3, "A")
                line_count += 1  # = 2
                for k in range(len(fullname_a_conf)):
                    table.write(line_count, 3 * i - 3, nickname_a_conf[k])
                    table.write(line_count, 3 * i - 2, fullname_a_conf[k])
                    table.write(line_count, 3 * i - 1, hrefname_a_conf[k])
                    line_count += 1
            if j == 6:
                table.write(line_count, 3 * i - 3, "B")
                line_count += 1  # = 2
                for k in range(len(fullname_b_conf)):
                    table.write(line_count, 3 * i - 3, nickname_b_conf[k])
                    table.write(line_count, 3 * i - 2, fullname_b_conf[k])
                    table.write(line_count, 3 * i - 1, hrefname_b_conf[k])
                    line_count += 1
            if j == 7:
                table.write(line_count, 3 * i - 3, "C")
                line_count += 1  # = 2
                for k in range(len(fullname_c_conf)):
                    table.write(line_count, 3 * i - 3, nickname_c_conf[k])
                    table.write(line_count, 3 * i - 2, fullname_c_conf[k])
                    table.write(line_count, 3 * i - 1, hrefname_c_conf[k])
                    line_count += 1
    xl_file.save('ccf_names&links.xls')


if __name__ == '__main__':
    update_info()
