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


levelF = '0'
levelP = '0'
levelH = '0'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    global levelF
    global levelP
    global levelH
# =============================美食==================================
    if '美食' in msg:
        levelF = '1'
        message = FoodLo_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif (levelF == '1' or levelF == '2') and '公館' in msg:
        levelF = '2'
        message = FoodK_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif (levelF == '1' or levelF == '2') and '市場' in msg:
        levelF = '2'
        message = FoodW_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif levelF == '1' and '都不想' in msg:
        levelF = '0'
        message = TextSendMessage(text='下次再來唷~')
        line_bot_api.reply_message(event.reply_token, message)
    elif levelF == '2' and '兄弟麵線' in msg:
        message = TextSendMessage(text='下次再來唷~')
        line_bot_api.reply_message(event.reply_token, message)
    elif levelF == '2' and '鴉片粉圓圓' in msg:
        message = TextSendMessage(text='下次再來唷~')
        line_bot_api.reply_message(event.reply_token, message)
    elif levelF == '2' and '劉記蔥蛋餅' in msg:
        message = TextSendMessage(text='下次再來唷~')
        line_bot_api.reply_message(event.reply_token, message)
# =============================拍照==================================
    elif '拍照' in msg:
        levelP = '1'
        message0 = TextSendMessage(text='點擊圖示選擇地點唷~')
        message = photoLo_message()
        line_bot_api.reply_message(event.reply_token, [message0, message])
    elif levelP == '1' and '寶藏巖' in msg:
        levelP = '2B'
        message = photo_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif levelP == '1' and '自來水廠' in msg:
        levelP = '2w'
        message = photo_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif levelP == '2B' and '站' in msg:
        message = photoStB_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif levelP == '2B' and '坐' in msg:
        message = photoSiB_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif levelP == '2B' and '躺' in msg:
        message = photolaB_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif levelP == '2W' and '站' in msg:
        message = photoStW_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif levelP == '2W' and '坐' in msg:
        message = photoSiW_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif levelP == '2W' and '躺' in msg:
        message = photolaW_message()
        line_bot_api.reply_message(event.reply_token, message)
# =============================歷史==================================
    elif '歷史' in msg:
        levelH = '1'
        message = HistoryLo_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif levelH == '1' and '寶藏巖' in msg:
        message = HistoryB_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif levelH == '1' and '自來水廠' in msg:
        message = HistoryW_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif levelH == '1' and '都不想' in msg:
        message = TextSendMessage(text='下次再來唷~')
        line_bot_api.reply_message(event.reply_token, message)
# =============================導覽==================================
    elif '導覽' in msg:
        message = TextSendMessage(text='從左到右分別代表:')
        message1 = TextSendMessage(
            text='「美食好好知」\n 推薦你水源里的美食時，一邊讓你了解美食背後鮮為人知的小秘密。')
        message2 = TextSendMessage(
            text='「拍照打卡熱點」\n 不知道怎麼拍出打卡美照嗎?\n 沒關係!我教你如何在水源里的熱門景點拍出網美照')
        message3 = TextSendMessage(
            text='「歷史循跡」\n 想知道水源里以前的樣子嗎?\n 我們蒐集了水源里各處的新舊照片，快來比較看看吧!')
        line_bot_api.reply_message(
            event.reply_token, [message, message1, message2, message3])
    else:
        message0 = TextSendMessage(
            text='不明白你在說什麼耶~ \n 需要幫助的話，可以輸入「導覽」，讓我再向你介紹一次我的各個功能哦~')
        message = Introduction_message()
        line_bot_api.reply_message(event.reply_token, [message0, message])


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
