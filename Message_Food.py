from linebot.models import *
from Message_Flex import *


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


# ===================================美食推薦=======================================


def Food_message(Location):
    if (Location == "K"):
        message = FlexSendMessage(
            alt_text='美食',
            contents=noodle
        )
        return message

        # ===================================水源市場美食推薦========================================

        # elif (Location == "W"):
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


# ======================================店家介紹===========================================
def Price(Location):
    if(Location == "M"):
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
    elif (Location == "Y"):
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
    elif (Location == "D"):
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


def GetInformatiom(Location):
    if(Location == "M"):
        message1 = TextSendMessage(text='「兄弟麵線介紹」\n堅持傳統口味的用心維持了近三十年，以前店面在東南亞劇院那邊的唱片行租房子賣麵線，'
                                   + '某一次房東提議店名要不要一起用“兄弟”這個名字，之後就決定叫做「“兄弟”蚵仔麵線」直到現在')
        # message1 = TextSendMessage(text='「故事」')
        return message1
    elif(Location == "Y"):
        message1 = TextSendMessage(
            text='「鴉片粉圓介紹」\n位於「公館商圈」一間隱匿於小巷的「鴉片粉圓」是你夏日消暑聖品！' +
            '飽滿嫩Ｑ粉圓搭配甘甜的沁脾的黑糖冰，如同冰品名稱「鴉片」，讓你一口接一口停不下來')
        message2 = TextSendMessage(
            text='隔壁的「得記麻辣脆皮臭豆腐」也是十分有名！酷熱的白天來碗通體舒暢的粉圓冰，入夜後就是來一鍋暖胃的麻辣臭豆腐！' +
            '清蒸臭豆腐搭上麻辣鴨血還有肥腸，一鍋又辣又臭的麻辣五更熱呼呼的端上桌！')
        message3 = TextSendMessage(
            '無論是因為天氣熱想先來碗，讓人上癮的「鴉片粉圓」消暑；' +
            '或是深夜後飢腸轆轆，想來一鍋餘味無窮的「得記麻辣臭豆腐」在這裡都是一個不錯的選擇')
        return message1, message2, message3
    elif (Location == "D"):
        message1 = TextSendMessage(text='「劉記蔥蛋餅」雖然外型酷似蔥油餅，但其實是蔥蛋餅，不一樣！')
        # message1 = TextSendMessage(text='「故事」')
        return message1


# =====================================發送愛心========================================
def Send_Heart(Location):
    if(Location == "M"):
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
