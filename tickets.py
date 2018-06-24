
#docstring--docopt

'''命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 武汉 北京 2018-6-21
    tickets -dg 武汉 北京 2018-6-21
'''

import requests
from pprint import pprint
from station import station
from docopt import docopt
from prettytable import PrettyTable
from colorama import init,Fore

init()

class TrainsCollection:
    header = "车次 车站 时间 历时 商务座 一等 二等 高级软卧 软卧 动卧 硬卧 软座 硬座 无座".split()

    def __init__(self, available_trains, options):
        self.available_trains = available_trains
        self.options = options

    def _get_duration(self,duration):
        duration = duration.replace(":","小时")+"分"
        if duration.startswith("00"):
            return duration[4:]
        if duration.startswith("0"):
            return duration[3:]
        return duration

    def trains(self):
        res = []
        for available in self.available_trains:
            res.append([
                available["train_no"],Fore.GREEN+available["from_station"]+Fore.RESET+ "\n" + Fore.RED+available["to_station"]+Fore.RESET,
                Fore.GREEN+available["start_time"] +Fore.RESET+ "\n" +Fore.RED+available["end_time"]+Fore.RESET,  self._get_duration(available["duration"]), available["business_seat"],
                available["first_seat"],available["second_seat"],available["gjrw"],available["rw"],available["dw"],
                available["yw"], available["rz"],available["yz"],available["wz"]

            ])
        return res
    11
    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)#加表头
        for train in self.trains():
            pt.add_row(train)
        print(pt)


def cli():
    arguement = docopt(__doc__)
    fstation = station.get(arguement['<from>'])
    tstation = station.get(arguement['<to>'])
    date = arguement['<date>']
    options = ''.join(
        [key for key, value in arguement.items() if value is True]
    )
    get_station_url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT".format(
        date, fstation, tstation)
    r = requests.get(get_station_url)
    try:
        json_res = r.json()['data']
        result = json_res['result']
        trains = []
        for res in result:
            # 分割数据
            r_list = res.split("|")
            # 过滤数据
            r_dict = {
                'train_code': r_list[3],
                'train_no': r_list[2],
                'start_time': r_list[8],
                'end_time': r_list[9],
                'duration': r_list[10],
                'from_station': json_res['map'].get(r_list[6]),
                'to_station': json_res['map'].get(r_list[7]),
                'date': r_list[13],
                'business_seat': r_list[-5],
                'first_seat': r_list[-6],
                'second_seat': r_list[-7],
                'gjrw': r_list[-8],
                'rw': r_list[-9],
                'dw': r_list[-10],
                'yw': r_list[-11],
                'rz': r_list[-12],
                'yz': r_list[-13],
                'wz': r_list[-14],
                'qt': r_list[-15],
                'remark': r_list[1],
                'seat_type': r_list[-2],
                "from_station_no": r_list[16],
                "destinction_no": r_list[17],
            }
            for key,value in r_dict.items():
                if value == "":
                    r_dict[key] = "--"

            trains.append(r_dict)

        t = TrainsCollection(trains,options)
        t.pretty_print()

    except BaseException:

        print('Bye')



if __name__ == '__main__':
    cli()




#
# date = "2018-06-23"
#
# fstation = "北京"
# tstation = "上海"
#
#
# url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date" \
#       "={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT".format(date, station.get(fstation, ''), station[tstation])
# r = requests.get(url)
#
# pprint(r.text)