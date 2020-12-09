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


# 成為粉絲提示
@handler.add(FollowEvent)
def handle_Follow(event):
    # AccountName = '文化in水源'
    newcoming_message = Introduction_message()
    line_bot_api.reply_message(
        event.reply_token, newcoming_message)
    # message0 = TextSendMessage(
    #     text='你好啊(*≧∇≦*)！\n感謝你成為'+AccountName+'的好友！\n'+AccountName+'除了會介紹你公館的美食跟相關的的故事，還有很多水源里的老照片哦~' +
    #     '\n如果需要功能導覽的話，請輸入「導覽」，'+AccountName+'可以幫你介紹我的各個功能哦~')
    # line_bot_api.reply_message(
    #     event.reply_token, [message0, newcoming_message])
    print("FlowEvent =", FollowEvent)


# 離開粉絲提示
# @handler.add(UnfollowEvent)
# def handle_Follow(event):
#     message = TextSendMessage(text='祝福您，如果還有需要，歡迎再找我『文化in水源』唷~')
#     line_bot_api.reply_message(
#         event.reply_token, message)
#     print("FlowEvent =", UnfollowEvent)


# 加入群組提示
@handler.add(JoinEvent)
def handle_join(event):
    message0 = TextSendMessage(
        text='謝謝你讓我成為你們的一員 \n 需要幫助的話，可以選擇「導覽」，讓我向你介紹一次我的各個功能哦~')
    newcoming_message = Introduction_message()

    line_bot_api.reply_message(
        event.reply_token, [message0, newcoming_message])
    print("JoinEvent =", JoinEvent)


# 離開群組提示
@handler.add(LeaveEvent)
def handle_leave(event):
    print("leave Event =", event)
    print("很高興為你們服務唷!", event.source)

# ============================RichMenu===============================
    # rich_menu_to_create = RichMenu(
    #     size=RichMenuSize(width=2500, height=843),
    #     selected=True,
    #     name="main richmenu",
    #     chat_bar_text="Tap here",
    #     areas=[
    #         RichMenuArea(
    #             bounds=RichMenuBounds(
    #                 x=0,
    #                 y=0,
    #                 width=2500,
    #                 height=843
    #             ),
    #             action=URIAction(
    #                 label='Go to line.me',
    #                 uri='https://line.me'
    #             )
    #         )
    #     ]
    # )
    # rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
    # print(rich_menu_id)


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
    if '我想吃美食' in msg:
        levelF = '1'
        levelP = '0'
        levelH = '0'
        message = FoodLo_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '我想拍照' in msg:
        levelF = '0'
        levelP = '1'
        levelH = '0'
        message0 = TextSendMessage(text='點擊圖示選擇地點唷~')
        message = photoLo_message()
        line_bot_api.reply_message(event.reply_token, [message0, message])
    elif '想知道歷史' in msg:
        levelF = '0'
        levelP = '0'
        levelH = '1'
        message = HistoryLo_message()
        line_bot_api.reply_message(event.reply_token, message)
# =============================導覽==================================
    elif msg == '導覽':
        [message0, message1, message2, message3, message4] = MenuIntroduction()
        line_bot_api.reply_message(
            event.reply_token, [message0, message1, message2, message3, message4])
    elif msg == '我自己摸索就好~':
        message = TextSendMessage(text='好唷! 如果還有需要直接打『導覽』也可以唷!')
        line_bot_api.reply_message(event.reply_token, message)
# =============================美食==================================
    elif (levelF == '1' or levelF == '2K' or levelF == '2W'):
        if msg == '我想找美食:公館':
            levelF = '2K'
            message = FoodK_message()
            line_bot_api.reply_message(event.reply_token, message)
        elif msg == '我想找美食:水源市場':
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
            elif msg == '我想了解更多:兄弟麵線':
                message0 = GetIntroductionM()
                line_bot_api.reply_message(event.reply_token, message0,)
            elif msg == '我想了解更多:鴉片粉圓':
                [message0, message1] = GetIntroductionY()
                line_bot_api.reply_message(
                    event.reply_token, [message0, message1])
            elif msg == '我想了解更多:劉記蔥蛋餅':
                message0 = GetIntroductionD()
                line_bot_api.reply_message(event.reply_token, message0)
# =============================拍照==================================
    elif (levelP == '1' or levelP == '2B' or levelP == '2W' or levelP == '2K'):
        if msg == '拍照地點:寶藏巖':
            levelP = '2B'
            message = photo_message()
            line_bot_api.reply_message(event.reply_token, message)
        elif msg == '拍照地點:自來水博物館':
            levelP = '2W'
            message = photo_message()
            line_bot_api.reply_message(event.reply_token, message)
        elif msg == '拍照地點:公館商圈':
            levelP = '2K'
            message = photo_message()
            line_bot_api.reply_message(event.reply_token, message)
        elif levelP == '2B':
            if '站' in msg:
                message0 = photoStB_message()
                message1 = Camera_message()
                line_bot_api.reply_message(
                    event.reply_token, [message0, message1])
            elif '坐' in msg:
                message0 = photoSiB_message()
                message1 = Camera_message()
                line_bot_api.reply_message(
                    event.reply_token, [message0, message1])
            elif '躺' in msg:
                message0 = photolaB_message()
                message1 = Camera_message()
                line_bot_api.reply_message(
                    event.reply_token, [message0, message1])
        elif levelP == '2W':
            if '站' in msg:
                message0 = photoStW_message()
                message1 = Camera_message()
                line_bot_api.reply_message(
                    event.reply_token, [message0, message1])
            elif '坐' in msg:
                message0 = photoSiW_message()
                message1 = Camera_message()
                line_bot_api.reply_message(
                    event.reply_token, [message0, message1])
            elif '躺' in msg:
                message0 = photolaW_message()
                message1 = Camera_message()
                line_bot_api.reply_message(
                    event.reply_token, [message0, message1])
        elif levelP == '2K':
            if '站' in msg:
                message0 = photoStK_message()
                message1 = Camera_message()
                line_bot_api.reply_message(
                    event.reply_token, [message0, message1])
            # elif '坐' in msg:
            #     message0 = photoSiK_message()
            #     message1 = Camera_message()
            #     line_bot_api.reply_message(
            #         event.reply_token, [message0, message1])
            # elif '躺' in msg:
            #     message0 = photolaK_message()
            #     message1 = Camera_message()
            #     line_bot_api.reply_message(
            #         event.reply_token, [message0, message1])
# =============================歷史==================================
    elif levelH == '1':
        if msg == '瞭解歷史:寶藏巖':
            message0 = HistoryB_message()
            [message1, message2, message3] = HistoryBIntro()
            line_bot_api.reply_message(
                event.reply_token, [message0, message1, message2, message3])
        elif msg == '瞭解歷史:自來水博物館':
            message0 = HistoryW_message()
            [message1, message2] = HistoryWIntro()
            line_bot_api.reply_message(
                event.reply_token, [message0, message1, message2])
        elif '都不想' in msg:
            message = TextSendMessage(text='下次再來唷~')
            line_bot_api.reply_message(event.reply_token, message)

    else:
        message0 = TextSendMessage(
            text='不明白你在說什麼耶~ \n 需要幫助的話，可以輸入「導覽」，讓我再向你介紹一次我的各個功能哦~')
        message1 = Introduction_message()
        line_bot_api.reply_message(event.reply_token, [message0, message1])


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
