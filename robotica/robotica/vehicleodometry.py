import rclpy
from rclpy.node import Node
from px4_msgs.msg import VehicleOdometry
from rclpy.qos import QoSProfile, ReliabilityPolicy
import os
from datetime import datetime

class VehicleOdometryLogger(Node):
    def __init__(self):
        super().__init__('vehicle_odometry_logger')

        # Definisci il file e il topic associato
        self.file_name = 'vehicle_odometry.txt'
        self.topic = '/fmu/out/vehicle_odometry'

        # Definisci una politica QoS meno restrittiva (Best Effort)
        qos_profile = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)

        # Crea la sottoscrizione per il topic con la politica QoS Best Effort
        self.create_subscription(VehicleOdometry, self.topic, self.callback, qos_profile)

        self.get_logger().info(f"Subscribed to {self.topic} and logging data to {self.file_name}")

    def callback(self, msg):
        """Callback per salvare i dati del topic nel file"""
        file_path = os.path.join(os.getcwd(), self.file_name)
        with open(file_path, 'a') as f:
            # Accedi agli elementi di 'position' e 'velocity' usando indici di array
            log_entry = (f"{datetime.now()}: x={msg.position[0]}, y={msg.position[1]}, z={msg.position[2]}, "
                         f"vx={msg.velocity[0]}, vy={msg.velocity[1]}, vz={msg.velocity[2]}\n")
            f.write(log_entry)

        self.get_logger().info(f"Written data to {self.file_name}")

def main(args=None):
    rclpy.init(args=args)
    node = VehicleOdometryLogger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
