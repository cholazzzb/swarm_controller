import rclpy
from rclpy.node import Node

from sensor import MinimalSubscriber

rclpy.init(args=args)

Drone1Sensor = MinimalSubscriber(1)

rclpy.spin(Drone1Sensor)

# Destroy the node explicitly
# (optional - otherwise it will be done automatically
# when the garbage collector destroys the node object)
minimal_subscriber.destroy_node()
rclpy.shutdown()

