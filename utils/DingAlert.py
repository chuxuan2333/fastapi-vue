"""
钉钉机器人工具类
"""
import time
import hmac
import hashlib
import base64
import json
import urllib.parse
import requests
from core.config import settings

def create_secret(secret):
    """
    计算签名
    :return:
    """
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode("utf-8")
    string_to_sign = f"{timestamp}\n{secret}"
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return {"timestamp": timestamp, "sign": sign}


def send_message(ding_url, data):
    """
    发送钉钉消息
    :param ding_url: webhooks加密后地址
    :param data: 消息详情
    :return:
    """
    headers = {"Content-Type": "application/json"}
    requests.post(ding_url, headers=headers, data=json.dumps(data))


class DingAlert:
    def __init__(self, webhook, secret):
        self.webhook = webhook
        self.secret = secret

    def send_text(self, content, at_mobiles=None, at_all=False):
        """
        发送text类型消息
        :param content: 消息详情
        :param at_mobiles: 需要@的人手机号码,默认为空，传入因为list
        :param at_all: 是否@所有人
        :return:
        """
        # 生成调用url
        if at_mobiles is None:
            at_mobiles = []
        secret = create_secret(self.secret)
        ding_url = f"{self.webhook}&timestamp={secret.get('timestamp')}&sign={secret.get('sign')}"
        message = {"msgtype": "text", "text": {"content": content}, "at": {"atMobiles": at_mobiles, "isAtAll": at_all}}
        send_message(ding_url, message)

    def send_link(self, text, title, message_url, pic_url=""):
        """
        发送link类型消息
        :param text: 消息正文
        :param title: 消息标题
        :param message_url: link url
        :param pic_url: 图片url
        :return:
        """
        # 生成调用url
        secret = create_secret(self.secret)
        ding_url = f"{self.webhook}&timestamp={secret.get('timestamp')}&sign={secret.get('sign')}"
        message = {"msgtype": "link",
                   "link": {"text": text, "title": title, "picUrl": pic_url, "messageUrl": message_url}}
        send_message(ding_url, message)

    def send_markdown(self, title, text, at_mobiles=None, at_all=False):
        """
        发送markdown类型的消息
        :param title: 标题
        :param text: markdown格式详情
        :param at_mobiles: 需要@的人手机号码,默认为空，传入因为list
        :param at_all: 是否@所有人
        :return:
        """
        if at_mobiles is None:
            at_mobiles = []
        # 生成调用url
        secret = create_secret(self.secret)
        ding_url = f"{self.webhook}&timestamp={secret.get('timestamp')}&sign={secret.get('sign')}"
        message = {"msgtype": "markdown", "markdown": {"title": title, "text": text},
                   "at": {"atMobiles": at_mobiles, "isAtAll": at_all}}
        send_message(ding_url, message)

    def send_actioncard(self):
        # 生成调用url
        secret = create_secret(self.secret)
        ding_url = f"{self.webhook}&timestamp={secret.get('timestamp')}&sign={secret.get('sign')}"
        # TODO 发送actionCard类型消息

    def send_feedcard(self):
        # 生成调用url
        secret = create_secret(self.secret)
        ding_url = f"{self.webhook}&timestamp={secret.get('timestamp')}&sign={secret.get('sign')}"
        # TODO 发送feedCard类型消息
if __name__ == '__main__':
    ding_alert=DingAlert(webhook=settings.DINGDING_WEBHOOK,secret=settings.DINGDING_SECRET)
    ding_alert.send_markdown(title="新账户创建",text=settings.USER_CREATE_MSG.format("huangtao","123456"))