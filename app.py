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


# 加入提示
@handler.add(JoinEvent)
def handle_join(event):
    message0 = TextSendMessage(
        text='不明白你在說什麼耶~ \n 需要幫助的話，可以輸入「導覽」，讓我再向你介紹一次我的各個功能哦~')
    newcoming_message = Introduction_message()

    line_bot_api.reply_message(
        event.reply_token, newcoming_message)
    # line_bot_api.reply_message(
    #     event.reply_token, [message0, newcoming_message])
    print("JoinEvent =", JoinEvent)


@handler.add(LeaveEvent)
def handle_leave(event):
    print("leave Event =", event)
    print("我被踢掉了QQ 相關資訊", event.source)


# 處理訊息
levelF = '0'
levelP = '0'
levelH = '0'
# Location='0'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    global levelF
    global levelP
    global levelH
    # global Location
# ============================選單列表=================================
    if '美食' in msg:
        levelF = '1'
        levelP = '0'
        levelH = '0'
        message = FoodLo_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '拍照' in msg:
        levelF = '0'
        levelP = '1'
        levelH = '0'
        message0 = TextSendMessage(text='點擊圖示選擇地點唷~')
        message = photoLo_message()
        line_bot_api.reply_message(event.reply_token, [message0, message])
    elif '歷史' in msg:
        levelF = '0'
        levelP = '0'
        levelH = '1'
        message = HistoryLo_message()
        line_bot_api.reply_message(event.reply_token, message)
# =============================美食==================================
    elif (levelF == '1' or levelF == '2K' or levelF == '2W'):
        if '公館' in msg:
            levelF = '2K'
            message = FoodK_message()
            line_bot_api.reply_message(event.reply_token, message)
        elif '市場' in msg:
            levelF = '2M'
            message = FoodW_message()
            line_bot_api.reply_message(event.reply_token, message)
        elif '都不想' in msg:
            message = TextSendMessage(text='想要再點選再來唷~')
            line_bot_api.reply_message(event.reply_token, message)
        elif levelF == '2K':
            # =============================愛心==================================
            if msg == '喜歡這家店:兄弟麵線':
                message = Send_Heart()
                line_bot_api.reply_message(event.reply_token, message)
            elif msg == '喜歡這家店:鴉片粉圓':
                message = Send_Heart()
                line_bot_api.reply_message(event.reply_token, message)
            elif msg == '喜歡這家店:劉記蔥蛋餅':
                message = Send_Heart()
                line_bot_api.reply_message(event.reply_token, message)
            elif msg == '想知道價目表:兄弟麵線':
                message = Price_M()
                line_bot_api.reply_message(event.reply_token, message)
            elif msg == '想知道價目表:鴉片粉圓':
                message = Price_Y()
                line_bot_api.reply_message(event.reply_token, message)
            elif msg == '想知道價目表:劉記蔥蛋餅':
                message = Price_D()
                line_bot_api.reply_message(event.reply_token, message)
            elif '我想了解更多:兄弟麵線' in msg:
                message0 = GetIntroductionM()
                line_bot_api.reply_message(event.reply_token, message0,)
            elif '我想了解更多:鴉片粉圓' in msg:
                [message0, message1] = GetIntroductionY()
                line_bot_api.reply_message(
                    event.reply_token, [message0, message1])
            elif '我想了解更多:劉記蔥蛋餅' in msg:
                message0 = GetIntroductionD()
                line_bot_api.reply_message(event.reply_token, message0)
# =============================拍照==================================
    elif (levelP == '1' or levelP == '2B' or levelP == '2W'):
        if '寶藏巖' in msg:
            levelP = '2B'
            message = photo_message()
            line_bot_api.reply_message(event.reply_token, message)
        elif '自來水廠' in msg:
            levelP = '2W'
            message = photo_message()
            line_bot_api.reply_message(event.reply_token, message)
        elif levelP == '2B':
            if '站' in msg:
                message = photoStB_message()
                line_bot_api.reply_message(event.reply_token, message)
            elif '坐' in msg:
                message = photoSiB_message()
                line_bot_api.reply_message(event.reply_token, message)
            elif '躺' in msg:
                message = photolaB_message()
                line_bot_api.reply_message(event.reply_token, message)
        elif levelP == '2W':
            if '站' in msg:
                message = photoStW_message()
                line_bot_api.reply_message(event.reply_token, message)
            elif '坐' in msg:
                message = photoSiW_message()
                line_bot_api.reply_message(event.reply_token, message)
            elif '躺' in msg:
                message = photolaW_message()
                line_bot_api.reply_message(event.reply_token, message)
# =============================歷史==================================
    elif levelH == '1':
        if '寶藏巖' in msg:
            message0 = HistoryB_message()
            message1 = HistoryBIntro()
            line_bot_api.reply_message(event.reply_token, [message0, message1])
        elif '自來水廠' in msg:
            message0 = HistoryW_message()
            message1 = HistoryWIntro()
            line_bot_api.reply_message(event.reply_token, [message0, message1])
        elif '都不想' in msg:
            levelF = '0'
            levelP = '0'
            levelH = '0'
            message = TextSendMessage(text='下次再來唷~')
            line_bot_api.reply_message(event.reply_token, message)
# =============================導覽==================================
    elif msg == '導覽':
        [message0, message1, message2, message3, ] = MenuIntroduction()
        line_bot_api.reply_message(
            event.reply_token, [message0, message1, message2, message3])
    elif msg == '我自己摸索就好~':
        message = TextSendMessage(text='好唷!，如果還有需要直接打導覽也可以唷!')
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message0 = TextSendMessage(
            text='不明白你在說什麼耶~ \n 需要幫助的話，可以輸入「導覽」，讓我再向你介紹一次我的各個功能哦~')
        message1 = Introduction_message()
        line_bot_api.reply_message(event.reply_token, [message0, message1])


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
