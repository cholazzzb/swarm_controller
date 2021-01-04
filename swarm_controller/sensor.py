import rclpy
from rclpy.node import Node

from tello_msgs.msg import FlightData

class MinimalSubscriber(Node):

    def __init__(self, drone_index):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            FlightData,
            '/drone'+ drone_index+ '/flight_data',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Drone 1 x: "%s"' % msg.x)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
