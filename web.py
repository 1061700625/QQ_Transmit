# coding:utf-8

from flask import Flask, request
from flask import make_response
import json
import re
import requests

app = Flask(__name__)

BOSS = 0
SEND = 0

URL = r'http://127.0.0.1:5700/send_private_msg?'
def sendMsg(user_id, message):
    for i in user_id:
        url = URL + 'user_id=%s&message=%s' % (i, message)
        statcode = requests.get(url).status_code
        if statcode == 200:
            print('>> 发给[%s]完成' % i)
    print('')

def Process(contents):
    receiveQQ = contents['sender']['user_id']
    receiveMSG = contents['message']
    try:
        receiveGROUP = contents['group_id']
    except:
        receiveGROUP = ''
    if 'CQ:image' in receiveMSG:  # 图片
        receiveMSG = re.findall("url=(.*)\]", receiveMSG)[0]
        # receiveCQ = re.findall("\[CQ:(.*)\]", receiveMSG)[0]
        # print("CQ：", receiveCQ)

    print("GROUP：", receiveGROUP)
    print("QQ：", receiveQQ)
    print("消息：", receiveMSG)
    sendMsg(SEND, receiveMSG)


@app.route('/', methods=['POST'])
def receive():
    global BOSS, SEND
    contents = json.loads(request.get_data().decode('utf-8'))
    print("原始：", contents)
    receiveQQ = contents['sender']['user_id']

    if receiveQQ == BOSS:
        Process(contents)

    return make_response(''), 200





if __name__ == '__main__':
    BOSS = input('输入要接收的QQ： ').strip() or '1061700625'
    BOSS = int(BOSS)
    SEND = input('输入要发送的QQ,英文逗号分隔： ').strip() or '1061700625'
    SEND = SEND.split(',')
    for i in range(len(SEND)):
        SEND[i] = int(SEND[i])

    print('*' * 50)
    print('>> 接收：', BOSS)
    print('>> 发送：', SEND)
    print('*' * 50)
    print()

    app.run()  # debug=True

