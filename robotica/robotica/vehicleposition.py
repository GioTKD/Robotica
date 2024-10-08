import rclpy
from rclpy.node import Node
from px4_msgs.msg import VehicleLocalPosition
from rclpy.qos import QoSProfile, ReliabilityPolicy
import os
from datetime import datetime

class VehicleLocalPositionLogger(Node):
    def __init__(self):
        super().__init__('vehicle_local_position_logger')

        # Definisci il file e il topic associato
        self.file_name = 'vehicle_local_position.txt'
        self.topic = '/fmu/out/vehicle_local_position'

        # Definisci una politica QoS meno restrittiva (Best Effort)
        qos_profile = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)

        # Crea la sottoscrizione per il topic con la politica QoS Best Effort
        self.create_subscription(VehicleLocalPosition, self.topic, self.callback, qos_profile)

        self.get_logger().info(f"Subscribed to {self.topic} and logging data to {self.file_name}")

    def callback(self, msg):
        """Callback per salvare i dati del topic nel file"""
        file_path = os.path.join(os.getcwd(), self.file_name)
        with open(file_path, 'a') as f:
            # Logga solo i dati della posizione (x, y, z) e velocità (vx, vy, vz)
            log_entry = (f"{datetime.now()}: x={msg.x}, y={msg.y}, z={msg.z}, "
                         f"vx={msg.vx}, vy={msg.vy}, vz={msg.vz}\n")
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
