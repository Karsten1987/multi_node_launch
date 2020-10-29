import os
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
from launch_ros.descriptions import ParameterFile
from launch.actions import SetLaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    explicit_default_file = os.path.join(
        get_package_share_directory('multi_node_launch'), 'my_node_explicit.yaml')
    implicit_default_file = os.path.join(
        get_package_share_directory('multi_node_launch'), 'my_node_implicit.yaml')
    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            'explicit_parameter_file',
            default_value=[explicit_default_file],
            description='Parameterfile for the node'),
        launch.actions.DeclareLaunchArgument(
            'implicit_parameter_file',
            default_value=[implicit_default_file],
            description='Parameterfile for the node'),
        SetLaunchConfiguration('my_node_ns', 'namespace_1'),
        launch_ros.actions.Node(
            package='multi_node_launch',
            executable='my_node',
            output='screen',
            name=['my_node'],
            namespace=launch.substitutions.LaunchConfiguration('my_node_ns'),
#            namespace='any_namespace',
            parameters=[
                ParameterFile(launch.substitutions.LaunchConfiguration('implicit_parameter_file'), allow_substs=True),
                ParameterFile(launch.substitutions.LaunchConfiguration('explicit_parameter_file'), allow_substs=True)
            ]),
        SetLaunchConfiguration('my_node_ns', 'namespace_2'),
        launch_ros.actions.Node(
            package='multi_node_launch',
            executable='my_node',
            output='screen',
            name=['my_node'],
            namespace=launch.substitutions.LaunchConfiguration('my_node_ns'),
#            namespace='any_other_workspace',
            parameters=[
                ParameterFile(launch.substitutions.LaunchConfiguration('implicit_parameter_file'), allow_substs=True),
                ParameterFile(launch.substitutions.LaunchConfiguration('explicit_parameter_file'), allow_substs=True)
            ]),
    ])
