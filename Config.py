import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 1578262)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(715779594)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "1487403789:AAH_OYwuWuF6lfQZTo33S_7idzy6oQmohvk"
    DATABASE_URL = "postgres://ckukrcziykaejp:54e9272421b670c8a9359b65eb12fb3bc4914864788ee214693f25b21854d67c@ec2-54-205-248-255.compute-1.amazonaws.com:5432/d64pfa0kvkh6km"
    APP_ID = "1578262"
    API_HASH = "664ecb8d62405ae3e3e015216f6e2615"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(715779594)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and I will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn off ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
        "**Developed by @AbirHasan2005**\nTelegram Group: @linux_repo\nOur Bot's Updates: @Discovery_Updates"
      ]

      START_MSG = "**Hi, [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
