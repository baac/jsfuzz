"""
    This file checks if project is configurated
"""
from subprocess import call
from utils.constants import chakra, v8, javascriptcore, spidermonkey

ERROR_MSG = """\n########## ENVIRONMENT ERROR ##########\n Error: {}\n##########"""

def is_engines_installed():
    if not (chakra and v8 and javascriptcore and spidermonkey):
        raise Exception(
            ERROR_MSG.format(
                "Engines not found, please go to jsfuzz/js_engines folder and see the instructions"
            )
        )

def is_radamsa_installed():
    try:
        call(["radamsa", "-h"])
    except OSError:
        raise Exception(
            ERROR_MSG.format(
                "Radamsa not found, please go to jsfuzz/README.md and see the instructions"
            )
        )

is_engines_installed()
is_radamsa_installed()