import rclpy
from robotont_msgs.msg import LedModuleMode, ColorRGB
from laserscan_to_ranges.msg import SimpleRanges
import os

node = None
pub_mode = None

def update_ranges(ranges):
    led_msg_mode = LedModuleMode()
    color = ColorRGB()
    color.r = min(int(ranges.left*100), 255)
    color.g = min(int(ranges.right*100), 255)
    color.b = min(int(ranges.front*100), 255)
    led_msg_mode.mode = led_msg_mode.SPIN
    led_msg_mode.color = color
    pub_mode.publish(led_msg_mode)
    #node.get_logger().info('Publishing: "%s"' % led_msg_mode)

def main(args=None):
    global pub_mode, node
    rclpy.init(args=args)
    node = rclpy.create_node('demo_lighting')
    pub_mode = node.create_publisher(LedModuleMode, 'led_mode', 10)
    sub_laserscan = node.create_subscription(SimpleRanges,'/simple_ranges', update_ranges, 10)
    try:
        rclpy.spin(node)
    except:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
