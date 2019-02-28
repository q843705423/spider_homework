import ssl
import re
import urllib.request
import time
from bs4 import BeautifulSoup


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(url, context=context)

        if response.getcode() != 200:
            return None
        else:
            return response.read()

    def getdata(self, soup):
        messcontent = soup.find("div", id="resultList")
        messtr = str(messcontent)
        # pattern = re.compile('<div class="el">.*?="t1">(\w+)</span>.*?="t2">(\w+)</span>.*?="t3">(\w+)</span>'
        #                      '.*?="t4">(\w+)</span>.*?="t5">(\w+)</span>.*?</div>', re.S)
        pattern = re.compile('<span class="t4">(.*?)</span>', re.S)
        res = re.findall(pattern, messtr)
        resstratmoney = []
        resendmoney = []
        for i, item in enumerate(res):
            if len(item) == 0:
                continue
            if i != 0:
                # print(i, item, "--->", type(item),"--->", len(item),"---->" , item[-1:])
                time = item[-1:]
                # 0.5-1
                money = item[:-3]
                list = money.split("-")

                try:
                    # 0.5
                    start_money = list[0]
                    # 1
                    end_money = list[1]
                except:
                    continue

                moneystr = item[-3]
                if time == "年":
                    if moneystr == "万":
                        start_money = int((float(start_money)*10000)/12.0)
                        end_money = int((float(end_money)*10000)/12.0)
                    elif moneystr == "千":
                        start_money = int((float(start_money) * 1000) / 12.0)
                        end_money = int((float(end_money) * 1000) / 12.0)
                    resstratmoney.append(start_money)
                    resendmoney.append(end_money)

                else:
                    if moneystr == "万":
                        start_money = int((float(start_money)*10000))
                        end_money = int((float(end_money)*10000))
                    elif moneystr == "千":
                        start_money = int((float(start_money) * 1000))
                        end_money = int((float(end_money) * 1000))

                    resstratmoney.append(start_money)
                    resendmoney.append(end_money)

        for i in range(len(resstratmoney)):
            file.write(str(resstratmoney[i])+"-"+str(resendmoney[i])+"\n")



num = 1
hp = HtmlDownloader()
# urlcplusplus = "https://search.51job.com/list/000000,000000,0000,00,9,99,C%252B%252B%25E5%25BC%2580%25E5%258F%2591,2," \
#          "1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=" \
#          "0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=21&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
# urljava = "https://search.51job.com/list/000000,000000,0000,00,9,99,java%25E5%25BC%2580%25E5%258F%2591,2,1.html?" \
#           "lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&" \
#           "lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
while num <= 100:
    file = open("D:/java.txt", "a+")

    urljava = "https://search.51job.com/list/000000,000000,0000,00,9,99,java%25E5%25BC%2580%25E5%258F%2591,2,"+str(num)+".html?" \
          "lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&" \
          "lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    html_cont = hp.download(urljava)
    soup = BeautifulSoup(html_cont, "html.parser", from_encoding="gbk")
    hp.getdata(soup)
    time.sleep(5)
    print("第"+str(num)+"爬完了")
    num += 1
    file.close()