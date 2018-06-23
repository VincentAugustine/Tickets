#re--正则表达式
import re
#requests--访问HTTP
import requests
#pprint--智能打印python所有内置数据结构
from pprint import pprint
'''重定向输入输出：>   <
输出： python .\station_name.py > station.py'''

url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9056"

r = requests.get(url, verify = False)

stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',r.text)



pprint(dict(stations),indent=4)
#print(r.text)