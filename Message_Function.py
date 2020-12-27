# ===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
# ===========================LINEAPI==============================


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
                        image_url='https://i.imgur.com/2wbSWAD.png',
                        action=MessageTemplateAction(
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
                        image_url='https://i.imgur.com/2wbSWAD.png',
                        action=MessageTemplateAction(
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
    message4 = VideoSendMessage(
        original_content_url='https://example.com/original.mp4',
        preview_image_url='https://i.imgur.com/mtn1Tmw.jpg'
    )
    return message0, message1, message2, message3, message4
