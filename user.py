#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import (
    Client,
    __version__
)

from config import (
    API_HASH,
    APP_ID,
    LOGGER,
    TG_BOT_WORKERS,
)

TG_USER_SESSION = ("BQF3TIEAqUI8tHMPvkABoOCULrzSyTcLKGl13sEqa89wdQbAoCiU7a-ZsGtMLgAGku0z-y5B32eVqFewhsGfx3DH0jHiRJk9mAtzqz_2xGtvoeHScPf-HCJNPHHYHJSBgsVXCfwKY_YaSHkmCIV_9SDaCyNpXVbSR931yTKRUDtnASM9HKwNR_apMrBbejc209-MJS6IOwPmTt7oaAqhLxYl63ITvUmE3MrK1mJX4mjxOgKGGCi2XOi_DJjZV2pEGrwwhhyIpvxVfmYA11T8RQX59rLiNvYtHlZjEZ3MqBBGjTINwrFTJ8zVDJ-yGqEijGY6aEplOgl_S_A_ji4gab25uClwAAAAAAFE3SXbAA")


class User(Client):
    def __init__(self):
        super().__init__(
            TG_USER_SESSION,
            api_hash=API_HASH,
            api_id=APP_ID,
            workers=TG_BOT_WORKERS
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username}  started! \n\nSend a message in your channel now!!"
        )
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
 
