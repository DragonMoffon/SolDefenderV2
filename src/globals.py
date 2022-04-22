import src.time as time


class Constants:
    pass


class Globals:
    GLOBAL_CLOCK: time.GlobalClock = time.GlobalClock()
    LOCAL_CLOCK: time.Clock = GLOBAL_CLOCK.clocks[0]


GLOBALS = Globals()
CONSTANTS = Constants()