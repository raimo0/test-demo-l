import rclpy
from robotont_msgs.msg import LedModuleMode, ColorRGB
import random
import os

node = None
pub_mode = None
mode = 0

def change_mode():
    global mode
    led_msg_mode = LedModuleMode()
    color = ColorRGB()
    color.r = random.randint(0, 255)
    color.g = random.randint(0, 255)
    color.b = random.randint(0, 255)
    led_msg_mode.mode = mode
    led_msg_mode.color = color
    pub_mode.publish(led_msg_mode)
    #node.get_logger().info('Publishing: "%s"' % led_msg_mode)
    mode += 1
    if mode >= 6:
        mode = 0

def main(args=None):
    global pub_mode, node
    rclpy.init(args=args)
    node = rclpy.create_node('demo_lighting')
    pub_mode = node.create_publisher(LedModuleMode, 'led_mode', 10)
    node.create_timer(10, change_mode)
    try:
        rclpy.spin(node)
    except:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
