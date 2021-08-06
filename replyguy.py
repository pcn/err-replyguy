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


    @arg_botcmd('action', type=str)
    @arg_botcmd('trigger', type=str)
    @arg_botcmd('reply', type=str)
    def rg(self, action, trigger=None, reply=None):
        """
        (!rg add <trigger> <reply>) add a trigger phrase
        (!rg list <trigger>) list trigger phrases
        (!rg del <trigger>) get rid of a trigger phrase
        (!rg <trigger>) reply to the trigger phrase
        """
        self.log.info(f"Got this action: {action}, trigger: {trigger}, reply: {reply}")
        self.initialize_persistence(KEY, dict())

        if action not in ('add', 'list', 'del'):
            return self.get_trigger(trigger)

        if action == 'add' and trigger is not None and reply is not None:
            return self.set_trigger(trigger, reply)

        if action == 'del' and trigger is not None:
            return "Elaborate voicemail hoax"

        if action == 'list':
            return "Elaborate voicemail hoax"

        return "I didn't know what to do with whatever that was"
