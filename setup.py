from setuptools import setup

package_name = 'swarm_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='toro',
    maintainer_email='nicsphehehe@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'swarm_controller = swarm_controller.control_single_drone:main',
            'ros_timer = swarm_controller.interval_rclpy',
            'sensor = swarm_controller.sensor:main',
            'main = swarm_controller.controller'
        ],
    },
)
