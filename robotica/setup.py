from setuptools import find_packages, setup

package_name = 'robotica'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='giovanni',
    maintainer_email='giovanni@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [
            'processes = robotica.processes:main',
            'vehicleposition = robotica.vehicleposition:main'
        ],
    },
)
