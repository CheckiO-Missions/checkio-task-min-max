from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.code import CheckiORefereeCode
from checkio.referees import cover_codes
from checkio.referees import checkers

from tests import TESTS

api.add_listener(
    ON_CONNECT,
    CheckiORefereeCode(
        tests=TESTS,
        # add_allowed_modules=[],
        add_close_builtins=["import", "__import__", "eval", "exec"],
        # remove_allowed_modules=[]
    ).on_ready)
