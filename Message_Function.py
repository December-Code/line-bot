# ===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
# ===========================LINEAPI==============================


def FoodLo_message():
    message = TemplateSendMessage(
        alt_text='你想要找哪裡的美食呢?',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/cMyF8lN.png",
            title="找哪裡的美食呢?",
            text="選擇你的地點",
            actions=[
                MessageTemplateAction(
                    label="公館美食",
                    text='公館',
                ),
                MessageTemplateAction(
                    label="水源市場美食",
                    text='水源市場',
                ),
                MessageTemplateAction(
                    label="都沒有耶QQ",
                    text='都不想',
                ),
            ]
        )
    )
    return message

# ===================================公館美食推薦==========================================


def FoodK_message():
    message = TemplateSendMessage(
        alt_text='最近美食資訊',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/LupmODQ.jpg',
                    title='兄弟蚵仔麵線',
                    text='堅持傳統口味的用心維持了近三十年 \n 地點:100台北市中正區汀州路三段235號',
                    actions=[
                        PostbackTemplateAction(
                            label='我喜歡這家店',
                            data='使用者喜歡'
                        ),
                        URITemplateAction(
                            label='大約價錢：50 元',
                            uri='https://i.imgur.com/5jNgx1V.jpg'
                        ),
                        # message(
                        #     label='我想了解更多~',
                        #     text='我想了解更多:兄弟麵線'
                        # )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/HOyJCWN.jpg',
                    title='鴉片粉圓',
                    text='「鴉片」一吃就上癮 \n 地點:100台北市中正區羅斯福路四段52巷16弄4號',
                    actions=[
                        PostbackTemplateAction(
                            label='我喜歡這家店',
                            data='使用者喜歡'
                        ),
                        PostbackTemplateAction(
                            label='大約價錢：50 元',
                            data='使用者喜歡'
                        ),
                        message(
                            label='我想了解更多~',
                            text='我想了解更多:鴉片粉圓'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/HXNAAUG.jpg',
                    title='劉記古早味蔥蛋餅',
                    text='雖然外型酷似蔥油餅，但其實是蔥蛋餅，不一樣！\n 地點:100台北市中正區羅斯福路四段108巷2-3號',
                    actions=[
                        PostbackTemplateAction(
                            label='我喜歡這家店',
                            data='使用者喜歡'
                        ),
                        PostbackTemplateAction(
                            label='大約價錢：45 元',
                            data='使用者喜歡'
                        ),
                        message(
                            label='我想了解更多~',
                            text='我想了解更多:蔥蛋餅'
                        )
                    ]
                ),
            ]
        )
    )
    return message

# ===================================水源市場美食推薦=========================================
# def FoodW_message():
#     message = TemplateSendMessage(
#         alt_text='最近美食資訊',
#         template=CarouselTemplate(
#             columns=[
#                 CarouselColumn(
#                     thumbnail_image_url='https://i.imgur.com/LupmODQ.jpg',
#                     title='兄弟蚵仔麵線',
#                     text='堅持傳統口味的用心維持了近三十年',
#                     actions=[
#                         PostbackTemplateAction(
#                             label='我喜歡這家店',
#                             data='使用者喜歡'
#                         ),
#                         PostbackTemplateAction(
#                             label='大約價錢：50 元',
#                             data='使用者喜歡'
#                         ),
#                         URITemplateAction(
#                             # label='100台北市中正區汀州路三段235號',
#                             label='它在哪呢?',
#                             uri='https://goo.gl/maps/FodenKrdkMt7Kq4Z7'
#                         )
#                     ]
#                 ),
#                 CarouselColumn(
#                     thumbnail_image_url='https://i.imgur.com/HOyJCWN.jpg',
#                     title='鴉片粉圓',
#                     text='「鴉片」一吃就上癮',
#                     actions=[
#                         PostbackTemplateAction(
#                             label='我喜歡這家店',
#                             data='使用者喜歡'
#                         ),
#                         PostbackTemplateAction(
#                             label='大約價錢：50 元',
#                             data='使用者喜歡'
#                         ),
#                         URITemplateAction(
#                             # label='100台北市中正區羅斯福路四段52巷16弄4號',
#                             label='它在哪呢?',
#                             uri='https://goo.gl/maps/bUDeGy4QDjYFgCar9'
#                         )
#                     ]
#                 ),
#                 CarouselColumn(
#                     thumbnail_image_url='https://i.imgur.com/HXNAAUG.jpg',
#                     title='劉記古早味蔥蛋餅',
#                     text='雖然外型酷似蔥油餅，但其實是蔥蛋餅，不一樣！',
#                     actions=[
#                         PostbackTemplateAction(
#                             label='我喜歡這家店',
#                             data='使用者喜歡'
#                         ),
#                         PostbackTemplateAction(
#                             label='大約價錢：45 元',
#                             data='使用者喜歡'
#                         ),
#                         URITemplateAction(
#                             # label='100台北市中正區羅斯福路四段108巷2-3號',
#                             label='它在哪呢?',
#                             uri='https://goo.gl/maps/7H6dCPVUcVr3PuAv8'
#                         )
#                     ]
#                 ),
#             ]
#         )
#     )
#     return message

# =====================================站著的照片推薦============================================


def photo_message():
    message = TemplateSendMessage(
        alt_text='選擇你要的姿勢',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/raFTzTo.jpg",
            title="想要拍照了嗎?",
            text="選擇想要的姿勢",
            actions=[
                MessageTemplateAction(
                    label="我想站姿",
                    text='站',
                ),
                MessageTemplateAction(
                    label="我想坐姿",
                    text='坐',
                ),
                MessageTemplateAction(
                    label="我想躺姿",
                    text='躺',
                ),
            ]
        )
    )
    return message


# =====================================站著的照片推薦============================================
def photoSt_message():
    message = TemplateSendMessage(
        alt_text='站姿推薦',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/rpIHO7w.jpg",
                    action=URITemplateAction(
                        label="自來水_扭曲水管",
                        uri="https://i.imgur.com/rpIHO7w.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/lZSR4Bq.jpg",
                    action=URITemplateAction(
                        label="自來水_扭曲水管(站)",
                        uri="https://i.imgur.com/lZSR4Bq.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/xuS9nUe.jpg",
                    action=URITemplateAction(
                        label="寶藏巖_幸福餅乾",
                        uri="https://i.imgur.com/xuS9nUe.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/xuS9nUe.jpg",
                    action=URITemplateAction(
                        label="寶藏巖_幸福餅乾(站)",
                        uri="https://i.imgur.com/xuS9nUe.jpg"
                    )
                ),
            ]
        )
    )
    return message

# =====================================坐著的照片推薦============================================


def photoSi_message():
    message = TemplateSendMessage(
        alt_text='坐姿推薦',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/xuS9nUe.jpg",
                    action=URITemplateAction(
                        label="寶藏巖_幸福餅乾",
                        uri="https://i.imgur.com/xuS9nUe.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/xuS9nUe.jpg",
                    action=URITemplateAction(
                        label="寶藏巖_幸福餅乾(坐)",
                        uri="https://i.imgur.com/xuS9nUe.jpg"
                    )
                )
            ]
        )
    )
    return message

# =====================================躺著的照片推薦============================================


def photola_message():
    message = TemplateSendMessage(
        alt_text='躺姿推薦',
        template=ImageCarouselTemplate(
            columns=[
                 ImageCarouselColumn(
                     image_url="https://i.imgur.com/4PZvAlV.jpg",
                     action=URITemplateAction(
                         label="自來水廠_管中世界",
                         uri="https://i.imgur.com/4PZvAlV.jpg"
                     )
                 ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/RkrmZjH.jpg",
                    action=URITemplateAction(
                        label="自來水廠_管中世界(躺)",
                        uri="https://i.imgur.com/RkrmZjH.jpg"
                    )
                 ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/1DHNhgM.jpg",
                    action=URITemplateAction(
                        label="自來水_長椅下午后",
                        uri="https://i.imgur.com/1DHNhgM.jpg"
                    )
                 ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/MkPeQQY.jpg",
                    action=URITemplateAction(
                        label="自來水_長椅下午后(躺)",
                        uri="https://i.imgur.com/MkPeQQY.jpg"
                    )
                 )
            ]
        )
    )
    return message

# =====================================歷史對照==========================================


def HistoryLo_message():
    message = TemplateSendMessage(
        alt_text='你想要了解那裡的歷史呢?',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/8ze9PtV.png",
            title="想了解那裡的歷史呢?",
            text="選擇想要的地點",
            actions=[
                MessageTemplateAction(
                    label="我想瞭解寶藏巖",
                    text='寶藏巖',
                ),
                MessageTemplateAction(
                    label="我想瞭解自來水廠",
                    text='自來水廠',
                ),
                MessageTemplateAction(
                    label="都沒有耶QQ",
                    text='都不想',
                ),
            ]
        )
    )
    return message
# =====================================寶藏巖對照========================================


def HistoryB_message():
    message = TemplateSendMessage(
        alt_text='先看看寶藏巖的今昔對比',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/dlk5RhE.png",
                    action=URITemplateAction(
                        label="寶藏巖_(新))",
                        uri="https://i.imgur.com/dlk5RhE.png"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/5TMDvWW.png",
                    action=URITemplateAction(
                        label="寶藏巖(舊))",
                        uri="https://i.imgur.com/5TMDvWW.png"
                    )
                )
            ]
        )
    )
    return message
# =====================================自來水廠對照========================================


def HistoryW_message():
    message = TemplateSendMessage(
        alt_text='先看看自來水廠的今昔對比',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/3K6Kl1s.png",
                    action=URITemplateAction(
                        label="自來水廠(新)",
                        uri="https://i.imgur.com/3K6Kl1s.png"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/YA3NPS5.png",
                    action=URITemplateAction(
                        label="自來水廠(舊)",
                        uri="https://i.imgur.com/YA3NPS5.png"
                    )
                )
            ]
        )
    )
    return message

# def History_message():
#     message = ImagemapSendMessage(
#         base_url="https://i.imgur.com/OKgp8Fa.png",
#         alt_text='這裡有什麼歷史呢?',
#         base_size=BaseSize(height=2000, width=2000),
#         actions=[
#             URIImagemapAction(
#                 # 寶藏巖
#                 link_uri="https://tw.shop.com/search/%E5%AE%B6%E6%A8%82%E7%A6%8F",
#                 label='寶藏巖',
#                 area=ImagemapArea(
#                     x=0, y=0, width=1000, height=1000
#                 )
#             ),
#             URIImagemapAction(
#                 # 自來水廠
#                 link_uri="https://tw.shop.com/search/%E7%94%9F%E6%B4%BB%E5%B8%82%E9%9B%86",
#                 label='自來水廠',
#                 area=ImagemapArea(
#                     x=1000, y=0, width=1000, height=1000
#                 )
#             ),
#         ]
#     )
#     return message


# =====================================導覽確認========================================
def Introduction_message():
    message = TemplateSendMessage(
        alt_text='想要功能導覽嗎?',
        template=ConfirmTemplate(
            text='不明白你在說什麼耶~ \n 需要幫助的話，可以輸入「導覽」，讓我再向你介紹一次我的各個功能哦~',
            actions=[
                PostbackTemplateAction(
                    label='postback',
                    text='postback text',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='message',
                    text='message text'
                )
            ]
        )
    )
