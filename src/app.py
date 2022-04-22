import arcade

import src
import src.space_view as space_view


class App(arcade.Window):

    def __init__(self):
        super().__init__(vsync=False, update_rate=1/144)
        self.space_view = space_view.SpaceView()

        self.show_view(self.space_view)

    def update(self, delta_time: float):
        src.GLOBALS.GLOBAL_CLOCK.tick(delta_time)

    def on_update(self, delta_time: float):
        src.Input.cycle()

    def on_key_press(self, symbol: int, modifiers: int):
        src.Input.record_key_down(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        src.Input.record_key_up(symbol, modifiers)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        src.Input.record_mouse_down(button, x, y, modifiers)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        src.Input.record_mouse_up(button, x, y, modifiers)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        src.Input.record_mouse_motion(x, y, dx, dy)

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, buttons: int, modifiers: int):
        src.Input.record_mouse_dragged(x, y, dx, dy)


def run():
    application = App()
    application.run()
