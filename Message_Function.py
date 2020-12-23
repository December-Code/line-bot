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
            thumbnail_image_url='https://i.imgur.com/NbgfxlT.png',
            title='找哪裡的美食呢?',
            text='選擇你的地點',
            actions=[
                MessageTemplateAction(
                    label='公館美食',
                    text='我想找美食:公館',
                ),
                MessageTemplateAction(
                    label='水源市場',
                    text='我想找美食:水源市場',
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
                    text='堅持傳統口味的用心維持了近三十年\n地址:100台北市中正區汀州路三段235號',
                    actions=[
                        PostbackTemplateAction(
                            label='喜歡這家店',
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
                    text='「鴉片」一吃就上癮\n地址:100台北市中正區羅斯福路四段52巷16弄4號',
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
                    text='雖然外型酷似蔥油餅，但其實是蔥蛋餅，不一樣！\n地址:100台北市中正區羅斯福路四段108巷2-3號',
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
    message = TextMessage(text='$蚵仔麵線(小碗) NT$50/份\n$蚵仔麵線(大碗) NT$60/份',
                          emojis=[
                              {
                                  "index": 0,
                                  "productId": "5ac1de17040ab15980c9b438",
                                  "emojiId": "035"
                              },
                              {
                                  "index": 18,
                                  "productId": "5ac1de17040ab15980c9b438",
                                  "emojiId": "035"
                              },
                          ]
                          )
    return message


def Price_Y():
    message = TextMessage(text='$鴉片粉圓(冰/熱) NT$50/份\n$綜合紅豆(冰/熱) NT$50/份\n' +
                          '$三圓冰(冰/熱) NT$50/份\n$檸檬愛玉(冰/熱) NT$50/份\n' +
                          '$檸檬愛玉粉圓(冰) NT$50/份\n$香Q芋圓(冰/熱) NT$50/份\n' +
                          '$鮮奶粉圓(正常/去冰) (NT$60/65)/份\n$檸檬汁(冰) NT$50/份',
                          emojis=[
                              {
                                  "index": 0,
                                  "productId": "5ac21a18040ab15980c9b43e",
                                  "emojiId": "029"
                              },
                              {
                                  "index": 19,
                                  "productId": "5ac1de17040ab15980c9b438",
                                  "emojiId": "035"
                              },
                              {
                                  "index": 38,
                                  "productId": "5ac1de17040ab15980c9b438",
                                  "emojiId": "035"
                              },
                              {
                                  "index": 56,
                                  "productId": "5ac21a18040ab15980c9b43e",
                                  "emojiId": "029"
                              },
                              {
                                  "index": 75,
                                  "productId": "5ac1de17040ab15980c9b438",
                                  "emojiId": "035"
                              },
                              {
                                  "index": 94,
                                  "productId": "5ac1de17040ab15980c9b438",
                                  "emojiId": "035"
                              },
                              {
                                  "index": 113,
                                  "productId": "5ac1de17040ab15980c9b438",
                                  "emojiId": "035"
                              },
                              {
                                  "index": 139,
                                  "productId": "5ac1de17040ab15980c9b438",
                                  "emojiId": "035"
                              },
                          ]
                          )

    return message


def Price_D():
    message = TextMessage(text='$蔥餅加蛋 NT$30/份\n$蜜地瓜糖 NT$35/份',
                          emojis=[
                              {
                                  "index": 0,
                                  "productId": "5ac1de17040ab15980c9b438",
                                  "emojiId": "035"
                              },
                              {
                                  "index": 14,
                                  "productId": "5ac1de17040ab15980c9b438",
                                  "emojiId": "035"
                              },
                          ])
    return message


def GetIntroductionM():
    message0 = TextSendMessage(text='「兄弟麵線介紹」\n堅持傳統口味的用心維持了近三十年，以前店面在東南亞劇院那邊的唱片行租房子賣麵線，'
                               + '某一次房東提議店名要不要一起用“兄弟”這個名字，之後就決定叫做「“兄弟”蚵仔麵線」直到現在')
    # message1 = TextSendMessage(text='「故事」')
    return message0


def GetIntroductionY():
    message0 = TextSendMessage(
        text='「鴉片粉圓介紹」\n位於「公館商圈」一間隱匿於小巷的「鴉片粉圓」是你夏日消暑聖品！' +
        '飽滿嫩Ｑ粉圓搭配甘甜的沁脾的黑糖冰，如同冰品名稱「鴉片」，讓你一口接一口停不下來')
    message1 = TextSendMessage(
        text='隔壁的「得記麻辣脆皮臭豆腐」也是十分有名！酷熱的白天來碗通體舒暢的粉圓冰，入夜後就是來一鍋暖胃的麻辣臭豆腐！' +
        '清蒸臭豆腐搭上麻辣鴨血還有肥腸，一鍋又辣又臭的麻辣五更熱呼呼的端上桌！')
    message2 = TextSendMessage(
        '無論是因為天氣熱想先來碗，讓人上癮的「鴉片粉圓」消暑；' +
        '或是深夜後飢腸轆轆，想來一鍋餘味無窮的「得記麻辣臭豆腐」在這裡都是一個不錯的選擇')
    return message0, message1, message2


def GetIntroductionD():
    message0 = TextSendMessage(text='「劉記蔥蛋餅」雖然外型酷似蔥油餅，但其實是蔥蛋餅，不一樣！')
    # message1 = TextSendMessage(text='「故事」')
    return message0

# ===================================水源市場美食推薦========================================


# def FoodW_message():
#     message = FlexSendMessage(
#         alt_text='hello',
#         contents=BubbleContainer(
#             direction='ltr',
#             hero=ImageComponent(
#                 url='https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png',
#                 size='full',
#                 aspect_ratio='20:13',
#                 aspect_mode='cover',
#                 action=URIAction(uri='http://example.com', label='label')
#             )
#         )
#     )
#     return message

# ====================================拍照推薦地點=============================================


def photoLo_message():
    # message = TextSendMessage(
    #     text='想要馬上嘗試嗎?',
    #     quick_reply=QuickReply(
    #         items=[
    #             QuickReplyButton(
    #                 action=LocationAction(
    #                     label="傳送我的地點",
    #                 ),
    #             ),
    #             QuickReplyButton(
    #                 action=CameraRollAction(
    #                     label="相機啟動",
    #                 ),
    #             )
    #         ]
    #     )
    # )
    message = ImagemapSendMessage(
        base_url='https://i.imgur.com/cFFeXLt.png',
        alt_text='想要拍照了嗎 ?',
        base_size=BaseSize(height=1000, width=1000),
        actions=[
            MessageImagemapAction(
                text='拍照地點:公館商圈',
                area=ImagemapArea(
                    x=0, y=0, width=500, height=500
                )
            ),
            MessageImagemapAction(
                text='拍照地點:自來水博物館',
                area=ImagemapArea(
                    x=500, y=0, width=500, height=500
                )
            ),
            MessageImagemapAction(
                text='拍照地點:寶藏巖',
                area=ImagemapArea(
                    x=0, y=500, width=1000, height=500
                )
            )
            # MessageImagemapAction(
            #     text='拍照地點:寶藏巖',
            #     area=ImagemapArea(
            #         x=235, y=500, width=500, height=500
            #     )
            # )

        ]
    )
    return message

# ===================================照片的姿勢推薦=========================================


def photo_message(L):
    if L == 'K':
        message = TemplateSendMessage(
            alt_text='選擇你想要的姿勢',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/FmZo2Eu.png',
                title='想要拍照了嗎?',
                text='選擇想要的姿勢',
                actions=[
                    MessageTemplateAction(
                        label='我想站姿',
                        text='公館:站',
                    ),
                    # MessageTemplateAction(
                    #     label='我想坐姿',
                    #     text='公館:坐',
                    # ),
                    # MessageTemplateAction(
                    #     label='我想躺姿',
                    #     text='公館:躺',
                    # ),
                ]
            )
        )
        return message
    elif L == 'B':
        message = TemplateSendMessage(
            alt_text='選擇你想要的姿勢',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/yWRa31N.png',
                title='想要拍照了嗎?',
                text='選擇想要的姿勢',
                actions=[
                    MessageTemplateAction(
                        label='我想站姿',
                        text='寶藏巖:站',
                    ),
                    MessageTemplateAction(
                        label='我想坐姿',
                        text='寶藏巖:坐',
                    ),
                    # MessageTemplateAction(
                    #     label='我想躺姿',
                    #     text='躺',
                    # ),
                ]
            )
        )
        return message
    elif L == 'W':
        message = TemplateSendMessage(
            alt_text='選擇你想要的姿勢',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/2VMl7Jq.png',
                title='想要拍照了嗎?',
                text='選擇想要的姿勢',
                actions=[
                    MessageTemplateAction(
                        label='我想站姿',
                        text='自來水博物館:站',
                    ),
                    # MessageTemplateAction(
                    #     label='我想坐姿',
                    #     text='自來水博物館:坐',
                    # ),
                    MessageTemplateAction(
                        label='我想躺姿',
                        text='自來水博物館:躺',
                    ),
                ]
            )
        )
        return message


# =====================================公館商圈站姿的照片推薦=======================================
def photoStK_message():
    message = TemplateSendMessage(
        alt_text='公館商圈站姿推薦',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/pqJbKt2.jpg',
                    action=URITemplateAction(
                        label='里長辦公室',
                        uri='https://i.imgur.com/pqJbKt2.jpg'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/vSLhuNN.jpg',
                    action=URITemplateAction(
                        label='里長辦公室(站姿)',
                        uri='https://i.imgur.com/vSLhuNN.jpg'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/GEmmxnl.jpg',
                    action=URITemplateAction(
                        label='得記麻辣',
                        uri='https://i.imgur.com/GEmmxnl.jpg'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/Do6PKWw.jpg',
                    action=URITemplateAction(
                        label='得記麻辣(站姿)',
                        uri='https://i.imgur.com/Do6PKWw.jpg'
                    )
                ),
            ]
        )
    )
    return message


# ==================================公館商圈坐姿的照片推薦=========================================
def photoSiK_message():
    message = TemplateSendMessage(
        alt_text='公館商圈坐姿推薦',
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


# ==================================公館商圈躺著的照片推薦==========================================
# def photolaK_message():
#     message = TemplateSendMessage(
#         alt_text='公館商圈躺姿推薦',
#         template=ImageCarouselTemplate(
#             columns=[
#                  ImageCarouselColumn(
#                      image_url='https://i.imgur.com/4PZvAlV.jpg',
#                      action=URITemplateAction(
#                          label='管中世界',
#                          uri='https://i.imgur.com/4PZvAlV.jpg'
#                      )
#                  ),
#                 ImageCarouselColumn(
#                     image_url='https://i.imgur.com/RkrmZjH.jpg',
#                     action=URITemplateAction(
#                         label='管中世界(躺)',
#                         uri='https://i.imgur.com/RkrmZjH.jpg'
#                     )
#                  ),
#                 ImageCarouselColumn(
#                     image_url='https://i.imgur.com/1DHNhgM.jpg',
#                     action=URITemplateAction(
#                         label='長椅下午后',
#                         uri='https://i.imgur.com/1DHNhgM.jpg'
#                     )
#                  ),
#                 ImageCarouselColumn(
#                     image_url='https://i.imgur.com/MkPeQQY.jpg',
#                     action=URITemplateAction(
#                         label='長椅下午后(躺)',
#                         uri='https://i.imgur.com/MkPeQQY.jpg'
#                     )
#                  )
#             ]
#         )
#     )
#     return message


# =====================================寶藏巖站姿的照片推薦=======================================
def photoStB_message():
    message = TemplateSendMessage(
        alt_text='寶藏巖站姿推薦',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/fq034OP.jpg',
                    action=URITemplateAction(
                        label='巷弄',
                        uri='https://i.imgur.com/fq034OP.jpg'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/65KSqgr.jpg',
                    action=URITemplateAction(
                        label='巷弄(站)',
                        uri='https://i.imgur.com/65KSqgr.jpg'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/rdjEYNk.jpg',
                    action=URITemplateAction(
                        label='等車的鴿們',
                        uri='https://i.imgur.com/rdjEYNk.jpg'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/Bkz5LU9.jpg',
                    action=URITemplateAction(
                        label='等車的鴿們(站)',
                        uri='https://i.imgur.com/Bkz5LU9.jpg'
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
                    image_url='https://i.imgur.com/MjvPRiq.jpg',
                    action=URITemplateAction(
                        label='幸福餅乾(坐)',
                        uri='https://i.imgur.com/MjvPRiq.jpg'
                    )
                )
            ]
        )
    )
    return message


# =====================================寶藏巖躺著的照片推薦==========================================
# def photolaB_message():
#     message = TemplateSendMessage(
#         alt_text='寶藏巖躺姿推薦',
#         template=ImageCarouselTemplate(
#             columns=[
#                  ImageCarouselColumn(
#                      image_url='https://i.imgur.com/4PZvAlV.jpg',
#                      action=URITemplateAction(
#                          label='管中世界',
#                          uri='https://i.imgur.com/4PZvAlV.jpg'
#                      )
#                  ),
#                 ImageCarouselColumn(
#                     image_url='https://i.imgur.com/RkrmZjH.jpg',
#                     action=URITemplateAction(
#                         label='管中世界(躺)',
#                         uri='https://i.imgur.com/RkrmZjH.jpg'
#                     )
#                  ),
#                 ImageCarouselColumn(
#                     image_url='https://i.imgur.com/1DHNhgM.jpg',
#                     action=URITemplateAction(
#                         label='長椅下午后',
#                         uri='https://i.imgur.com/1DHNhgM.jpg'
#                     )
#                  ),
#                 ImageCarouselColumn(
#                     image_url='https://i.imgur.com/MkPeQQY.jpg',
#                     action=URITemplateAction(
#                         label='長椅下午后(躺)',
#                         uri='https://i.imgur.com/MkPeQQY.jpg'
#                     )
#                  )
#             ]
#         )
#     )
#     return message


# =====================================自來水博物館站姿的照片推薦=======================================
def photoStW_message():
    message = TemplateSendMessage(
        alt_text='自來水博物館站姿推薦',
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
                    image_url='https://i.imgur.com/YpBmGQY.jpg',
                    action=URITemplateAction(
                        label='扭曲水管(站)',
                        uri='https://i.imgur.com/YpBmGQY.jpg'
                    )
                ),
            ]
        )
    )
    return message


# ==================================自來水博物館坐姿的照片推薦=========================================
# def photoSiW_message():
#     message = TemplateSendMessage(
#         alt_text='自來水博物館坐姿推薦',
#         template=ImageCarouselTemplate(
#             columns=[
#                 ImageCarouselColumn(
#                     image_url='https://i.imgur.com/xuS9nUe.jpg',
#                     action=URITemplateAction(
#                         label='幸福餅乾',
#                         uri='https://i.imgur.com/xuS9nUe.jpg'
#                     )
#                 ),
#                 ImageCarouselColumn(
#                     image_url='https://i.imgur.com/xuS9nUe.jpg',
#                     action=URITemplateAction(
#                         label='幸福餅乾(坐)',
#                         uri='https://i.imgur.com/xuS9nUe.jpg'
#                     )
#                 )
#             ]
#         )
#     )
#     return message


# =====================================自來水廠躺著的照片推薦==========================================
def photolaW_message():
    message = TemplateSendMessage(
        alt_text='自來水博物館躺姿推薦',
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
                    image_url='https://i.imgur.com/UVbVxkQ.jpg',
                    action=URITemplateAction(
                        label='管中世界(躺)',
                        uri='https://i.imgur.com/UVbVxkQ.jpg'
                    )
                 ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/1DHNhgM.jpg',
                    action=URITemplateAction(
                        label='長椅',
                        uri='https://i.imgur.com/1DHNhgM.jpg'
                    )
                 ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/qJLJPpw.jpg',
                    action=URITemplateAction(
                        label='長椅(躺)',
                        uri='https://i.imgur.com/qJLJPpw.jpg'
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
                        text="啟動相機"
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
            thumbnail_image_url='https://i.imgur.com/xdZ779W.png',
            title='想了解那裡的歷史呢?',
            text='選擇想要的地點',
            actions=[
                MessageTemplateAction(
                    label='我想瞭解寶藏巖',
                    text='瞭解歷史:寶藏巖',
                ),
                MessageTemplateAction(
                    label='我想瞭解自來水博物館',
                    text='瞭解歷史:自來水博物館',
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
    message0 = TemplateSendMessage(
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
    message1 = TextSendMessage(text='「寶藏巖介紹」\n福和橋下自來水廠附近的寶藏巖，屬於歷史型態聚落，' +
                               '具地景特殊性，景觀可見蜿蜒巷弄，階梯隨著緩坡起落，並沿著周圍山丘構築出天然地景與聚落錯落之風貌')
    return message0, message1


# ===================================寶藏巖更多介紹=========================================
def HistoryBIntro():
    message0 = TextSendMessage(text='寶藏巖又稱寶藏巖觀音寺、寶藏巖觀音亭、寶藏巖寺、石壁潭寺、觀音媽廟等\n' +
                               '靠虎空山小山坡而建，為福建泉州安溪移民的信仰中心，主奉觀音菩薩，1997年8月5日，' +
                               '由臺北市政府公告指定「寶藏巖」為市定古蹟')
    message1 = TextSendMessage(text='「寶藏巖國際藝術村」以「聚落共生」概念引入「寶藏家園」、「駐村計畫」與「青年會所」等計劃，用藝、居共構的做法' +
                               '活化保存歷時兩、三百年的山邊佛寺寶藏巖，注入了寶藏巖新的生命力')
    return message0, message1


# ====================================自來水廠對照========================================
def HistoryW_message():
    message0 = TemplateSendMessage(
        alt_text='先看看自來水博物館的今昔對比',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/3K6Kl1s.png',
                    action=URITemplateAction(
                        label='自來水博物館(今)',
                        uri='https://i.imgur.com/3K6Kl1s.png'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/YA3NPS5.png',
                    action=URITemplateAction(
                        label='自來水博物館(昔)',
                        uri='https://i.imgur.com/YA3NPS5.png'
                    )
                )
            ]
        )
    )
    message1 = TextSendMessage(
        text='「自來水博物館介紹」\n位於台北市公館的思源路上的自來水博物館，是台灣第一座自來水博物館')
    return message0, message1


# =================================自來水博物館介紹=======================================
def HistoryWIntro():
    message0 = TextSendMessage(text='民眾夏日消暑、戶外教學、新人婚紗攝影的最佳地點，' +
                               '自西元1908創建迄今己有100多年的歷史，於民國82年6月被內政部列為三級古蹟')
    message1 = TextSendMessage(text='唧筒室的正面，半圓弧由圓柱構成的門廊為愛奧尼柱式的門廊，外型則是仿自古希臘神殿，' +
                               '具地景特殊性，景觀可見蜿蜒巷弄，階梯隨著緩坡起落，並沿著周圍山丘構築出天然地景與聚落錯落之風貌' +
                               '融合古希臘、羅馬及巴洛克等建築風格，兼有莊嚴古典外觀與象徵現化功能的水源地唧筒室，就是在這種特定的社會歷史脈絡下所建構的')
    return message0, message1


def MoreInfo_message(L):
    if L == '2B':
        message = TextSendMessage(
            text='想要瞭解更多嗎?',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageTemplateAction(
                            imageUrl='https://i.imgur.com/CXFNuhB.png',
                            label='我想瞭解寶藏巖',
                            text='瞭解更多:寶藏巖',
                        ),
                    )
                ]
            )
        )
        return message
    elif L == '2W':
        message = TextSendMessage(
            text='想要瞭解更多嗎?',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageTemplateAction(
                            imageurl='https://i.imgur.com/CXFNuhB.png',
                            label='我想瞭解自來水博物館',
                            text='瞭解更多:自來水博物館',
                        ),
                    )
                ]
            )
        )
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
    message0 = TextSendMessage(text='點選下面選單，將出現功能選擇列表\n從左到右分別代表:')
    message1 = TextSendMessage(
        text='「美食好好知」\n 推薦你水源里的美食時，一邊讓你了解美食背後鮮為人知的小秘密。')
    message2 = TextSendMessage(
        text='「拍照打卡熱點」\n 不知道怎麼拍出打卡美照嗎?\n 沒關係!我教你如何在水源里的熱門景點拍出網美照')
    message3 = TextSendMessage(
        text='「歷史循跡」\n 想知道水源里以前的樣子嗎?\n 我們蒐集了水源里各處的新舊照片，快來比較看看吧!')
    message4 = TextSendMessage(text='從左到右分別代表:')
    return message0, message1, message2, message3, message4
