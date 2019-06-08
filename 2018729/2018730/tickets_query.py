#_*_ coding:utf-8 _*_
'''命令行火车票查询器
Usage:
    trainTicket [-abcdefg] <from> <to> <date> <train>
    trainTicket [-abcdefg] <from> <to> <date> <train> --type

Options:
    -h --help   显示帮助菜单
    -a         硬座
    -b         硬卧
    -c         软卧
    -d         无座
    -e         商务/特等
    -f         一等座
    -g         二等座
    --type    票种

Example:
    trainTicket -ab 肇庆 湛江西 2017-08-28 Z111
'''
from docopt import docopt
from prettytable import PrettyTable
import requests
import json
import urllib
import logging
import os
import time
from send_email import send_email
#初探log
logging.basicConfig(filename='./log.txt',
                    level=logging.DEBUG,
                    filemode='w',
                    format='%(asctime)s-%(levelname)s:%(message)s',
                    )
logger = logging.getLogger(__name__)

def load(): #读取车站代码列表json
    with open('station_code.json','r') as f:
        data = json.load(f)
        return data

def get_ticket_mes(arg):
    print(arg)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    data = {
        'leftTicketDTO.train_date':arg['<date>'],
        'leftTicketDTO.from_station':arg['<from>'],
        'leftTicketDTO.to_station':arg['<to>'],
        'purpose_codes':not arg['--type'] and 'ADULT' or arg['--type'], #默认成人票，输入0X00为学生票
    }
    base_url = 'https://kyfw.12306.cn/otn/leftTicket/query'
    last_url = '?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=%s'\
               %(data['leftTicketDTO.train_date'],data['leftTicketDTO.from_station'],data['leftTicketDTO.to_station'],data['purpose_codes'])
    url = base_url+last_url
    try:
        res = requests.get(url,headers=header,verify=False)
        ticket_mes = list(map(lambda x:x.split('|'),res.json()['data']['result']))
    except:
        logger.exception('failed to get json!')

    for i in ticket_mes:
        if arg['<train>'] == i[3]:
            train_mes = i
    flag = False
    if (arg['-a'] == True) and (train_mes[29] and train_mes[29] != '无'):
        flag = True
    if (arg['-b'] == True) and (train_mes[28] and train_mes[28] != '无'):
        flag = True
    if (arg['-c'] == True) and (train_mes[23] and train_mes[23] != '无'):
        flag = True
    if (arg['-d'] == True) and (train_mes[26] and train_mes[26] != '无'):
        flag = True
    if (arg['-e'] == True) and (train_mes[32] and train_mes[32] != '无'):
        flag = True
    if (arg['-f'] == True) and (train_mes[31] and train_mes[31] != '无'):
        flag = True
    if (arg['-g'] == True) and (train_mes[30] and train_mes[30] != '无'):
        flag = True
    return flag,train_mes

def pretty_print(i):
    header = '车次 出发站\n到达站 出发时间\n到达时间 历时 商务座\n特等座 一等座 二等座 软卧 硬卧 硬座 无座'.split(' ')
    pt = PrettyTable()
    pt.add_row(header)
    pt.add_row([i[3], i[6] + '\n' + i[7], i[8] + '\n' + i[9], i[10], i[32], i[31], i[30], i[23], i[28], i[29], i[26]])

    return pt

if __name__ == '__main__':
    while 1:
        argument = docopt(__doc__)
        logger.info('Start waiting ticket.....%s-%s %s %s', *(argument['<from>'], argument['<to>'], argument['<date>'],argument['<train>']))
        try:
            station_list = load()
        except:
            logger.exception('failed to load station code!')
        _to = station_list[argument['<to>']]
        _from = station_list[argument['<from>']]
        argument['<to>'] = _to
        argument['<from>'] = _from
        flag,ticket_mes= get_ticket_mes(argument)
        if flag:
            pt = pretty_print(ticket_mes)
            logger.info('Finish waiting ticket.....')
            logger.info('Start to send email....')
            data = {
                '<from_addr>':'wwwinter34@163.com',
                '<password>':'winter34',
                '<to_addr>':'121402687@qq.com',
                '<smtp_server>':'smtp.163.com',
                '<Subject>':'有票啦！！',
                '<text>':'有票啦',
            }
            sender = send_email(data)
            sender.send()
            break
        time.sleep(300)
