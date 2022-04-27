from arcade.key import *
import arcade

import src
from src.time import LOCAL_CLOCK, GLOBAL_CLOCK

M_MOD = 65535


class InputManager:
    KEY_MAP = {
        'up': UP,
        'down': DOWN,
        'left': LEFT,
        'right': RIGHT,
        'up_b': W,
        'down_b': S,
        'left_b': D,
        'right_b': A,
        'shoot': M_MOD+arcade.MOUSE_BUTTON_LEFT,
        'thrust': M_MOD+arcade.MOUSE_BUTTON_RIGHT
    }

    def __init__(self):
        self.this_frame_down: set = set()
        self.this_frame_up: set = set()

        self._mouse_pos = (0, 0)
        self._mouse_velocity = (0, 0)
        self.dragged = True

        self.symbols: dict[int, tuple[bool, float]] = {
            BACKSPACE: (False, -1.0),
            TAB: (False, -1.0),
            ENTER: (False, -1.0),
            ESCAPE: (False, -1.0),
            LEFT: (False, -1.0),
            UP: (False, -1.0),
            RIGHT: (False, -1.0),
            DOWN: (False, -1.0),
            NUM_0: (False, -1.0),
            NUM_1: (False, -1.0),
            NUM_2: (False, -1.0),
            NUM_3: (False, -1.0),
            NUM_4: (False, -1.0),
            NUM_5: (False, -1.0),
            NUM_6: (False, -1.0),
            NUM_7: (False, -1.0),
            NUM_8: (False, -1.0),
            NUM_9: (False, -1.0),
            F1: (False, -1.0),
            F2: (False, -1.0),
            F3: (False, -1.0),
            F4: (False, -1.0),
            F5: (False, -1.0),
            F6: (False, -1.0),
            F7: (False, -1.0),
            F8: (False, -1.0),
            F9: (False, -1.0),
            F10: (False, -1.0),
            F11: (False, -1.0),
            F12: (False, -1.0),
            F13: (False, -1.0),
            F14: (False, -1.0),
            F15: (False, -1.0),
            F16: (False, -1.0),
            LSHIFT: (False, -1.0),
            RSHIFT: (False, -1.0),
            LCTRL: (False, -1.0),
            RCTRL: (False, -1.0),
            SPACE: (False, -1.0),
            KEY_0: (False, -1.0),
            KEY_1: (False, -1.0),
            KEY_2: (False, -1.0),
            KEY_3: (False, -1.0),
            KEY_4: (False, -1.0),
            KEY_5: (False, -1.0),
            KEY_6: (False, -1.0),
            KEY_7: (False, -1.0),
            KEY_8: (False, -1.0),
            KEY_9: (False, -1.0),
            A: (False, -1.0),
            B: (False, -1.0),
            C: (False, -1.0),
            D: (False, -1.0),
            E: (False, -1.0),
            F: (False, -1.0),
            G: (False, -1.0),
            H: (False, -1.0),
            I: (False, -1.0),
            J: (False, -1.0),
            K: (False, -1.0),
            L: (False, -1.0),
            M: (False, -1.0),
            N: (False, -1.0),
            O: (False, -1.0),
            P: (False, -1.0),
            Q: (False, -1.0),
            R: (False, -1.0),
            S: (False, -1.0),
            T: (False, -1.0),
            U: (False, -1.0),
            V: (False, -1.0),
            W: (False, -1.0),
            X: (False, -1.0),
            Y: (False, -1.0),
            Z: (False, -1.0),
            M_MOD+arcade.MOUSE_BUTTON_LEFT: (False, -1.0),
            M_MOD+arcade.MOUSE_BUTTON_MIDDLE: (False, -1.0),
            M_MOD+arcade.MOUSE_BUTTON_RIGHT: (False, -1.0)
        }
        self.modifiers = 0

    def record_key_down(self, symbol, modifiers):
        self.this_frame_down.add(symbol)
        self.modifiers = modifiers

        self.symbols[symbol] = (True, LOCAL_CLOCK.time)

    def record_key_up(self, symbol, modifiers):
        self.this_frame_up.add(symbol)
        self.modifiers = modifiers

        self.symbols[symbol] = (False, -1.0)

    def record_mouse_down(self, button, x, y, modifiers):
        self.this_frame_down.add(M_MOD+button)
        self.modifiers = modifiers

        self._mouse_velocity = x - self._mouse_pos[0], y - self._mouse_pos[1]
        self._mouse_pos = (x, y)

        self.symbols[M_MOD+button] = (True, LOCAL_CLOCK.time)

    def record_mouse_up(self, button, x, y, modifiers):
        self.this_frame_up.add(M_MOD + button)
        self.modifiers = modifiers

        self._mouse_velocity = x - self._mouse_pos[0], y - self._mouse_pos[1]
        self._mouse_pos = (x, y)

        self.symbols[M_MOD + button] = (False, -1)
        self.dragged = False

    def record_mouse_motion(self, x, y, dx, dy):
        self._mouse_velocity = (dx, dy)
        self._mouse_pos = (x, y)

    def record_mouse_dragged(self, x, y, dx, dy):
        self.record_mouse_motion(x, y, dx, dy)
        self.dragged = True

    def cycle(self):
        self.this_frame_down = set()
        self.this_frame_up = set()

    def key_down(self, key):
        if isinstance(key, int):
            return key in self.this_frame_down
        elif isinstance(key, str):
            return InputManager.KEY_MAP[key] in self.this_frame_down

    def key_up(self, key):
        if isinstance(key, int):
            return key in self.this_frame_up
        elif isinstance(key, str):
            return InputManager.KEY_MAP[key] in self.this_frame_up

    def key_pressed(self, key):
        if isinstance(key, int):
            return self.symbols[key][0]
        elif isinstance(key, str):
            return self.symbols[InputManager.KEY_MAP[key]][0]

    def key_pressed_time(self, key):
        if isinstance(key, int):
            return LOCAL_CLOCK.time_since(self.symbols[key][1])
        elif isinstance(key, str):
            return LOCAL_CLOCK.time_since(self.symbols[InputManager.KEY_MAP[key]][1])

    def mouse_down(self, key):
        if isinstance(key, int):
            return M_MOD+key in self.this_frame_down
        elif isinstance(key, str):
            return InputManager.KEY_MAP[key] in self.this_frame_down

    def mouse_up(self, key):
        if isinstance(key, int):
            return M_MOD+key in self.this_frame_up
        elif isinstance(key, str):
            return InputManager.KEY_MAP[key] in self.this_frame_up

    def mouse_pressed(self, key):
        if isinstance(key, int):
            return self.symbols[M_MOD+key][0]
        elif isinstance(key, str):
            return self.symbols[InputManager.KEY_MAP[key]][0]

    def mouse_pressed_time(self, key):
        if isinstance(key, int):
            return LOCAL_CLOCK.time_since(self.symbols[M_MOD+key][1])
        elif isinstance(key, str):
            return LOCAL_CLOCK.time_since(self.symbols[InputManager.KEY_MAP[key]][1])

    def get_modifiers(self, key):
        try:
            if isinstance(key, int):
                return key & self.modifiers
            elif isinstance(key, str):
                return InputManager.KEY_MAP[key] & self.modifiers
        except KeyError:
            raise Exception("The key you input into InputManager.key_pressed_time is invalid.")

    @property
    def mouse_pos(self):
        return self._mouse_pos

    @property
    def mouse_velocity(self):
        return self._mouse_velocity


Input = InputManager()