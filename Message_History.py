from linebot.models import *
# =====================================歷史地點==========================================


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
def History_message(Location):
    if(Location == "B"):
        message1 = TemplateSendMessage(
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
        message2 = TextSendMessage(text='「寶藏巖介紹」\n福和橋下自來水廠附近的寶藏巖，屬於歷史型態聚落，' +
                                   '具地景特殊性，景觀可見蜿蜒巷弄，階梯隨著緩坡起落，並沿著周圍山丘構築出天然地景與聚落錯落之風貌')
        return message1, message2
    elif(Location == "W"):
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


# ===================================更多歷史介紹=========================================
def HistoryIntro(Location):
    if(Location == "B"):
        message1 = TextSendMessage(text='寶藏巖又稱寶藏巖觀音寺、寶藏巖觀音亭、寶藏巖寺、石壁潭寺、觀音媽廟等\n' +
                                   '靠虎空山小山坡而建，為福建泉州安溪移民的信仰中心，主奉觀音菩薩，1997年8月5日，' +
                                   '由臺北市政府公告指定「寶藏巖」為市定古蹟')
        message2 = TextSendMessage(text='「寶藏巖國際藝術村」以「聚落共生」概念引入「寶藏家園」、「駐村計畫」與「青年會所」等計劃，用藝、居共構的做法' +
                                   '活化保存歷時兩、三百年的山邊佛寺寶藏巖，注入了寶藏巖新的生命力')
        return message1, message2
    if(Location == "W"):
        message1 = TextSendMessage(text='民眾夏日消暑、戶外教學、新人婚紗攝影的最佳地點，' +
                                   '自西元1908創建迄今己有100多年的歷史，於民國82年6月被內政部列為三級古蹟')
        message2 = TextSendMessage(text='唧筒室的正面，半圓弧由圓柱構成的門廊為愛奧尼柱式的門廊，外型則是仿自古希臘神殿，' +
                                   '具地景特殊性，景觀可見蜿蜒巷弄，階梯隨著緩坡起落，並沿著周圍山丘構築出天然地景與聚落錯落之風貌' +
                                   '融合古希臘、羅馬及巴洛克等建築風格，兼有莊嚴古典外觀與象徵現化功能的水源地唧筒室，就是在這種特定的社會歷史脈絡下所建構的')
        return message1, message2


# ===========================瞭解更多確認鈕================================
def MoreInfo_message(Location):
    if Location == 'B':
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
    elif Location == 'W':
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
