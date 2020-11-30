from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import tempfile
import os
import datetime
import time

# ======這裡是呼叫的檔案內容=====
from Message_Function import *

# ========ChatBot開始==========
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(
    'IVUnxQv7vzwOIC//Dc3/6HRzHvqsNoOEwN13B7mDzkFX1FKyM2+487NSJfk28NYFDDJ7KsgH2ph7GUfGEuYAk+i8yfJX050ip5nm9itmT14awJVJbF4wX5I/eIN0PXZR7kYUyDyHnRtAJ4QHazzjFwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('7d1a1ea57f47cf33c3ecf42237cad089')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '美食' in msg:
        message = Food_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '拍照' in msg:
        message = photo_message()
        line_bot_api.reply_message(event.reply_token, message)

        # message = TextSendMessage(text='想要什麼姿勢呢?站,坐,躺?')
        # line_bot_api.reply_message(event.reply_token, message)

        # @handler.add(MessageEvent, message=TextMessage)
        # def handle_message(event):
        #     msg = event.message.text
        #     if '站' in msg:
        #         message = photoSt_message()
        #         line_bot_api.reply_message(event.reply_token, message)
        #     elif '坐' in msg:
        #         message = photoSi_message()
        #         line_bot_api.reply_message(event.reply_token, message)
        #     elif '躺' in msg:
        #         message = photola_message()
        #         line_bot_api.reply_message(event.reply_token, message)

    elif '歷史' in msg:
        message = History_message()
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text='請點選單按鈕唷~')
        line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
