from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

# ======這裡是呼叫的py功能======

import os
import datetime
import time

# ======這裡是呼叫的檔案內容=====
from Message_Food import *
from Message_Photo import *
from Message_History import *


# ========ChatBot開始==========
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(
    "IVUnxQv7vzwOIC//Dc3/6HRzHvqsNoOEwN13B7mDzkFX1FKyM2+487NSJfk28NYFDDJ7KsgH2ph7GUfGEuYAk+i8yfJX050ip5nm9itmT14awJVJbF4wX5I/eIN0PXZR7kYUyDyHnRtAJ4QHazzjFwdB04t89/1O/w1cDnyilFU=")
# Channel Secret
handler = WebhookHandler("7d1a1ea57f47cf33c3ecf42237cad089")


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"

# 成為粉絲提示


@handler.add(FollowEvent)
def handle_Follow(event):
    # AccountName = "文化in水源"
    newcoming_message = Introduction_message()
    line_bot_api.reply_message(
        event.reply_token, newcoming_message)
    # message0 = TextSendMessage(
    #     text="你好啊(*≧∇≦*)！\n感謝你成為"+AccountName+"的好友！\n"+AccountName+"除了會介紹你公館的美食跟相關的的故事，還有很多水源里的老照片哦~" +
    #     "\n如果需要功能導覽的話，請輸入「導覽」，"+AccountName+"可以幫你介紹我的各個功能哦~")
    # line_bot_api.reply_message(
    #     event.reply_token, [message0, newcoming_message])
    print("FlowEvent =", FollowEvent)


# 離開粉絲提示
# @handler.add(UnfollowEvent)
# def handle_Follow(event):
#     message = TextSendMessage(text="祝福您，如果還有需要，歡迎再找我『文化in水源』唷~")
#     line_bot_api.reply_message(
#         event.reply_token, message)
#     print("FlowEvent =", UnfollowEvent)


# 加入群組提示
@handler.add(JoinEvent)
def handle_join(event):
    message1 = TextSendMessage(
        text="謝謝你讓我成為你們的一員 \n 需要幫助的話，可以選擇「導覽」，讓我向你介紹一次我的各個功能哦~")
    newcoming_message = Introduction_message()

    line_bot_api.reply_message(
        event.reply_token, [message1, newcoming_message])
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
    #                 label="Go to line.me",
    #                 uri="https://line.me"
    #             )
    #         )
    #     ]
    # )
    # rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
    # print(rich_menu_id)


# 處理訊息

@handler.add(MessageEvent, message=TextMessage)
def handle_Message(event):
    msg = event.message.text
# ============================選單列表=================================
    if "我想吃美食" in msg:
        message1 = FoodLo_message()
        line_bot_api.reply_message(event.reply_token, message1)
    elif "我想拍照" in msg:
        message1 = TextSendMessage(text="點擊圖示選擇地點唷~")
        message2 = photoLo_message()
        line_bot_api.reply_message(event.reply_token, [message1, message2])
    elif "想知道歷史" in msg:
        message1 = HistoryLo_message()
        line_bot_api.reply_message(event.reply_token, message1)
# =============================導覽==================================
    elif msg == "導覽":
        [message1, message2, message3, message4, message5] = MenuIntroduction()
        line_bot_api.reply_message(
            event.reply_token, [message1, message2, message3, message4, message5])
    elif "我自己摸索就好~" in msg:
        message1 = TextSendMessage(text="好唷! 如果還有需要直接打『導覽』也可以唷!")
        line_bot_api.reply_message(event.reply_token, message1)
# =============================美食==================================
    elif "我想找美食:公館" in msg:
        message1 = Food_message("K")
        line_bot_api.reply_message(event.reply_token, message1)
    elif "我想找美食:水源市場" in msg:
        message1 = TextSendMessage(text="這裡還沒有新增，可以選其他地方看看唷!")
        line_bot_api.reply_message(event.reply_token, message1)
        # message = Food_message("W")
        # line_bot_api.reply_message(event.reply_token, message)
    # =============================愛心==================================
    elif "喜歡這家店:兄弟麵線" in msg:
        message1 = Send_Heart("M")
        line_bot_api.reply_message(event.reply_token, message1)
    elif "喜歡這家店:鴉片粉圓" in msg:
        message1 = Send_Heart("Y")
        line_bot_api.reply_message(event.reply_token, message1)
    elif "喜歡這家店:劉記蔥蛋餅" in msg:
        message1 = Send_Heart("D")
        line_bot_api.reply_message(event.reply_token, message1)
    elif "想知道價目表:兄弟麵線" in msg:
        message1 = Price("M")
        line_bot_api.reply_message(event.reply_token, message1)
    elif "想知道價目表:鴉片粉圓" in msg:
        message1 = Price("Y")
        line_bot_api.reply_message(event.reply_token, message1)
    elif "想知道價目表:劉記蔥蛋餅" in msg:
        message1 = Price("D")
        line_bot_api.reply_message(event.reply_token, message1)
    elif "我想了解更多:兄弟麵線" in msg:
        message1 = GetInformation("M")
        line_bot_api.reply_message(event.reply_token, message1)
    elif "我想了解更多:鴉片粉圓" in msg:
        [message1, message2, message3] = GetInformation("Y")
        line_bot_api.reply_message(
            event.reply_token, [message1, message2, message3])
    elif "我想了解更多:劉記蔥蛋餅" in msg:
        message1 = GetInformation("D")
        line_bot_api.reply_message(event.reply_token, message1)
# =============================拍照==================================
    elif "地點選單:顯示" in msg:
        message1 = photo_menu()
        line_bot_api.reply_message(event.reply_token, message1)
    elif "拍照地點:寶藏巖" in msg:
        message1 = photo_message("B")
        line_bot_api.reply_message(event.reply_token, message1)
    elif "拍照地點:自來水博物館" in msg:
        message1 = photo_message("W")
        line_bot_api.reply_message(event.reply_token, message1)
    elif "拍照地點:公館商圈" in msg:
        message1 = photo_message("K")
        line_bot_api.reply_message(event.reply_token, message1)
# =============================歷史==================================
    elif "瞭解歷史:寶藏巖" in msg:
        [message1 message2] = History_message("B")
        message3 = MoreInfo_message("B")
        line_bot_api.reply_message(
            event.reply_token, [message1, message2, message3])
    elif "瞭解更多:寶藏巖" in msg:
        [message1, message2] = HistoryIntro("B")
        line_bot_api.reply_message(event.reply_token, [message1, message2])
    elif "瞭解歷史:自來水博物館" in msg:
        [message1, message2] = History_message("W")
        message3 = MoreInfo_message("W")
        # [message1, message2] = HistoryWIntro()
        line_bot_api.reply_message(
            event.reply_token, [message1, message2, message3])
    elif "瞭解更多:自來水博物館" in msg:
        [message1, message2] = HistoryIntro("W")
        line_bot_api.reply_message(event.reply_token, [message1, message2])
    elif "都不想" in msg:
        message1 = TextSendMessage(text="有需要再找我唷~")
        line_bot_api.reply_message(event.reply_token, message1)
# ====================================================================
    else:
        message1 = TextSendMessage(
            text="不明白你在說什麼耶~ \n 需要幫助的話，可以輸入「導覽」，讓我再向你介紹一次我的各個功能哦~")
        message2 = Introduction_message()
        line_bot_api.reply_message(event.reply_token, [message1, message2])


@handler.add(MessageEvent, message=LocationMessage)
def handle_Message(Location):
    Latitude = Location.message.latitude
    Longitude = Location.message.longitude
    [message1, message2] = photo_UserLocation(Latitude, Longitude)
    line_bot_api.reply_message(Location.reply_token, [message1, message2])
    # message1 = photo_UserLocation(Latitude, Longitude)
    # line_bot_api.reply_message(Location.reply_token, message1)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


# =====================================導覽確認========================================
def Introduction_message():
    message = TemplateSendMessage(
        alt_text='想要功能導覽嗎?',
        template=ConfirmTemplate(
            text='需要功能導覽嗎?',
            actions=[
                PostbackTemplateAction(
                    label='好呀~',
                    text='導覽',
                    data='action=Introduction'
                ),
                MessageTemplateAction(
                    label='我自己摸索沒關係',
                    text='我自己摸索就好~'
                )
            ]
        )
    )
    return message


# =====================================導覽========================================
def MenuIntroduction():
    message1 = TextSendMessage(text='點選下面選單，將出現功能選擇列表\n從左到右分別代表:')
    message2 = TextSendMessage(
        text='「美食好好知」\n 推薦你水源里的美食時，一邊讓你了解美食背後鮮為人知的小秘密。')
    message3 = TextSendMessage(
        text='「拍照打卡熱點」\n 不知道怎麼拍出打卡美照嗎?\n 沒關係!我教你如何在水源里的熱門景點拍出網美照')
    message4 = TextSendMessage(
        text='「歷史循跡」\n 想知道水源里以前的樣子嗎?\n 我們蒐集了水源里各處的新舊照片，快來比較看看吧!')
    message5 = VideoSendMessage(
        original_content_url='https://example.com/original.mp4',
        preview_image_url='https://i.imgur.com/mtn1Tmw.jpg'
    )
    return message1, message2, message3, message4, message5
