# How to run
Steps : 
1. Open Terminal and always run this code first:
```
cd ~/tello_ros_ws
source install/setup.bash
```
first
2. Run Gazebo + 2 Drone
```
export GAZEBO_MODEL_PATH=${PWD}/install/tello_gazebo/share/tello_gazebo/models
source /usr/share/gazebo/setup.sh
ros2 launch tello_gazebo two_drones_launch.py
```
3. Run swarm controller package
```
ros2 run swarm_controller swarm_controller 
```