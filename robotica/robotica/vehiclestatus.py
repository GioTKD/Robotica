import rclpy
from rclpy.node import Node
from px4_msgs.msg import VehicleStatus
from rclpy.qos import QoSProfile, ReliabilityPolicy
import os
from datetime import datetime

class VehicleStatusLogger(Node):
    def __init__(self):
        super().__init__('vehicle_status_logger')

        # Definisci il file e il topic associato
        self.file_name = 'vehicle_status.txt'
        self.topic = '/fmu/out/vehicle_status'

        # Definisci una politica QoS Best Effort
        qos_profile = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)

        # Crea la sottoscrizione per il topic con la politica QoS Best Effort
        self.create_subscription(VehicleStatus, self.topic, self.callback, qos_profile)

        self.get_logger().info(f"Subscribed to {self.topic} and logging data to {self.file_name}")

    def callback(self, msg):
        """Callback per salvare i dati del topic nel file"""
        file_path = os.path.join(os.getcwd(), self.file_name)
        with open(file_path, 'a') as f:
            log_entry = (f"{datetime.now()}: nav_state={msg.nav_state}, "
                         f"arming_state={msg.arming_state}, failsafe={msg.failsafe}\n")
            f.write(log_entry)

        self.get_logger().info(f"Written data to {self.file_name}")

def main(args=None):
    rclpy.init(args=args)
    node = VehicleStatusLogger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
