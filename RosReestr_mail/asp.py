# http://sro-sso.ru/reestr_sro/view?id=52


import requests
from bs4 import BeautifulSoup
import csv
from multiprocessing import Pool, freeze_support
from time import sleep
from datetime import datetime

global_lst = []


class Count:
    c = 0


count = Count()


def writer_csv_include(dic):
    mail = 'Электронная почта'
    if mail not in dic:
        dic[mail] = ""
    else:
        print(dic[mail])

    try:
        with open("asp.csv", "a", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            if dic[mail] != "" or dic[mail] != 'нет':
                t = (dic[mail],

                     )

                writer.writerow(t)
    except Exception as e:
        print(e)


#
#
# def writer_csv_exclude(dic):
#     try:
#         with open("exclude_nostroy.csv", "a", newline='') as f:
#             writer = csv.writer(f, delimiter=';')
#             if len(dic) == 7:
#                 writer.writerow(tuple(dic))
#
#             else:
#                 print("csv len false")
#     except Exception as e:
#         print(str(e))


def get_html_(url):
    # sleep(0.5)
    k = 0
    page = ""
    while page == '':
        try:
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
            page = requests.get(url, headers=headers)
            return page.text
            break
        except:
            k += 1
            print("Connection refused by the doctor server..")
            print("Let me sleep for 10 seconds")
            # print("ZZzzzz...")
            sleep(10)
            # print("Was a nice sleep, now let me continue...")
            continue

def get_info_main(html):
    dictionary = []
    dic = []

    try:
        soup = BeautifulSoup(html, "lxml")
        #print(soup)
        soup = soup.find("table",class_="member_list").findAll("a")

        #print(soup)
        for i in soup:
            # dictionary.append(i.find("td").text.strip())
            # dic[i.find("th").text.strip()] = i.find("td").text.strip()
            dic.append("http://www.a-s-p.org"+i.get("href"))
        #print(dic)
        return dic
    except Exception as e:

        print(str(e))
        return dic



def get_info(html):
    dictionary = []
    dic = {}

    try:
        soup = BeautifulSoup(html, "lxml")
        #
        soup = soup.find("div",class_="memberDetail").findAll("p")

        for i in soup:
            temp=i.text.split(":")
            if len(temp)==2:
            # dictionary.append(i.find("td").text.strip())
                dic[temp[0]] = temp[1].strip()
        #print(dic)
        return dic
    except Exception as e:

        print(str(e))
        return dic


if __name__ == "__main__":
    links=[]
    for i in range(1, 5):

        links.extend(get_info_main(get_html_("http://www.a-s-p.org/register/?PAGEN_1={}".format(str(i)))))

    for link in links:
        writer_csv_include(get_info(get_html_(link)))

    # url="http://www.a-s-p.org/register/Domocentr/"
    # get_info(get_html_(url))

