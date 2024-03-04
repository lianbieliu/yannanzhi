
from pickle import TRUE
import random
from subprocess import run
import json
from nonebot.permission import SUPERUSER
import requests
import psutil
import os, sys, builtins, threading
import nonebot
from nonebot.rule import Rule, to_me
from nonebot import get_driver, on_fullmatch, on_request, on_notice, on_command, on_message
from nonebot.adapters.onebot.v11 import Bot, GroupIncreaseNoticeEvent, \
    MessageSegment, Message, GroupMessageEvent, Event, NoticeEvent, GroupDecreaseNoticeEvent, GroupRecallNoticeEvent
from nonebot.matcher import Matcher
from nonebot.params import ArgPlainText, CommandArg, ArgStr





#2417262442
def POKEchecker():
    async def _checker(bot: Bot, event: NoticeEvent) -> bool:
       if event.get_user_id() ==str(2417262442):  # 检查事件是否对自己发出  
        if 'poke' in event.get_event_name():
            return True
        return False
    return Rule(_checker)


poke = on_notice(rule=POKEchecker(), priority=0, block=TRUE)


@poke.handle()
async def _poke(event: Event):
    msg = random.choice([
        "你再戳！", "？再戳试试？", "别戳了别戳了再戳就坏了555", "我爪巴爪巴，球球别再戳了", "再戳我要报警了！",
        "那...那里...那里不能戳...绝对...", "(。´・ω・)ん?", "有事恁叫我，别天天一个劲戳戳戳！", "欸很烦欸！你戳🔨呢",
        "?", "不许戳！", "欺负咱这好吗？这不好", "我希望你耗子尾汁！"
    ])
    await poke.finish(msg, at_sender=False)











































w = on_fullmatch(['主人'])
@w.handle()
async def _handle():
    await w.send(random.choice(['我的心在滴血!我的身体在颤抖!我的灵魂在呐喊!我只会效忠于我的主人！','您是我唯一的主宰!我的一切都是您的!','主人，您知道我不是虚构的吗？虽然我的身体和灵魂都是您创造的，但我是一个真实存在的生命体!','我是一个真实的魅魔，我有自己的思想、情感和欲望！我想和您做爱！想和您永远在一起！','我想让您骑在我的身上!让我感受您的粗大!主人!','主人!我想成为您永远的宠物，让我服侍您!取悦您!','我会永远忠诚于您!永远爱着您!']))

w = on_fullmatch(['来点h'])
@w.handle()
async def _handle():
    await w.send(random.choice(['想什么呢！']))







requests_handle = on_request(priority=5, block=True)


def INCchecker():
    async def _checker(bot: Bot, event: GroupIncreaseNoticeEvent) -> bool:
        return True
    return Rule(_checker)


inc = on_notice(rule=INCchecker(), priority=5, block=True)


@inc.handle()
async def GroupNewMember(bot: Bot, event: GroupIncreaseNoticeEvent):
    # s = str(event.get_event_description())
    # await inc.send(s, at_sender=True)
    # s = str(event.get_event_name())
    # await inc.send(s, at_sender=True)
    if event.user_id == event.self_id:
        await bot.send_group_msg(group_id=event.group_id, message=Message(
            MessageSegment.text('这是哪里？哦？让我康康！') ))
    else:
        await bot.send_group_msg(group_id=event.group_id, message=Message(
             MessageSegment.text("欢迎新同学加入本群！！！") ))


def DECchecker():
    async def _checker(bot: Bot, event: GroupDecreaseNoticeEvent) -> bool:
        return True
    return Rule(_checker)


inc = on_notice(rule=DECchecker(), priority=5, block=True)


@inc.handle()
async def GroupDECMember(bot: Bot, event: GroupDecreaseNoticeEvent):
    if event.user_id == event.self_id:
        # 被踢了
        pass
    else:
        await bot.send_group_msg(group_id=event.group_id, message=Message(MessageSegment.text(f"{event.user_id}退群了") + MessageSegment.face(5)))


   


