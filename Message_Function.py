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
                    thumbnail_image_url='https://i.imgur.com/LupmODQ.jpg',
                    title='兄弟蚵仔麵線',
                    text='堅持傳統口味的用心維持了近三十年',
                    actions=[
                        PostbackTemplateAction(
                            label='我喜歡這家店',
                            data='使用者喜歡'
                        ),
                        LocationAction(
                            label='大約價錢：50 元',
                        ),
                        URITemplateAction(
                            label='100台北市中正區汀州路三段235號',
                            uri='https://goo.gl/maps/FodenKrdkMt7Kq4Z7'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/HOyJCWN.jpg',
                    title='鴉片粉圓',
                    text='「鴉片」一吃就上癮',
                    actions=[
                        PostbackTemplateAction(
                            label='我喜歡這家店',
                            data='使用者喜歡'
                        ),
                        LocationAction(
                            label='大約價錢：50 元',
                        ),
                        URITemplateAction(
                            label='100台北市中正區羅斯福路四段52巷16弄4號',
                            uri='https://goo.gl/maps/bUDeGy4QDjYFgCar9'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/HXNAAUG.jpg',
                    title='劉記古早味蔥蛋餅',
                    text='雖然外型酷似蔥油餅，但其實是蔥蛋餅，不一樣！',
                    actions=[
                        PostbackTemplateAction(
                            label='我喜歡這家店',
                            data='使用者喜歡'
                        ),
                        LocationAction(
                            label='大約價錢：45 元',
                        ),
                        URITemplateAction(
                            label='100台北市中正區羅斯福路四段108巷2-3號',
                            uri='https://goo.gl/maps/7H6dCPVUcVr3PuAv8'
                        )
                    ]
                ),
            ]
        )
    )
    return message

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
                    action=TemplateAction(
                        label="自來水廠_破壞水管(原)",
                        # uri="http://img.juimg.com/tuku/yulantu/110709/222-110F91G31375.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/lZSR4Bq.jpg",
                    action=TemplateAction(
                        label="自來水廠_破壞水管(站姿)",
                        # uri="https://cdn.101mediaimage.com/img/file/1410464751urhp5.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/4PZvAlV.jpg",
                    action=TemplateAction(
                        label="自來水廠_管中世界",
                        # uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/RkrmZjH.jpg",
                    action=TemplateAction(
                        label="自來水廠_管中世界('躺姿')",
                        # uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
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
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="可愛狗狗",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message

# =====================================躺著的照片推薦============================================


def photola_message():
    message = TemplateSendMessage(
        alt_text='坐姿推薦',
        template=ImageCarouselTemplate(
            columns=[
                 ImageCarouselColumn(
                     image_url="https://i.imgur.com/4PZvAlV.jpg",
                     action=TemplateAction(
                         label="自來水廠_管中世界",
                         # uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                     )
                 ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/RkrmZjH.jpg",
                    action=TemplateAction(
                        label="自來水廠_管中世界('躺姿')",
                        # uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                 ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="可愛狗狗",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                 ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                 )
            ]
        )
    )
    return message

# =====================================歷史對照============================================


def History_message():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/BfTFVDN.jpg",
        alt_text='最新的合作廠商有誰呢？',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                # 家樂福
                link_uri="https://tw.shop.com/search/%E5%AE%B6%E6%A8%82%E7%A6%8F",
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                # 生活市集
                link_uri="https://tw.shop.com/search/%E7%94%9F%E6%B4%BB%E5%B8%82%E9%9B%86",
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
        ]
    )
    return message
