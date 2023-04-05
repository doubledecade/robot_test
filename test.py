import logging
import os

from flask import Flask, request, make_response
import hashlib
import xml.etree.ElementTree as ET

app = Flask(__name__)

token1 = os.environ.get("WEROBOT_TOKEN", "")
port = os.environ.get("PORT", 0)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


@app.route('/', methods=['GET', 'POST'])
def wechat_auth():
    if request.method == 'GET':
        token = token1  # 替换为自己在公众号设置中的Token
        data = request.args
        signature = data.get('signature', '')
        timestamp = data.get('timestamp', '')
        nonce = data.get('nonce', '')
        echostr = data.get('echostr', '')
        list = [token, timestamp, nonce]
        list.sort()
        logging.info(list)
        s = ''.join(list).encode('utf-8')
        if hashlib.sha1(s).hexdigest() == signature:
            return make_response(echostr)
        else:
            return 'Invalid Signature'
    else:
        xml_data = request.stream.read()
        xml_tree = ET.fromstring(xml_data)
        msg_type = xml_tree.find('MsgType').text
        if msg_type == 'text':
            content = xml_tree.find('Content').text
            response_content = chat_with_gpt(content)
            response = generate_text_response(xml_tree, response_content)
            return make_response(response)
        else:
            response_content = '暂不支持该类型消息的回复。'
            response = generate_text_response(xml_tree, response_content)
            return make_response(response)


def chat_with_gpt(text):
    # 调用ChatGPT的API接口，返回对话结果
    return "chat with gpt"


def generate_text_response(xml_tree, content):
    # 根据对话结果生成XML格式的回复消息
    return "ssds"


app.run(host="0.0.0.0", port=port)
