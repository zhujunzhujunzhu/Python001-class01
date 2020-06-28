'''
安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，
并以 UTF-8 字符集保存到 csv 格式的文件中。
'''
import requests
# import bs4.BeautifulSoup as bs
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
cookie = "__mta=187088535.1593223852700.1593223869150.1593223947432.3; uuid_n_v=v1; uuid=6B610690B81B11EA8A833903D3167283DDCC43CEE9514DDC8A747A4ED22807FA; _csrf=94b2c76cddee6fdf0c327caa7bc79c341a54b1d84f28be940a1b2fccf0698059; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593223852; _lxsdk_cuid=172f38ab070ad-0949427938e6a4-376b4502-1fa400-172f38ab071c8; _lxsdk=6B610690B81B11EA8A833903D3167283DDCC43CEE9514DDC8A747A4ED22807FA; mojo-uuid=c7dfb7aa617737fee941ffb7fc2771fe; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593224116; __mta=187088535.1593223852700.1593223947432.1593224116302.4; _lxsdk_s=172f38ab071-19e-623-661%7C%7C46"
accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
referer = "https://maoyan.com/films?sourceId=10&showType=3"
header = {"user-agent": user_agent, "Cookie": cookie,
          "Accept": accept, "Referer": referer}

base_url = 'https://maoyan.com'
url = 'https://maoyan.com/films?showType=3'

LEN = 10

MAP = {
    "name": "名称",
    "type": "类型",
    "time": "上映时间",
    "short": "简介"
}


def get_movies():
    response = requests.get(url, headers=header)
    soup = bs(response.text, 'html.parser')
    infos = get_info(soup)
    save_movies(infos)


def get_info(soup):
    infos = []
    movie_infos = soup.find_all('div', {"class": "movie-hover-info"})
    movie_item_hovers = soup.find_all("div", {"class": "movie-item-hover"})
    for index, movie_info in enumerate(movie_infos[0:LEN]):
        try:
          # 当存在部分结构不一致时 可以继续向下
            moive_titles = movie_info.find_all(
                'div', {"class": "movie-hover-title"})
            info = {}
            info["name"] = deal_name(moive_titles[0].text)
            info["type"] = deal_others(moive_titles[1].text)
            info["time"] = deal_others(moive_titles[3].text)
            info["short"] = get_movie_short(movie_item_hovers[index])
            infos.append(info)
        except:
            print("get_info throw Error")

    return infos

# 名称处理


def deal_name(name):
    # 去掉评分
    return name.split()[0]

# 其它处理


def deal_others(str):
    return str.split()[1]


# 爬取电影简介
def get_movie_short(movie_item_hover):
    try:
        href = movie_item_hover.find('a').get('href')
        url = base_url + href
        #  请求详情页
        return go_detail(url)
    except:
        print("get_movie_short throw Error")

# 进入详情页面


def go_detail(url):
    response = requests.get(url, headers=header)
    soup = bs(response.text, 'html.parser')
    text = soup.find('div', {"class": 'tab-content-container'}
                     ).find('div', {"class": "mod-content"}).text
    short = "".join(text.split())
    return short
# 保存到maoyan.csv文件中


def save_movies(infos):
    movies_list = []
    for info in infos:
        new_info = {}
        for key, value in info.items():
            # 将字典属性替换成中文保存
            new_info[MAP[key]] = value
        movies_list.append(new_info)
    maoyan_list = pd.DataFrame(movies_list)
    maoyan_list.to_csv('csv/maoyan1.csv')


get_movies()
