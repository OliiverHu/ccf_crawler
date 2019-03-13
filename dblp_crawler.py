import requests
from bs4 import BeautifulSoup

def crawl_volume_links_from_journal(journal_url, year):
    # return link lists of journal in 'journal_url' in recent 'year' years
    soup = BeautifulSoup(requests.get(url=journal_url).text, 'html.parser')
    a_objects = soup.find_all('ul', class_=False)[6].find_all('a')
    links = []
    for a_object in a_objects[:year]:
        links.append(a_object.get('href'))
    return links


def crawl_titles(url, keywords):
    # return paper title list in 'url' which contains 'keywords'
    titles = []
    html_soup = BeautifulSoup(requests.get(url=url).text, 'html.parser')
    for title in html_soup.find_all('span', class_='title'):
        text = title.get_text()
        flag = False
        for word in keywords:
            if text.upper().find(word.upper()) is not -1:
                flag = True
        if flag:
            titles.append(text)
    return titles


def crawl_contents_links_from_conference(conference_url, year):
    # return link lists of journal in 'journal_url' in recent 'year' years
    soup = BeautifulSoup(requests.get(url=conference_url).text, 'html.parser')
    publ_lists = soup.find_all('ul', class_='publ-list')
    links = []
    for i in range(year):
        a_objects = (publ_lists[i].find_all('a', class_='toc-link'))
        for a_object in a_objects:
            links.append(a_object.get('href'))
    # print(links)
    return links


if __name__ == "__main__":
    # links = crawl_contents_links_from_conference('https://dblp.uni-trier.de/db/conf/sigmod/', 1)
    links = crawl_volume_links_from_journal('https://dblp.uni-trier.de/db/journals/tods/', year=5)
    print(links)
    for link in links:
        titles = crawl_titles(link, ['graph'])
        print(titles)
