# def FoodW_message():
#     message = FlexSendMessage(
#         alt_text='測試',
#         contents=noodle
#     )
#     return message


# ===========================蚵仔麵線================================
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

# ===========================鴉片粉圓================================
opiumIce = {
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
                        "text": "鴉片粉圓",
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
                                "url": "https://i.imgur.com/baY264N.png",
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
                                      "text": "地址",
                                      "weight": "bold",
                                      "size": "md",
                                      "flex": 1,
                                      "align": "start",
                                      "contents": []
                                  },
                                    {
                                      "type": "text",
                                      "text": "台北市 中正區 羅斯福路四段 52巷 16弄 4號",
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
                                        "text": "12:00 ~ 23:30",
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


# ===========================劉記蛋餅================================

LiuEgg = {
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
                        "text": "劉記古早味蔥蛋餅",
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
                                "url": "https://i.imgur.com/baY264N.png",
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
                                      "text": "地址",
                                      "weight": "bold",
                                      "size": "md",
                                      "flex": 1,
                                      "align": "start",
                                      "contents": []
                                  },
                                    {
                                      "type": "text",
                                      "text": "台北市 中正區 羅斯福路 四段 108巷 2-3號",
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
                                        "text": "15:00 ~ 00:30  (週三、四休息)",
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
                          "text": "想知道價目表:劉記蔥蛋餅"
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

FoodK = {
    "type": "carousel",
    "contents": [
        noodle,
        # opiumIce,
        LiuEgg,
    ]
}
