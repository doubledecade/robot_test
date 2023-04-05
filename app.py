import werobot
import os

token = os.environ.get("WEROBOT_TOKEN", "")
port = os.environ.get("PORT", 0)
if token != "" and port != 0:
    print("环境变量读取成功")
robot = werobot.WeRoBot(token=token)


@robot.text
def hello_world():
    return 'Hello World!'


robot.run(port=port)
