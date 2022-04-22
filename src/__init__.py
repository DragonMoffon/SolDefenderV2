from src.inputs import InputManager
from src.globals import GLOBALS, CONSTANTS


def local_time():
    return GLOBALS.LOCAL_CLOCK.elapsed


def global_time():
    return GLOBALS.GLOBAL_CLOCK.elapsed


def frame_count():
    return GLOBALS.GLOBAL_CLOCK.frame_count



