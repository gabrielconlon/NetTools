"""
credit for this module to SpookySec
https://github.com/SpookySec/OSINTed/blob/3a169d6dc2b4200938e18e9963c32b6d0480da8d/core/auto_complete.py#L43
"""

from resources import menus
import os, sys, readline, rlcompleter, glob

def tabCompleter(text, state):
    """
    complete commands from the list above
    """
    options = [i for i in menus.commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

def pathCompleter(text,state):
    """
    This is the tab completer for systems paths.
    """
    if '~' in text:
        text = os.path.expanduser('~')
    if os.path.isdir(text):
        text += '/'
    return [x for x in glob.glob(text + '*')][state]

def PathComplete():
    readline.set_completer(pathCompleter)

def CommandComplete():
    readline.set_completer(tabCompleter)

def HistoryClear():
    readline.clear_history()

readline.set_completer(tabCompleter)

if 'libedit' in readline.__doc__:
    readline.parse_and_bind("bind -e")
    readline.parse_and_bind("bind '\t' rl_comomplete'")
else:
    readline.parse_and_bind("tab: complete")