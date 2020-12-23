# def FoodW_message():
#     message = FlexSendMessage(
#         alt_text='測試',
#         contents=noodle
#     )
#     return message


noodle = {
    "type": "bubble",
    "hero": {
        "type": "image",
        "url": "https://i.imgur.com/LupmODQ.jpg",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
            "type": "uri",
            "label": "Line",
            "uri": "https://linecorp.com/"
        }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "%E5%85%84%E5%BC%9F%E9%BA%B5%E7%B7%9A",
                "weight": "bold",
                "size": "xl",
                "contents": []
            },
            {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                    {
                        "type": "icon",
                        "url": "https://i.imgur.com/IB5Xh7u.png",
                        "size": "md"
                    },
                    {
                        "type": "text",
                        "text": "234",
                        "weight": "bold",
                        "size": "lg",
                        "flex": 0,
                        "margin": "md",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "%E4%BA%BA%E6%8E%A8%E8%96%A6",
                        "size": "md",
                        "margin": "sm",
                        "contents": []
                    },
                    {
                        "type": "icon",
                        "url": "https://i.imgur.com/baY264N.png",
                        "size": "xxl",
                        "position": "relative",
                        "offsetStart": "12%"
                    },
                    {
                        "type": "text",
                        "text": "%E6%88%91%E6%8E%A8%E8%96%A6",
                        "weight": "regular",
                        "align": "end",
                        "action": {
                            "type": "postback",
                            "label": "店家推薦",
                            "text": "喜歡這家店:兄弟麵線",
                            "data": "使用者喜歡:兄弟麵線"
                        },
                        "contents": []
                    }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "margin": "lg",
                "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "%E5%9C%B0%E5%9D%80",
                                "weight": "bold",
                                "size": "md",
                                "color": "#AAAAAA",
                                "flex": 1,
                                "align": "start",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": "100%E5%8F%B0%E5%8C%97%E5%B8%82%E4%B8%AD%E6%AD%A3%E5%8D%80%E6%B1%80%E5%B7%9E%E8%B7%AF%E4%B8%89%E6%AE%B5235%E8%99%9F",
                                "weight": "bold",
                                "size": "md",
                                "color": "#666666",
                                "flex": 5,
                                "align": "start",
                                "wrap": True,
                                "contents": []
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Time",
                                "size": "md",
                                "color": "#AAAAAA",
                                "flex": 1,
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": "10%3A00%EF%BD%9E20%3A30%20%20(%E9%80%B1%E4%B8%80%E5%85%AC%E4%BC%91)",
                                "size": "md",
                                "flex": 5,
                                "wrap": True,
                                "contents": []
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "菜單(點擊)",
                    "text": "想知道價目表:兄弟麵線"
                },
                "height": "sm",
                "style": "primary"
            },
            {
                "type": "button",
                "action": {
                    "type": "message",
                    "label": "我想了解更多~",
                    "text": "我想了解更多:兄弟麵線"
                },
                "height": "sm",
                "style": "secondary"
            },
            {
                "type": "spacer",
                "size": "sm"
            }
        ]
    }
}
