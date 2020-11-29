# ===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
# ===========================LINEAPI==============================


def Food_message():
    message = TemplateSendMessage(
        alt_text='最近美食資訊',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://drive.google.com/file/d/1Lc7TEnZ3liqrlPTQ_vUC2J3vvtK9N69b/preview',
                    title='兄弟蚵仔麵線',
                    text='堅持傳統口味的用心維持了近三十年',
                    actions=[
                        PostbackTemplateAction(
                            label='我喜歡這家店',
                            data='使用者喜歡'
                        ),
                        URITemplateAction(
                            label='100台北市中正區汀州路三段235號',
                            uri='https://goo.gl/maps/FodenKrdkMt7Kq4Z7'
                        ),
                        # MessageTemplateAction(
                        #     label='用戶發送訊息',
                        #     text='我知道這是1'
                        # )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                    title='這是第二塊模板',
                    text='副標題可以自己改',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是2'
                        ),
                        URITemplateAction(
                            label='進入2的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
                    title='這是第三個模塊',
                    text='最多可以放十個',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=3'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是3'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png'
                        )
                    ]
                )
            ]
        )
    )
    return message
    # message = TemplateSendMessage(
    #     alt_text='最近美食資訊',
    #     template=CarouselTemplate(
    #         columns=[
    #             CarouselColumn(
    #                 thumbnail_image_url='https://drive.google.com/file/d/1Lc7TEnZ3liqrlPTQ_vUC2J3vvtK9N69b/view?usp=sharing',
    #                 title='兄弟蚵仔麵線',
    #                 text='堅持傳統口味的用心維持了近三十年',
    #                 actions=[
    #                     PostbackTemplateAction(
    #                         label='我喜歡這家店',
    #                         data='使用者喜歡'
    #                     ),
    #                     URITemplateAction(
    #                         label='100台北市中正區汀州路三段235號',
    #                         uri='https://goo.gl/maps/FodenKrdkMt7Kq4Z7'
    #                     ),
    #                     MessageTemplateAction(
    #                         label='用戶發送訊息',
    #                         text='我知道這是1'
    #                     )
    #                 ]
    #             ),
    #             CarouselColumn(
    #                 thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
    #                 title='這是第二塊模板',
    #                 text='副標題可以自己改',
    #                 actions=[
    #                     PostbackTemplateAction(
    #                         label='回傳一個訊息',
    #                         data='這是ID=2'
    #                     ),
    #                     MessageTemplateAction(
    #                         label='用戶發送訊息',
    #                         text='我知道這是2'
    #                     ),
    #                     URITemplateAction(
    #                         label='進入2的網頁',
    #                         uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
    #                     )
    #                 ]
    #             )
    #         ]
    #     )
    # )
    # return message
