# Industrial Automation and Robotics Module B
## Goals of the project
The goal of this project is to create a simulation for record some data like:
* Position
* Velocity 
* Status
## Prerequisites
* ROS2 Humble
* PX4 Autopilot
* Micro XRCE-DDS Agent
* px4_msgs
* Ubuntu 22.04
* Python 3.10
## Setup
### Install PX4 Autopilot
```
cd
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
bash ./PX4-Autopilot/Tools/setup/ubuntu.sh
cd PX4-Autopilot/
make px4_sitl
```

Run this script in a bash shell to install everything

```
bash ./PX4-Autopilot/Tools/setup/ubuntu.sh
```
Before continue, reboot your pc.

### Install ROS2 Humble
```
To install ROS2 Humble:
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update && sudo apt upgrade -y
sudo apt install ros-humble-desktop
sudo apt install ros-dev-tools
source /opt/ros/humble/setup.bash && echo "source /opt/ros/humble/setup.bash" >> .bashrc
```
### Install Dependencies

Install Python dependencies with this code

```
pip install --user -U empy==3.3.4 pyros-genmsg setuptools
```

And:

```
pip3 install kconfiglib
pip install --user jsonschema
pip install --user jinja2
```

### Build Micro DDS
Follow this [PX4 Docs](https://docs.px4.io/main/en/ros/ros2_comm.html#setup-micro-xrce-dds-agent-client) in order to build MicroDDS on your machine

```
git clone https://github.com/eProsima/Micro-XRCE-DDS-Agent.git
cd Micro-XRCE-DDS-Agent
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig /usr/local/lib/
```
### Create Folder
First of all we need to create a folder in the home directory:
```
mkdir -p ~/(name)/src
```
After this, go in src folder and clone the px4_msgs repo:
```
git clone https://github.com/PX4/px4_msgs.git
git clone https://github.com/PX4/px4_ros_com.git
```
inside the new folder clone this repo:
```
git clone "https://github.com/GioTKD/Robotica"
```
### Wireshark Setup
To seup wireshark we need to create a plugin, in order to do this click [here](https://mavlink.io/en/guide/wireshark.html)
### Build
Before building source ROS2 installation(you need to run this for each terminal):
```
source /opt/ros/humble/setup.bash
```
Then go in the home directory, 
```
cd (name folder)
```
and run
```
colcon build
source install/local_setup.bash
```
once done, we will face a warning about setup.py, but it works.
Then:
```
source /opt/ros/humble/setup.bash
source install/setup.bash
```
### Run project
Once all is done launch the project:
```
ros2 run robotica processes
```
