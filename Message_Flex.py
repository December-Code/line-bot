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
                "text": "兄弟蚵仔麵線",
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
                        "text": "人推薦",
                        "size": "md",
                        "margin": "sm",
                        "contents": []
                    },
                    {
                        "type": "icon",
                        "url": "https://i.imgur.com/IB5Xh7u.png",
                        "size": "xxl",
                        "position": "relative",
                        "offsetStart": "12%"
                    },
                    {
                        "type": "text",
                        "text": "我推薦",
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
                                "text": "地址",
                                "weight": "bold",
                                "size": "md",
                                "flex": 1,
                                "align": "start",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": "台北市 中正區 汀州路三段 235號",
                                "weight": "bold",
                                "size": "md",
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
                                "text": "時間",
                                "weight": "bold",
                                "size": "md",
                                "flex": 1,
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": "10:00～20:30  (週一公休)",
                                "weight": "bold",
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
                    "label": "菜單",
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

FoodK = {
    "type": "carousel",
    "contents": [
            noodle,
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/HOyJCWN.jpg",
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
                        "text": "%E9%B4%89%E7%89%87%E7%B2%89%E5%9C%93",
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
                                    "text": "喜歡這家店:鴉片粉圓",
                                    "data": "使用者喜歡:鴉片粉圓"
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
                                      "flex": 1,
                                      "align": "start",
                                      "contents": []
                                  },
                                    {
                                      "type": "text",
                                      "text": "%E5%8F%B0%E5%8C%97%E5%B8%82%20%E4%B8%AD%E6%AD%A3%E5%8D%80%20%E7%BE%85%E6%96%AF%E7%A6%8F%E8%B7%AF%E5%9B%9B%E6%AE%B5%2052%E5%B7%B7%2016%E5%BC%84%204%E8%99%9F",
                                      "weight": "bold",
                                      "size": "md",
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
                                        "text": "%E6%99%82%E9%96%93",
                                        "weight": "bold",
                                        "size": "md",
                                        "flex": 1,
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "12%3A00%20~%2023%3A30",
                                        "weight": "bold",
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
                          "label": "菜單",
                          "text": "想知道價目表:鴉片粉圓"
                        },
                        "height": "sm",
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "我想了解更多~",
                            "text": "我想了解更多:鴉片粉圓"
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
        },
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/HXNAAUG.jpg",
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
                        "text": "%E5%8A%89%E8%A8%98%E5%8F%A4%E6%97%A9%E5%91%B3%E8%94%A5%E8%9B%8B%E9%A4%85",
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
                                    "text": "喜歡這家店:劉記蔥蛋餅",
                                    "data": "使用者喜歡:劉記蔥蛋餅"
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
                                      "flex": 1,
                                      "align": "start",
                                      "contents": []
                                  },
                                    {
                                      "type": "text",
                                      "text": "%E5%8F%B0%E5%8C%97%E5%B8%82%20%E4%B8%AD%E6%AD%A3%E5%8D%80%20%E7%BE%85%E6%96%AF%E7%A6%8F%E8%B7%AF%E5%9B%9B%E6%AE%B5%20108%E5%B7%B7%202-3%E8%99%9F",
                                      "weight": "bold",
                                      "size": "md",
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
                                        "text": "%E6%99%82%E9%96%93",
                                        "weight": "bold",
                                        "size": "md",
                                        "flex": 1,
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "15%3A00%20~%2000%3A30%20%20(%E9%80%B1%E4%B8%89%E3%80%81%E5%9B%9B%E4%BC%91%E6%81%AF)",
                                        "weight": "bold",
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
                            "text": "我想了解更多:劉記蔥蛋餅"
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
    ]
}
