# How to run
Steps : 
1. Open Terminal and always run this code first:
```
cd ~/tello_ros_ws
source install/setup.bash
```
maybe or
```
cd ~/tello_ros_ws
source /opt/ros/eloquent/setup.bash
```
first
2. Run Gazebo + 2 Drone
```
export GAZEBO_MODEL_PATH=${PWD}/install/tello_gazebo/share/tello_gazebo/models
source /usr/share/gazebo/setup.sh
ros2 launch tello_gazebo two_drones_launch.py
```
2. Run service and topic UI
```
rqt
```

3. Run swarm controller package 
```
ros2 run swarm_controller swarm_controller 
```

4. After editing the swarm_controller packages, you need to build before the usage
```
colcon build --packages-select swarm_controller
```

5. See all script in setup.py

# Service usage lists :
/drone1/tello_action -> command to move the drone 1
/dronex/tello_action -> command to move the drone x


