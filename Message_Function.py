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
                            text='喜歡這家店:兄弟麵線'
                        ),
                        MessageTemplateAction(
                            label='菜單(約50元)',
                            text='想知道價目表:兄弟麵線',
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
                            text='喜歡這家店:鴉片粉圓'

                        ),
                        MessageTemplateAction(
                            label='菜單(約50元)',
                            text='想知道價目表:鴉片粉圓'
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
                            text='喜歡這家店:劉記蔥蛋餅'
                        ),
                        MessageTemplateAction(
                            label='菜單(約30元)',
                            text='想知道價目表:劉記蔥蛋餅',
                        ),
                        # URITemplateAction(
                        #     label='大約價錢：30元',
                        #     uri='https://i.imgur.com/1eWyjG2.png'
                        # ),
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
# ======================================店家介紹===========================================


def Price_M():
    message = TextSendMessage(text='蚵仔麵線(小碗) NT$50/碗\n蚵仔麵線(大碗) NT$60/碗')
    return message


def Price_Y():
    message = TextSendMessage(text='鴉片粉圓(冰/熱) NT$50/個\n綜合紅豆(冰/熱) NT$50/個\n三圓冰(冰/熱) NT$50/個\n檸檬愛玉(冰/熱) NT$50/個\n'
                              + '檸檬愛玉粉圓(冰) NT$50/個\n香Q芋圓(冰/熱) NT$50/個\n鮮奶粉圓(正常/去冰) (NT$60/65)/個\n檸檬汁(冰) NT$50/個')
    return message


def Price_D():
    message = TextSendMessage(text='蔥餅加蛋 NT$30/個\n蜜地瓜糖 NT$35/個')
    return message


def GetIntroductionM():
    message0 = TextSendMessage(text='「兄弟麵線介紹」\n堅持傳統口味的用心維持了近三十年，以前店面在東南亞劇院那邊的唱片行租房子賣麵線，'
                               + '某一次房東提議店名要不要一起用“兄弟”這個名字，之後就決定叫做「“兄弟”蚵仔麵線」直到現在')
    # message1 = TextSendMessage(text='「故事」')
    return message0


def GetIntroductionY():
    message0 = TextSendMessage(text='「鴉片粉圓介紹」「鴉片」一吃就上癮')
    message1 = TextSendMessage(text='「故事」')
    return message0, message1


def GetIntroductionD():
    message0 = TextSendMessage(text='「劉記蔥蛋餅」雖然外型酷似蔥油餅，但其實是蔥蛋餅，不一樣！')
    # message1 = TextSendMessage(text='「故事」')
    return message0

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

# =====================================相機開啟=======================================


def Camera_message():
    message = TextSendMessage(
        text='想要馬上嘗試嗎?',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=CameraAction(
                        label="立刻啟動Line相機",
                        text="text"))
            ]
        )
    )
    # message = TemplateSendMessage(
    #     alt_text='馬上拍出好照片吧!',
    #     template=ConfirmTemplate(
    #         text='等不及嘗試了嗎?',
    #         actions=[
    #                 CameraAction(
    #                     label='立刻嘗試'
    #                 ),
    #             MessageTemplateAction(
    #                 label='再等一下了@@',
    #                 text='再等一下了'
    #             )
    #         ]
    #     )
    # )
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
                        label='寶藏巖(今)',
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
# ====================================寶藏巖介紹=========================================


def HistoryBIntro():
    message = TextSendMessage(text='「寶藏巖介紹」')
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
# ====================================自來水廠介紹=========================================


def HistoryWIntro():
    message = TextSendMessage(text='「自來水廠介紹」')
    return message
# =====================================發送愛心========================================


def Send_Heart():
    message = TextMessage(
        text='$',
        emojis=[
            {
                "index": 0,
                "productId": "5ac1bfd5040ab15980c9b435",
                "emojiId": "215"
            }
        ]
    )
    return message

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
    message0 = TextSendMessage(text='從左到右分別代表:')
    message1 = TextSendMessage(
        text='「美食好好知」\n 推薦你水源里的美食時，一邊讓你了解美食背後鮮為人知的小秘密。')
    message2 = TextSendMessage(
        text='「拍照打卡熱點」\n 不知道怎麼拍出打卡美照嗎?\n 沒關係!我教你如何在水源里的熱門景點拍出網美照')
    message3 = TextSendMessage(
        text='「歷史循跡」\n 想知道水源里以前的樣子嗎?\n 我們蒐集了水源里各處的新舊照片，快來比較看看吧!')
    return message0, message1, message2, message3
