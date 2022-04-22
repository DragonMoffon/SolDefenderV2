import arcade

from src.physics.linear import Vec2
from src.physics.rigidbody import RigidBody
from src import Input


class Thruster:

    def __init__(self):
        self.thrust = 1.0  # The force in Newtons that the thruster produces
        self.direction = Vec2(0.707, 0.707)  # The direction in which the thrust is applied - Normalised
        self.position = Vec2(0.0, 1.0)  # The position where the thrust is applied - with C.M. at origin (0, 0)

        self.throttle_percent = -1
        self.throttle_length = 0.5
        self.throttle = 0.0
        self.throttle_func = arcade.ease_in

    def fire(self, time):
        self.throttle_percent = min(time / self.throttle_length, 1.0)
        if self.throttle_percent > 0:
            self.throttle = self.throttle_func(self.throttle_percent)

            thrust = self.thrust * self.throttle * self.direction

            return thrust, self.position.cross(thrust)
        return Vec2(0), 0


class ThrusterController:

    Controllers: list = []

    def __init__(self, target: RigidBody, control_groups=None):
        if control_groups is None:
            control_groups = {}
        self.target = target
        self.control_groups: dict[any, list[Thruster]] = control_groups
        ThrusterController.Controllers.append(self)

    def delete(self):
        ThrusterController.Controllers.remove(self)

    def find_firing(self):
        total_force = Vec2(0)
        total_torque = 0
        for group, thrusters in self.control_groups.items():
            time = Input.key_pressed_time(group)
            results = tuple(zip(*[thruster.fire(time) for thruster in thrusters]))
            total_force += sum(results[0])
            total_torque += sum(results[1])

        self.target.add_force(total_force)
        self.target.add_torque(total_torque)

    @staticmethod
    def all_fire():
        for controller in ThrusterController.Controllers:
            controller.find_firing()
