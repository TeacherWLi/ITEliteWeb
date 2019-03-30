"""


__author__ = Li Wei (liw@sicnu.edu.cn)
"""

# -------- Regular Expression --------

import re       # 正则表达式regular expression模块
from urllib import request


def re_demo():
    # 常量表达式
    demo_str = '1C2C++3Java4Python5Swift6OC7Javascript8C#9PHP!@#$%^PythoPythonPythonnnncatcetcot'
    pattern = 'Python'
    # print(re.findall(pattern, demo_str))

    # 元数据
    pattern = '\\d'
    # print(re.findall(pattern, demo_str))

    # 范围
    pattern = '[J-P]'
    # print(re.findall(pattern, demo_str))

    # 字符集特性
    pattern = 'c[ae]t'
    # print(re.findall(pattern, demo_str))

    # 数量词
    pattern = '[a-zA-Z]{3,5}'
    # print(re.findall(pattern, demo_str))

    # 通配符
    pattern = 'Python*'
    # print(re.findall(pattern, demo_str))

    # ? 当该字符紧跟在任何一个其他限制符（*,+,?，{n}，{n,}，{n,m}）后面时，匹配模式是非贪婪的。
    # 非贪婪模式尽可能少地匹配所搜索的字符串，而默认的贪婪模式则尽可能多地匹配所搜索的字符串。
    # 例如，对于字符串“oooo”，“o+”将尽可能多地匹配“o”，得到结果[“oooo”]，
    # 而“o+?”将尽可能少地匹配“o”，得到结果 ['o', 'o', 'o', 'o']
    pattern = '[a-zA-Z]{3,6}'  # 贪婪匹配
    # print(re.findall(pattern, demo_str))
    pattern = '[a-zA-Z]{3,6}?'  # 非贪婪匹配
    # print(re.findall(pattern, demo_str))

    # 边界匹配
    # ^ 匹配输入字行首
    # $ 匹配输入行尾
    # 例子，检查QQ号，QQ号是5-9位数字
    qq_str = '10000001'
    pattern = '^\\d{5,9}$'
    # print(re.findall(pattern, qq_str))

    # 组
    # (pattern) 匹配pattern并获取这一匹配。
    # 匹配是否包括GO!GO!GO!
    html_s = '<p>p1</p><p>p2</p><p>p3</p><div>p4</div>'
    pattern = '<p>(\\S+?)</p>'
    # print(re.findall(pattern, html_s))

    # 字符串替换
    pattern = 'Python'
    print(re.sub(pattern, 'Go', demo_str, 2))



# -------- Spider --------

url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.5ddadrilvua'


def fetch_html_content():
    response = request.urlopen(url)
    html_str = response.read()
    html_str = str(html_str, encoding='utf-8')
    return html_str


def analyse_video_info_ele(html_str):
    pattern = '<div class="video-info">([\\S\\s]*?)</div>'
    return re.findall(pattern, html_str)


def analyse_nickname_ele(video_info_str):
    pattern = '<span class="video-nickname"([\\S\\s]*?)</span>'
    rst = re.findall(pattern, video_info_str)[0]
    pattern = '</i>([\\S\\s]*)'
    return re.findall(pattern, rst)[0].strip()


def analyse_number_ele(video_info_str):
    pattern = '<span class="video-number"([\\S\\s]*?)</span>'
    rst = re.findall(pattern, video_info_str)[0]
    pattern = '</i>([\\S\\s]*)'
    return re.findall(pattern, rst)[0].strip()




def start_spider():         # 爬虫执行演示函数
    # Step1: 获取HTML数据
    html_str = fetch_html_content()

    # Step2: 解析出所有的video_info div元素
    all_video_info_ele = analyse_video_info_ele(html_str)

    for video_info_ele_str in all_video_info_ele:
        name = analyse_nickname_ele(video_info_ele_str)
        number = analyse_number_ele(video_info_ele_str)
        print(name + ': ' + number)


if __name__ == '__main__':
    # re_demo()
    start_spider()


