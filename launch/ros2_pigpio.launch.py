import os
import yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from yaml.loader import SafeLoader

def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('ros2_pigpio'),
        'config',
        'thrusters.yaml'
        )
    with open(config) as f:
        data = yaml.load(f, Loader=SafeLoader)
    
    thruster_fl_pin = data['thruster_fl']['ros__parameters']['pin']
    thruster_fr_pin = data['thruster_fr']['ros__parameters']['pin']
    thruster_rl_pin = data['thruster_rl']['ros__parameters']['pin']
    thruster_rr_pin = data['thruster_rr']['ros__parameters']['pin']
    thruster_ul_pin = data['thruster_ul']['ros__parameters']['pin']
    thruster_ur_pin = data['thruster_ur']['ros__parameters']['pin']

    return LaunchDescription([
        Node(
            package='ros2_pigpio',
            executable='gpio_pwm_writer',
            name='thruster_fl',
            parameters = [config],
            remappings = [('/gpio_pwm_{}'.format(thruster_fl_pin), '/thruster_fl')]
        ),
        Node(
            package='ros2_pigpio',
            executable='gpio_pwm_writer',
            name='thuster_fr',
            parameters= [config],
            remappings = [('/gpio_pwm_{}'.format(thruster_fr_pin), '/thruster_fr')]
        ),
        Node(
            package='ros2_pigpio',
            executable='gpio_pwm_writer',
            name='thuster_rl',
            parameters= [config],
            remappings = [('/gpio_pwm_{}'.format(thruster_rl_pin), '/thruster_rl')]
        ),
        Node(
            package='ros2_pigpio',
            executable='gpio_pwm_writer',
            name='thuster_rr',
            parameters= [config],
            remappings = [('/gpio_pwm_{}'.format(thruster_rr_pin), '/thruster_rr')]
        ),
        Node(
            package='ros2_pigpio',
            executable='gpio_pwm_writer',
            name='thuster_ul',
            parameters= [config],
            remappings = [('/gpio_pwm_{}'.format(thruster_ul_pin), '/thruster_ul')]
        ),
        Node(
            package='ros2_pigpio',
            executable='gpio_pwm_writer',
            name='thuster_ur',
            parameters= [config],
            remappings = [('/gpio_pwm_{}'.format(thruster_ur_pin), '/thruster_ur')]
        )
    ])