from tello_msgs.srv import TelloAction
import rclpy
from rclpy.node import Node
import threading

## Todo
# Create White Noise -> Extended Kalman Filter to estimate the state after noise is given
# Create a plot x position and y position
# Create a plot about the disturbance (slide pptx konmul ahaw)

satuan = 0.05

# Commands
TAKEOFF = "takeoff"
LAND = "land"
def move(vx, vy, vz, yaw):
    print('vx: ', vx)
    print('vy: ', vy)
    print('vz: ', vz)
    print('yaw: ', yaw)

    return ("rc %d %d %d %d" % (vx, vy, vz, yaw))

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(TelloAction, '/drone1/tello_action')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = TelloAction.Request()

    def send_request(self):
        self.req.cmd = move(0.1, 0.1, 0, 0.5)
        self.future = self.cli.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    # Service
    minimal_client = MinimalClientAsync()
    minimal_client.send_request()

    # Timer
    # timer = rclpy.create_node('timer')
    ## Spin in a separate thread
    # thread = threading.Thread(target=rclpy.spin, args=(timer, ), daemon=True)
    # thread.start()

    # rate = timer.create_rate(0.5) #Hz

    try:
        while rclpy.ok():
            # Timer
            # print('Help me body, you are my only hope')
            # rate.sleep()
            
            # Service
            rclpy.spin_once(minimal_client)
            if minimal_client.future.done():
                try:
                    response = minimal_client.future.result()
                except Exception as e:
                    minimal_client.get_logger().info(
                        'Service call failed %r' % (e,))
                else:
                    minimal_client.get_logger().info('Success')
                break
    except KeyboardInterrupt:
        pass

    minimal_client.destroy_node()
    rclpy.shutdown()
    # thread.join()


if __name__ == '__main__':
    main()
