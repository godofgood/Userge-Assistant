# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge-Assistant > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Userge-Assistant/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ["Config"]

import os

from dotenv import load_dotenv

if os.path.isfile("config.env"):
    load_dotenv("config.env")


class Config:
    """ assistant configs """
    APP_ID = int(os.environ.get("1511336", 0))
    API_HASH = os.environ.get("8f670902d751008396e20f91505892b6")
    BOT_TOKEN = os.environ.get("1272994884:AAECqOlERs6M0RVwbgBIs4A2h5yX03zkACY")
    AUTH_CHATS = set([-1001169690724])  # @Hacking_burners
    if os.environ.get("AUTH_CHATS"):
        AUTH_CHATS.update(map(int, os.environ.get("AUTH_CHATS").split()))
    WHITELIST_CHATS = set([-1001169690724])  # @Hacking_burners
    if os.environ.get("WHITELIST_CHATS"):
        WHITELIST_CHATS.update(map(int, os.environ.get("WHITELIST_CHATS").split()))
    DEV_USERS = (
        1013793759,  # @Legitxd
        
    )
    ADMINS = {}
    MAX_MSG_LENGTH = 4096
