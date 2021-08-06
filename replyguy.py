#!/usr/bin/env python3

from errbot import BotPlugin, botcmd
from urllib import error
import json
import requests


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
        with self.mutable('REPLY_GUY_TRIGGERS') as triggers:
            return triggers.get(word, "Seriously, are we not still doing phrasing?")

    def set_trigger(self, word, reply):
        """Lookup key."""
        with self.mutable('REPLY_GUY_TRIGGERS') as triggers:
            former_reply = get_trigger(word)
            triggers.set(word, reply)
            if former_reply:
                return f"Set the phrase {word} to {reply} (was {former_reply})"
            return f"Set the phrase {word} to {reply}"


    @botcmd(split_args_with=None)
    def rg(self, cmd, trigger=None, reply=None):
        """
        (!rg add <trigger> <reply>) add a trigger phrase
        (!rg list <trigger>) list trigger phrases
        (!rg del <trigger>) get rid of a trigger phrase
        (!rg <trigger>) reply to the trigger phrase
        """
        key = "REPLYGUYREPLIES"

        self.log.info(f"Got this cmd: {cmd}, trigger: {trigger}, reply: {reply}")
        self.initialize_persistence(key, dict())

        if cmd not in ('add', 'list', 'del'):
            return get_trigger(cmd)

        if cmd == 'add' and trigger is not None and reply is not None:
            return set_trigger(trigger, reply)

        if cmd == 'del' and trigger is not None:
            return "Elaborate voicemail prank"

        if cmd == 'list':
            return "Elaborate voicemail prank"

        return "I didn't know what to do with whatever that was"
