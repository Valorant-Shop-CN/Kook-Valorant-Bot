from khl import Bot,Message
from ..utils.log import BotLog
from ..utils.KookApi import status_active_game,status_active_music,status_delete

def init(bot:Bot):
    # 开始打游戏
    @bot.command(name="gaming")
    async def gaming(msg: Message, game: int = 1):
        BotLog.log_msg(msg)
        #await bot.client.update_playing_game(3,1)# 英雄联盟
        if game == 1:
            ret = await status_active_game(453027)  # 瓦洛兰特
            await msg.reply(f"{ret['message']}，阿狸上号valorant啦！")
        elif game == 2:
            ret = await status_active_game(3)  # 英雄联盟
            await msg.reply(f"{ret['message']}，阿狸上号LOL啦！")


    # 开始听歌
    @bot.command(name="singing")
    async def singing(msg: Message, music: str = "err", singer: str = "err"):
        BotLog.log_msg(msg)
        if music == "err" or singer == "err":
            await msg.reply(f"函数参数错误，music: `{music}` singer: `{singer}`")
            return

        ret = await status_active_music(music, singer)
        await msg.reply(f"{ret['message']}，阿狸开始听歌啦！")


    # 停止打游戏1/听歌2
    @bot.command(name='sleeping')
    async def sleeping(msg: Message, d: int = 1):
        BotLog.log_msg(msg)
        ret = await status_delete(d)
        if d == 1:
            await msg.reply(f"{ret['message']}，阿狸下号休息啦!")
        elif d == 2:
            await msg.reply(f"{ret['message']}，阿狸摘下了耳机~")
        #await bot.client.stop_playing_game()
