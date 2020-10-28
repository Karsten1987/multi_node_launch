import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
from launch_ros.descriptions import ParameterFile
from launch.actions import SetLaunchConfiguration


def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            'parameter_file',
            default_value=[''],
            description='Parameterfile for the node'),
        SetLaunchConfiguration('my_node_ns', 'namespace_1'),
        launch_ros.actions.Node(
            package='multi_node_launch',
            executable='my_node',
            output='screen',
            name=['my_node'],
            namespace=launch.substitutions.LaunchConfiguration('my_node_ns'),
            parameters=[ParameterFile(launch.substitutions.LaunchConfiguration('parameter_file'), allow_substs=True)]),
        SetLaunchConfiguration('my_node_ns', 'namespace_2'),
        launch_ros.actions.Node(
            package='multi_node_launch',
            executable='my_node',
            output='screen',
            name=['my_node'],
            namespace=launch.substitutions.LaunchConfiguration('my_node_ns'),
            parameters=[ParameterFile(launch.substitutions.LaunchConfiguration('parameter_file'), allow_substs=True)]),
    ])
