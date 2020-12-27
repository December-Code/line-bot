# ============================呼叫line bot chat model=============================================
from linebot.models import *


# ====================================拍照推薦地點=============================================
def photoLo_message():
    message = TextSendMessage(
        text="想要拍照了嗎?\n傳送你的地點，讓我們推薦最近的景點與姿勢",
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=LocationAction(
                        label="傳送我的地點",
                    ),
                ),
                QuickReplyButton(
                    action=CameraAction(
                        label="相機啟動",
                    ),
                )
            ]
        )
    )
    return message


def photo_UserLocation(Longitude, Latitude):
    message1 = TextSendMessage(text=Longitude)
    message2 = TextSendMessage(text=Latitude)
    return message1, message2

    # message = ImagemapSendMessage(
    #     base_url="https://i.imgur.com/cFFeXLt.png",
    #     alt_text="想要拍照了嗎 ?",
    #     base_size=BaseSize(height=1000, width=1000),
    #     actions=[
    #         MessageImagemapAction(
    #             text="拍照地點:公館商圈",
    #             area=ImagemapArea(
    #                 x=0, y=0, width=500, height=500
    #             )
    #         ),
    #         MessageImagemapAction(
    #             text="拍照地點:自來水博物館",
    #             area=ImagemapArea(
    #                 x=500, y=0, width=500, height=500
    #             )
    #         ),
    #         MessageImagemapAction(
    #             text="拍照地點:寶藏巖",
    #             area=ImagemapArea(
    #                 x=0, y=500, width=1000, height=500
    #             )
    #         )
    #     ]
    # )

    # ===================================照片的姿勢推薦=========================================


def photo_message(Location):
    # ================================公館商圈的照片推薦===================================
    if (Location == 'K'):
        message1 = TemplateSendMessage(
            alt_text='公館商圈站姿推薦',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/vSLhuNN.jpg',
                        action=URITemplateAction(
                            label='里長辦公室(站姿)',
                            uri='https://i.imgur.com/vSLhuNN.jpg'
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
        return message1
# ================================寶藏巖的照片推薦===================================
    elif (Location == 'B'):
        message1 = TemplateSendMessage(
            alt_text='寶藏巖站姿推薦',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/65KSqgr.jpg',
                        action=URITemplateAction(
                            label='巷弄(站)',
                            uri='https://i.imgur.com/65KSqgr.jpg'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/Bkz5LU9.jpg',
                        action=URITemplateAction(
                            label='等車的鴿們(站)',
                            uri='https://i.imgur.com/Bkz5LU9.jpg'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/MjvPRiq.jpg',
                        action=URITemplateAction(
                            label='幸福餅乾(坐)',
                            uri='https://i.imgur.com/MjvPRiq.jpg'
                        )
                    ),
                ]
            )
        )
        return message1
# ================================自來水廠的照片推薦===================================
    elif (Location == 'W'):
        message1 = TemplateSendMessage(
            alt_text='自來水博物館站姿推薦',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/YpBmGQY.jpg',
                        action=URITemplateAction(
                            label='扭曲水管(站)',
                            uri='https://i.imgur.com/YpBmGQY.jpg'
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
                        image_url='https://i.imgur.com/qJLJPpw.jpg',
                        action=URITemplateAction(
                            label='長椅(躺)',
                            uri='https://i.imgur.com/qJLJPpw.jpg'
                        )
                    )
                ]
            )
        )
        return message1


# =====================================相機開啟=======================================
def Camera_message():
    message1 = TextSendMessage(
        text="想要馬上嘗試嗎?",
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
    return message1
