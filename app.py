import werobot
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

token = os.environ.get("WEROBOT_TOKEN", "")
port = os.environ.get("PORT", 0)
if token != "" and port != 0:
    logger.log('环境变量读取成功')
    logger.log("端口是{}".format(port))
    logger.log("token是{}".format(token))

else:
    logger.error('读取环境变量失败')

robot = werobot.WeRoBot(token=token)


@robot.text
def hello_world():
    return 'Hello World!'


robot.run(port=port,host="0.0.0.0")
