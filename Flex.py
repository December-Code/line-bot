# # ===============這些是LINE提供的功能套組，先用import叫出來=============
# from linebot import (LineBotApi, WebhookHandler)
# from linebot.exceptions import (InvalidSignatureError)
# from linebot.models import *


# def FoodW_message():
#     message = FlexSendMessage(
#         alt_text='hello',
#         contents=index
#     )
#     return message


# index = {
#     "type": "bubble",
#     "hero": {
#         "type": "image",
#         "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_2_restaurant.png",
#         "size": "full",
#         "aspect_ratio": "20:13",
#         "aspect_mode": "cover"
#     },
#     "body": {
#         "type": "box",
#         "layout": "vertical",
#         "spacing": "md",
#         "contents": [
#             {
#                 "type": "text",
#                 "text": "Into the alpaca_training",
#                 "size": "xl",
#                 "weight": "bold"
#             },
#             {
#                 "type": "separator",
#                 "margin": "xxl"
#             },
#             {
#                 "type": "box",
#                 "layout": "vertical",
#                 "spacing": "sm",
#                 "contents": [
#                     {
#                         "type": "box",
#                         "layout": "baseline",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "Overall",
#                                 "weight": "bold",
#                                 "margin": "sm",
#                                 "flex": 0
#                             }
#                         ]
#                     },
#                     {
#                         "type": "box",
#                         "layout": "baseline",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "# 查詢所有 alpaca_training 中的資料",
#                                 "size": "sm",
#                                 "color": "#aaaaaa"
#                             }
#                         ]
#                     },
#                     {
#                         "type": "box",
#                         "layout": "baseline",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "alpaca_name",
#                                 "weight": "bold",
#                                 "margin": "sm",
#                                 "flex": 0
#                             }
#                         ]
#                     },
#                     {
#                         "type": "box",
#                         "layout": "baseline",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "# 依照 alpaca_name 查詢",
#                                 "size": "sm",
#                                 "color": "#aaaaaa"
#                             }
#                         ]
#                     },
#                     {
#                         "type": "box",
#                         "layout": "baseline",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "training",
#                                 "weight": "bold",
#                                 "margin": "sm",
#                                 "flex": 0
#                             }
#                         ]
#                     },
#                     {
#                         "type": "box",
#                         "layout": "baseline",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "# 依照 training 查詢",
#                                 "size": "sm",
#                                 "color": "#aaaaaa"
#                             }
#                         ]
#                     }
#                 ]
#             },
#             {
#                 "type": "separator",
#                 "margin": "xxl"
#             }
#         ]
#     },
#     "footer": {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#             {
#                 "type": "button",
#                 "style": "link",
#                 "color": "#1DB446",
#                 "action": {
#                     "type": "postback",
#                     "label": "Overall",
#                     "data": "Overall"
#                 }
#             },
#             {
#                 "type": "button",
#                 "style": "link",
#                 "color": "#1DB446",
#                 "action": {
#                     "type": "postback",
#                     "label": "alpaca_name",
#                     "data": "alpaca_name"
#                 }
#             },
#             {
#                 "type": "button",
#                 "style": "link",
#                 "color": "#1DB446",
#                 "action": {
#                     "type": "postback",
#                     "label": "training",
#                     "data": "training"
#                 }
#             }
#         ]
#     }
# }
