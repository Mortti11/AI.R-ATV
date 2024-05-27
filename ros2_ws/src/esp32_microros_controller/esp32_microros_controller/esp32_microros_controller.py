#!/usr/bin/env python3
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import Int32
from rclpy.qos import QoSProfile, ReliabilityPolicy


class Esp32ControllerNode(Node):

    def __init__(self):
        super().__init__('esp32_controller_node')
        topic = "/atv/speed_feedback"
        self.get_logger().info('Esp32ControllerNode is listening to Topic -> ' + topic)
        self.sub = self.create_subscription(Int32, topic, self.chatter_callback, 5)
        qos_profile = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)
        self.sub = self.create_subscription(Int32, topic, self.chatter_callback, qos_profile)

    def chatter_callback(self, msg: Int32):
        self.get_logger().info(str(msg))


def main(args=None):
    rclpy.init(args=args)
    node = Esp32ControllerNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
