import arcade

from .physics import rigidbody, thruster, transform


class SpaceView(arcade.View):

    def __init__(self):
        super().__init__()
        self.test_transform = transform.Transform()
        self.test_body = rigidbody.RigidBody(self.test_transform)
        self.test_controller = thruster.ThrusterController(self.test_body, {'thrust': [thruster.Thruster(),
                                                                                       thruster.Thruster()]})

    def on_update(self, delta_time: float):
        thruster.ThrusterController.all_fire()
