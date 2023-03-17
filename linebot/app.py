from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
import random
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('')
# Channel Secret
handler = WebhookHandler('')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    music = ['https://www.youtube.com/watch?v=sI4hjLyZewo','https://www.youtube.com/watch?v=TRuGk9A8LVI','https://www.youtube.com/watch?v=fdvKAPiXf8k','https://www.youtube.com/watch?v=KrFCTcms27k','https://www.youtube.com/watch?v=D8S0kpZPRoI','https://www.youtube.com/watch?v=2cEZrBf3DSo','https://www.youtube.com/watch?v=bhP11C2Eh30','https://www.youtube.com/watch?v=JttKF1HbrOY','https://www.youtube.com/watch?v=skIy22LEuZY','https://www.youtube.com/watch?v=HI8xz8qAffQ','https://www.youtube.com/watch?v=rozWdePEQfc','https://www.youtube.com/watch?v=4BLKP_sQvjs','https://www.youtube.com/watch?v=IAZ8rQLTnXY','https://www.youtube.com/watch?v=wGrkkDFwwmY','https://www.youtube.com/watch?v=OFRrQU5Yxdw','https://www.youtube.com/watch?v=FTIwIH_nVww','https://www.youtube.com/watch?v=Muzc9WXIbNQ','https://www.youtube.com/watch?v=FvQpsray8ks','https://www.youtube.com/watch?v=1EMnazAdeU4','https://www.youtube.com/watch?v=zrZD6dl9pww 酷酷的鬧鐘','https://www.youtube.com/watch?v=UKeROQF8HCU 彩蛋，送你大便片']
    nice_img = ['https://i.imgur.com/vGscZQH.jpg','https://i.imgur.com/C3311un.jpg','https://i.imgur.com/Gv9O9Yo.jpg','https://i.imgur.com/4NZcw4B.jpg','https://i.imgur.com/CiZTyyl.jpg','https://i.imgur.com/vkjIY7L.jpg','https://i.imgur.com/ZzRzjES.jpg','https://i.imgur.com/nj49uMQ.jpg','https://i.imgur.com/Z9sqpvn.jpg','https://i.imgur.com/xwh1zMD.jpg','https://i.imgur.com/IwYpzAt.jpg','https://i.imgur.com/cEZeZtO.jpg','https://i.imgur.com/ZRqZ6SN.jpg','https://i.imgur.com/pPwzPHh.jpg','https://i.imgur.com/EKEkAaV.jpg','https://i.imgur.com/8toIGaa.jpg','https://i.imgur.com/442iGGX.jpg','https://i.imgur.com/P7DN3a8.jpg','https://i.imgur.com/LmeBwXb.jpg','https://i.imgur.com/t319eWx.jpg']
    angry_img = ['https://i.imgur.com/RYx97JD.jpg','https://i.imgur.com/yCTZcIu.jpg','https://i.imgur.com/BQXn0on.jpg','https://i.imgur.com/N2D4uvC.jpg','https://i.imgur.com/kjlIlKC.jpg','https://i.imgur.com/l1zfJUv.jpg','https://i.imgur.com/JBVPLKa.jpg','https://i.imgur.com/tFnibzi.jpg','https://i.imgur.com/kbgS9rT.jpg','https://i.imgur.com/SmdDXte.jpg','https://i.imgur.com/EhuaWlE.jpg','https://i.imgur.com/2Nq4d0R.jpg','https://i.imgur.com/dFYaQwF.jpg','https://i.imgur.com/n2XZlx1.jpg','https://i.imgur.com/HAWXoUo.jpg','https://i.imgur.com/WhhuVTC.jpg']
    msg = event.message.text
    if '音樂' in msg:
        message = music[random.randint(0,20)]
        line_bot_api.reply_message(event.reply_token, TextSendMessage(music[random.randint(0,20)]))
    elif '好康' in msg:
        line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url=nice_img[random.randint(0,19)], preview_image_url='https://i.imgur.com/9FqZiRP.png'))
    elif '中風' in msg:
        message=angry_img[random.randint(0,15)]
        line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url=message, preview_image_url=message))
    elif '臭' in msg:
        line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url='https://i.imgur.com/Gyp5Osy.jpg', preview_image_url='https://i.imgur.com/Gyp5Osy.jpg'))
    elif '冰' in msg:
        line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url='https://i.imgur.com/F7wt2Qz.jpg', preview_image_url='https://i.imgur.com/F7wt2Qz.jpg'))
    elif '瑞' in msg:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('瑞斯一打三AAAAAAAAAA'))
    elif '巨' in msg:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('你看到我媽的巨... 你看到我大槌達瑞斯都不會怕的欸. 還在他媽還在前面那邊洗兵耶'))
    elif '你' in msg:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('你繼續C皮笑臉沒關係 老子就送到底 欸嘿送幸福囉')) 
    elif '轟' in msg:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('轟隆隆隆🤣🤣隆隆隆隆衝衝衝衝😏😏😏拉風😎😎😎引擎發動🔑🔑🔑引擎發動+🚗+👉+🚗'))
    elif '宋' in msg:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('小幫手ㄉ開發者嗎? 聽說很帥ㄋ😎😎😎'))    
    else:
        message = '再亂講話，鼻樑不保'
        line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url='https://i.imgur.com/QOjwxVc.png', preview_image_url='https://i.imgur.com/QOjwxVc.png'))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
