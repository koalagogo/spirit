# -*- coding: utf-8 -*-
# import tornado.web
from wechatpy import create_reply, parse_message
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException

from ._base import BaseHandler


class InterfaceHandler(BaseHandler):
    def get(self):
        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce = self.get_argument('nonce')
        echostr = self.get_argument('echostr')

        token = 'spirit'

        try:
            check_signature(token, signature, timestamp, nonce)
        except InvalidSignatureException:
            # 处理异常情况或忽略
            pass
        self.write(echostr)

    def post(self):
        data = self.request.body
        msg = parse_message(data)

        if msg.type == 'text':
            reply = create_reply(msg.content, msg)
        else:
            reply = create_reply('Sorry, can not handle this for now', msg)
        self.write(reply.render())
