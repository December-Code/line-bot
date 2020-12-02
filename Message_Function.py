# ===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
# ===========================LINEAPI==============================


# ===================================美食推薦地點=======================================
def FoodLo_message():
    message = TemplateSendMessage(
        alt_text='你想要找哪裡的美食呢?',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/cMyF8lN.png',
            title='找哪裡的美食呢?',
            text='選擇你的地點',
            actions=[
                MessageTemplateAction(
                    label='公館美食',
                    text='公館',
                ),
                MessageTemplateAction(
                    label='水源市場美食',
                    text='水源市場',
                ),
                MessageTemplateAction(
                    label='都沒有耶QQ',
                    text='都不想',
                ),
            ]
        )
    )
    return message

# ===================================公館美食推薦=======================================


def FoodK_message():
    message = TemplateSendMessage(
        alt_text='最近美食資訊',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/LupmODQ.jpg',
                    title='兄弟蚵仔麵線',
                    text='堅持傳統口味的用心維持了近三十年\n地點:100台北市中正區汀州路三段235號',
                    actions=[
                        PostbackTemplateAction(
                            label='我喜歡這家店',
                            data='使用者喜歡:兄弟麵線',
                            # text='喜歡這家店:兄弟麵線'
                            text='喜歡這家店'
                        ),
                        URITemplateAction(
                            label='大約價錢：50元',
                            uri='https://i.imgur.com/5jNgx1V.jpg'
                        ),
                        MessageTemplateAction(
                            label='我想了解更多~',
                            text='我想了解更多:兄弟麵線',
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/HOyJCWN.jpg',
                    title='鴉片粉圓',
                    text='「鴉片」一吃就上癮\n地點:100台北市中正區羅斯福路四段52巷16弄4號',
                    actions=[
                        PostbackTemplateAction(
                            label='喜歡這家店',
                            data='使用者喜歡:鴉片粉圓',
                            # text='喜歡這家店:兄弟麵線'
                            text='喜歡這家店'
                        ),
                        URITemplateAction(
                            label='大約價錢：50元',
                            uri='https://i.imgur.com/5jNgx1V.jpg'
                        ),
                        MessageTemplateAction(
                            label='我想了解更多~',
                            text='我想了解更多:鴉片粉圓'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/HXNAAUG.jpg',
                    title='劉記古早味蔥蛋餅',
                    text='雖然外型酷似蔥油餅，但其實是蔥蛋餅，不一樣！\n地點:100台北市中正區羅斯福路四段108巷2-3號',
                    actions=[
                        PostbackTemplateAction(
                            label='喜歡這家店',
                            data='使用者喜歡:劉記蔥蛋餅',
                            # text='喜歡這家店:劉記蔥蛋餅'
                            text='喜歡這家店'
                        ),
                        URITemplateAction(
                            label='大約價錢：45元',
                            uri='https://goo.gl/maps/FodenKrdkMt7Kq4Z7'
                        ),
                        MessageTemplateAction(
                            label='我想了解更多~',
                            text='我想了解更多:劉記蔥蛋餅'
                        )
                    ]
                ),
            ]
        )
    )
    return message

# ===================================水源市場美食推薦========================================
# def FoodK_message():
#     message = TemplateSendMessage(
#         alt_text='最近美食資訊',
#         template=CarouselTemplate(
#             columns=[
#                 CarouselColumn(
#                     thumbnail_image_url='https://i.imgur.com/LupmODQ.jpg',
#                     title='兄弟蚵仔麵線',
#                     text='堅持傳統口味的用心維持了近三十年\n地點:100台北市中正區汀州路三段235號',
#                     actions=[
#                         PostbackTemplateAction(
#                             label='我喜歡這家店',
#                             data='使用者喜歡'
#                         ),
#                         URITemplateAction(
#                             label='大約價錢：50元',
#                             uri='https://i.imgur.com/5jNgx1V.jpg'
#                         ),
#                         MessageTemplateAction(
#                             label='我想了解更多~',
#                             text='我想了解更多:兄弟麵線',
#                         )
#                     ]
#                 ),
#                 CarouselColumn(
#                     thumbnail_image_url='https://i.imgur.com/HOyJCWN.jpg',
#                     title='鴉片粉圓',
#                     text='「鴉片」一吃就上癮\n地點:100台北市中正區羅斯福路四段52巷16弄4號',
#                     actions=[
#                         PostbackTemplateAction(
#                             label='我喜歡這家店',
#                             data='使用者喜歡'
#                         ),
#                         URITemplateAction(
#                             label='大約價錢：50元',
#                             uri='https://i.imgur.com/5jNgx1V.jpg'
#                         ),
#                         MessageTemplateAction(
#                             label='我想了解更多~',
#                             text='我想了解更多:鴉片粉圓'
#                         )
#                     ]
#                 ),
#                 CarouselColumn(
#                     thumbnail_image_url='https://i.imgur.com/HXNAAUG.jpg',
#                     title='劉記古早味蔥蛋餅',
#                     text='雖然外型酷似蔥油餅，但其實是蔥蛋餅，不一樣！\n地點:100台北市中正區羅斯福路四段108巷2-3號',
#                     actions=[
#                         PostbackTemplateAction(
#                             label='我喜歡這家店',
#                             data='使用者喜歡'
#                         ),
#                         URITemplateAction(
#                             label='大約價錢：45元',
#                             uri='https://goo.gl/maps/FodenKrdkMt7Kq4Z7'
#                         ),
#                         MessageTemplateAction(
#                             label='我想了解更多~',
#                             text='我想了解更多:蔥蛋餅'
#                         )
#                     ]
#                 ),
#             ]
#         )
#     )
#     return message

# ====================================拍照推薦地點=============================================


def photoLo_message():
    message = ImagemapSendMessage(
        base_url='https://i.imgur.com/OKgp8Fa.png',
        alt_text='想要拍照了嗎 ?',
        base_size=BaseSize(height=1000, width=1000),
        actions=[
            MessageImagemapAction(
                text='自來水廠',
                area=ImagemapArea(
                    x=500, y=0, width=500, height=500
                )
            ),
            MessageImagemapAction(
                text='寶藏巖',
                area=ImagemapArea(
                    x=0, y=0, width=500, height=500
                )
            )
        ]
    )
    return message

# ===================================照片的姿勢推薦=========================================


def photo_message():
    message = TemplateSendMessage(
        alt_text='選擇你想要的姿勢',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/raFTzTo.jpg',
            title='想要拍照了嗎?',
            text='選擇想要的姿勢',
            actions=[
                MessageTemplateAction(
                    label='我想站姿',
                    text='站',
                ),
                MessageTemplateAction(
                    label='我想坐姿',
                    text='坐',
                ),
                MessageTemplateAction(
                    label='我想躺姿',
                    text='躺',
                ),
            ]
        )
    )
    return message
# =====================================寶藏巖站姿的照片推薦=======================================


def photoStB_message():
    message = TemplateSendMessage(
        alt_text='寶藏巖站姿推薦',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/rpIHO7w.jpg',
                    action=URITemplateAction(
                        label='扭曲水管',
                        uri='https://i.imgur.com/rpIHO7w.jpg'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/lZSR4Bq.jpg',
                    action=URITemplateAction(
                        label='扭曲水管(站)',
                        uri='https://i.imgur.com/lZSR4Bq.jpg'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/xuS9nUe.jpg',
                    action=URITemplateAction(
                        label='幸福餅乾',
                        uri='https://i.imgur.com/xuS9nUe.jpg'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/xuS9nUe.jpg',
                    action=URITemplateAction(
                        label='幸福餅乾(站)',
                        uri='https://i.imgur.com/xuS9nUe.jpg'
                    )
                ),
            ]
        )
    )
    return message

# ==================================寶藏巖坐著的照片推薦=========================================


def photoSiB_message():
    message = TemplateSendMessage(
        alt_text='寶藏巖坐姿推薦',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/xuS9nUe.jpg',
                    action=URITemplateAction(
                        label='幸福餅乾',
                        uri='https://i.imgur.com/xuS9nUe.jpg'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/xuS9nUe.jpg',
                    action=URITemplateAction(
                        label='幸福餅乾(坐)',
                        uri='https://i.imgur.com/xuS9nUe.jpg'
                    )
                )
            ]
        )
    )
    return message

# =====================================寶藏巖躺著的照片推薦==========================================


def photolaB_message():
    message = TemplateSendMessage(
        alt_text='寶藏巖躺姿推薦',
        template=ImageCarouselTemplate(
            columns=[
                 ImageCarouselColumn(
                     image_url='https://i.imgur.com/4PZvAlV.jpg',
                     action=URITemplateAction(
                         label='管中世界',
                         uri='https://i.imgur.com/4PZvAlV.jpg'
                     )
                 ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/RkrmZjH.jpg',
                    action=URITemplateAction(
                        label='管中世界(躺)',
                        uri='https://i.imgur.com/RkrmZjH.jpg'
                    )
                 ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/1DHNhgM.jpg',
                    action=URITemplateAction(
                        label='長椅下午后',
                        uri='https://i.imgur.com/1DHNhgM.jpg'
                    )
                 ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/MkPeQQY.jpg',
                    action=URITemplateAction(
                        label='長椅下午后(躺)',
                        uri='https://i.imgur.com/MkPeQQY.jpg'
                    )
                 )
            ]
        )
    )
    return message

# =====================================自來水廠站姿的照片推薦=======================================


def photoStW_message():
    message = TemplateSendMessage(
        alt_text='自來水站姿推薦',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/rpIHO7w.jpg',
                    action=URITemplateAction(
                        label='扭曲水管',
                        uri='https://i.imgur.com/rpIHO7w.jpg'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/lZSR4Bq.jpg',
                    action=URITemplateAction(
                        label='扭曲水管(站)',
                        uri='https://i.imgur.com/lZSR4Bq.jpg'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/xuS9nUe.jpg',
                    action=URITemplateAction(
                        label='幸福餅乾',
                        uri='https://i.imgur.com/xuS9nUe.jpg'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/xuS9nUe.jpg',
                    action=URITemplateAction(
                        label='幸福餅乾(站)',
                        uri='https://i.imgur.com/xuS9nUe.jpg'
                    )
                ),
            ]
        )
    )
    return message

# ==================================自來水廠坐著的照片推薦=========================================


def photoSiW_message():
    message = TemplateSendMessage(
        alt_text='自來水坐姿推薦',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/xuS9nUe.jpg',
                    action=URITemplateAction(
                        label='幸福餅乾',
                        uri='https://i.imgur.com/xuS9nUe.jpg'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/xuS9nUe.jpg',
                    action=URITemplateAction(
                        label='幸福餅乾(坐)',
                        uri='https://i.imgur.com/xuS9nUe.jpg'
                    )
                )
            ]
        )
    )
    return message

# =====================================自來水廠躺著的照片推薦==========================================


def photolaW_message():
    message = TemplateSendMessage(
        alt_text='自來水躺姿推薦',
        template=ImageCarouselTemplate(
            columns=[
                 ImageCarouselColumn(
                     image_url='https://i.imgur.com/4PZvAlV.jpg',
                     action=URITemplateAction(
                         label='管中世界',
                         uri='https://i.imgur.com/4PZvAlV.jpg'
                     )
                 ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/RkrmZjH.jpg',
                    action=URITemplateAction(
                        label='管中世界(躺)',
                        uri='https://i.imgur.com/RkrmZjH.jpg'
                    )
                 ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/1DHNhgM.jpg',
                    action=URITemplateAction(
                        label='長椅下午后',
                        uri='https://i.imgur.com/1DHNhgM.jpg'
                    )
                 ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/MkPeQQY.jpg',
                    action=URITemplateAction(
                        label='長椅下午后(躺)',
                        uri='https://i.imgur.com/MkPeQQY.jpg'
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
            thumbnail_image_url='https://i.imgur.com/8ze9PtV.png',
            title='想了解那裡的歷史呢?',
            text='選擇想要的地點',
            actions=[
                MessageTemplateAction(
                    label='我想瞭解寶藏巖',
                    text='寶藏巖',
                ),
                MessageTemplateAction(
                    label='我想瞭解自來水廠',
                    text='自來水廠',
                ),
                MessageTemplateAction(
                    label='都沒有耶QQ',
                    text='都不想',
                ),
            ]
        )
    )
    return message
# ====================================寶藏巖對照=========================================


def HistoryB_message():
    message = TemplateSendMessage(
        alt_text='先看看寶藏巖的今昔對比',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/dlk5RhE.png',
                    action=URITemplateAction(
                        label='寶藏巖_(今)',
                        uri='https://i.imgur.com/dlk5RhE.png'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/5TMDvWW.png',
                    action=URITemplateAction(
                        label='寶藏巖(昔)',
                        uri='https://i.imgur.com/5TMDvWW.png'
                    )
                )
            ]
        )
    )
    return message
# ====================================自來水廠對照========================================


def HistoryW_message():
    message = TemplateSendMessage(
        alt_text='先看看自來水廠的今昔對比',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/3K6Kl1s.png',
                    action=URITemplateAction(
                        label='自來水廠(今)',
                        uri='https://i.imgur.com/3K6Kl1s.png'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/YA3NPS5.png',
                    action=URITemplateAction(
                        label='自來水廠(昔)',
                        uri='https://i.imgur.com/YA3NPS5.png'
                    )
                )
            ]
        )
    )
    return message

# def History_message():
#     message = ImagemapSendMessage(
#         base_url='https://i.imgur.com/OKgp8Fa.png',
#         alt_text='這裡有什麼歷史呢?',
#         base_size=BaseSize(height=2000, width=2000),
#         actions=[
#             URIImagemapAction(
#                 # 寶藏巖
#                 link_uri='https://tw.shop.com/search/%E5%AE%B6%E6%A8%82%E7%A6%8F',
#                 label='寶藏巖',
#                 area=ImagemapArea(
#                     x=0, y=0, width=1000, height=1000
#                 )
#             ),
#             URIImagemapAction(
#                 # 自來水廠
#                 link_uri='https://tw.shop.com/search/%E7%94%9F%E6%B4%BB%E5%B8%82%E9%9B%86',
#                 label='自來水廠',
#                 area=ImagemapArea(
#                     x=1000, y=0, width=1000, height=1000
#                 )
#             ),
#         ]
#     )
#     return message
# =====================================發送愛心========================================


def Send_Heart():
    message = TextSendMessage(
        text='$',
        emojis=TextMessage(
            index='0',
            productId='5ac1bfd5040ab15980c9b435',
            emojiId='215')
    )
    return message
# def Send_Heart():
#     emoji_heart = (
#         index=0,
#         lenghth=10,
#         productId='5ac1bfd5040ab15980c9b435',
#         emojiId='215'
#     )
#     message = TextSendMessage(
#         text='$',
#         emojis=[emoji_heart]
#     )
#     return message
# def Send_Heart():
#     message = StickerSendMessage(
#         package_id='5ac1bfd5040ab15980c9b435',
#         sticker_id='215'
#     )
#     return message

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
                    text='好唷!，如果還有需要直接打導覽也可以唷!'
                )
            ]
        )
    )
    return message
