#!/usr/bin/env python3

from errbot import BotPlugin, botcmd
from urllib import error
import json
import requests

KEY = "REPLYGUYREPLIES"

class ReplyGuy(BotPlugin):
    """Stores replies to questions (links etc)

    """
    def initialize_persistence(self, key, empty):
        """Conditinonally initialize an empty
        container for persistence, but only if it
        is not currently bound"""
        self.log.info(f"Checking to see if {key} is available")
        if not self.get(key):
            self.log.info(f"Initializing {key} is available")
            self[key] = empty


    def get_trigger(self, word):
        """Lookup key."""
        with self.mutable(KEY) as triggers:
            self.log.info(f"triggers is {triggers} and its type is {type(triggers)} and it has {dir(triggers)}")
            response = triggers.get(word, "Seriously, are we not still doing phrasing?")
            self.log.info(f"Going to try to return {response}")
            return response

    def set_trigger(self, word, reply):
        """Lookup key."""
        with self.mutable(KEY) as triggers:
            former_reply = get_trigger(word)
            triggers.set(word, reply)
            if former_reply:
                return f"Set the phrase {word} to {reply} (was {former_reply})"
            return f"Set the phrase {word} to {reply}"


    @botcmd
    def rg_add(self, msg, trigger, reply):
        """
        (!rg add <trigger> <reply>) add a trigger phrase
        """
        self.initialize_persistence(KEY, dict())

        return self.set_trigger(trigger, reply)


    @botcmd
    def rg_del(self, msg, trigger):
        """
        (!rg del <trigger> ) removes a trigger phrase
        """
        self.initialize_persistence(KEY, dict())
        return "Elaborate voicemail hoax"


    @botcmd
    def rg_list(self, msg):
        """
        (!rg list ) lists triggers that gets this bot to respond
        """
        self.initialize_persistence(KEY, dict())
        return "Elaborate voicemail hoax"


    @botcmd
    def rg(self, msg, action=None, trigger=None, reply=None):
        """
        (!rg <trigger>) reply to the trigger phrase
        """
        return self.get_trigger(trigger)
