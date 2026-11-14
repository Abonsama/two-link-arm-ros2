import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from arm_sim.fk import location
class JointSubscriber(Node):
    def __init__(self):
        super().__init__('JointSubscriber')
        self.create_subscription(Float64MultiArray,'joint_angles',self.listener_callback,10)
    def listener_callback(self, msg):
        a1=msg.data[0]
        a2=msg.data[1]
        # its like js destructuring 

        tip_x,tip_y = location(a1,a2,2,1)
        self.get_logger().info(f'the x position = {tip_x}, the y position ={tip_y} for angles {a1} and {a2}')

def main():
    rclpy.init()
    node = JointSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()