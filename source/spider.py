import requests
from bs4 import BeautifulSoup
import chardet
import sys
import traceback
class Spider:
    def __init__(self):
        self.url = 'https://github.com/microsoft/vscode/issues?page='
        self.header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
            "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        self.resList = []

    def getHTMLText(self, page):
        try:
            r = requests.get(self.url+page, headers=self.header, timeout=30)
            print(r.status_code)
            r.raise_for_status()
            print(r.apparent_encoding)
            r.encoding = r.apparent_encoding
            return r.text
        except:
            traceback.print_exc()
            sys.exit("the url refused requests")

    def dealHTMLText(self, text):
        soup = BeautifulSoup(text, 'lxml')
        for tr in soup.find_all('div', class_='flex-auto min-width-0 p-2 pr-3 pr-md-2'):
            content = str(tr.find('a', class_='link-gray-dark v-align-middle no-underline h4 js-navigation-open').string)
            print(content)
            self.resList.append(content)

    def output(self):
        with open('output.txt', 'w') as f:
            for i in range(len(self.resList)):
                try:
                    f.write(str(i+1) + ': ')
                    #print(f'chardet.detect(): {chardet.detect(self.resList[i].encode("Windows-1252"))}')
                    f.write(self.resList[i])
                    f.write('\n\n')
                except:
                    continue

if __name__ == "__main__":
    spider = Spider()
    for i in range(4):
        text = spider.getHTMLText(str(i+1))
        spider.dealHTMLText(text)
    spider.output()