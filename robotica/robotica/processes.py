#!/usr/bin/env python3

import subprocess
import time
import rclpy
from rclpy.node import Node

class PX4Launcher(Node):
    def __init__(self):
        super().__init__('px4_launcher_node')
        self.get_logger().info('PX4 Launcher Node Initialized')
        self.run_commands()

    def run_commands(self):
        val = "0,1"

        commands = [
            "MicroXRCEAgent udp4 -p 8888",
            "cd ~/PX4-Autopilot && make px4_sitl gz_x500"
        ]

        for command in commands:
            self.get_logger().info(f"Running: {command}")
            subprocess.run(["gnome-terminal", "--tab", "--", "bash", "-c", command + "; exec bash"])
            time.sleep(1)

def main(args=None):
    rclpy.init(args=args)
    node = PX4Launcher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
