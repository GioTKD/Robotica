import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import os
from datetime import datetime

class VehicleLocalPositionLogger(Node):
    def __init__(self):
        super().__init__('vehicle_local_position_logger')

        # Definisci il file e il topic associato
        self.file_name = 'vehicle_local_position.txt'
        self.topic = '/fmu/out/vehicle_local_position'

        # Crea la sottoscrizione per il topic
        self.create_subscription(String, self.topic, self.callback, 10)

        self.get_logger().info(f"Subscribed to {self.topic} and logging data to {self.file_name}")

    def callback(self, msg):
        """Callback per salvare i dati del topic nel file"""
        file_path = os.path.join(os.getcwd(), self.file_name)
        with open(file_path, 'a') as f:
            log_entry = f"{datetime.now()}: {msg.data}\n"
            f.write(log_entry)

        self.get_logger().info(f"Written data to {self.file_name}")

def main(args=None):
    rclpy.init(args=args)
    node = VehicleLocalPositionLogger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
