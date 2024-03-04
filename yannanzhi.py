import json
import logging
import random
import urllib
import time
import hashlib
import requests
import nonebot
from nonebot.rule import Rule
from nonebot import on_command, on_startswith, on_keyword, on_fullmatch, on_message
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageEvent
from nonebot.adapters.onebot.v11 import GROUP_ADMIN, GROUP_OWNER, GROUP_MEMBER
from nonebot.typing import T_State
from nonebot.log import logger
from nonebot.params import ArgPlainText, CommandArg, ArgStr
from nonebot.adapters.onebot.v11 import Bot, GroupIncreaseNoticeEvent, \
    MessageSegment, Message, GroupMessageEvent, Event, escape

from pathlib import Path
import os


def dbqchecker():
    async def _checker(bot: Bot, event: Event, state: T_State) -> bool:
        s = str(event.get_event_description())
        if 'type=sticker' in s or 'subType=1' in s or 'subType=2' in s:  # 在这个位置写入你的判断代码
            return True  # 记住，返回值一定要是个bool类型的值！
        return False

    return Rule(_checker)





plugin_enabled = True  # 插件启用状态
dbq = on_message(rule=dbqchecker())

w1 = on_fullmatch(['滟南沚','test'])


# 添加中文注释
@w1.handle()
async def _handle():
    # 当w1收到消息时，发送消息
    await w1.send(random.choice(['我不在！别找我！','在呢！在呢！','干什么！！']))

w2 = on_fullmatch(['南南'])

@w2.handle()
async def _handle2():
    await w2.send('在的呦！')

   

#好友#好友#好友#好友#好友#好友#好友
#好友#好友#好友#好友#好友#好友#好友


w = on_fullmatch(['晚安'])
@w.handle()
async def _handle():
    await w.send(random.choice(['哦呀斯密！米娜桑！','晚安，好梦！拜拜！']))










#发送图片的代码


w = on_fullmatch(['？？？'])
@w.handle()
async def _handle():
    await w.send(MessageSegment.image('file:///C:/Users/Lianb/Desktop/0.jpg'))


# 柴郡猫表情包路径
#img_chaijuncat_path = Path(os.path.join(os.path.dirname(__file__), "cjmbq"))
#all_file_chaijuncat_name = os.listdir(str(img_chaijuncat_path))
#img_folder="C:/Users/Lianb/Desktop/lhcbot/cjmbq/"
#img_cj=random.choice('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27',


w = on_fullmatch(['柴郡'])
@w.handle()
async def _handle():
    await w.send(MessageSegment.image('file:///C:/Users/Lianb/Desktop/lhcbot/cjmbq/1.jpg'))
















