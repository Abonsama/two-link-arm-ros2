import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

class JointPublisher(Node):
    def __init__(self):
        super().__init__('joint_publisher')
        self.angle = 0.0
        self.pub = self.create_publisher(Float64MultiArray, 'joint_angles', 10)
        self.timer = self.create_timer(0.5, self.tick)

    def tick(self):
        msg = Float64MultiArray()
        msg.data = [self.angle, 0.1]
        self.pub.publish(msg)
        self.get_logger().info(f'angle = {self.angle}')
        self.angle += 5.0


def main():
    rclpy.init()
    node = JointPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()