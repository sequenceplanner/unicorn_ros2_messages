#!/usr/bin/env python

from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_hrp1_sp_to_uni', output='screen'),
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_hrp1_uni_to_sp', output='screen'),
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_hrp2_sp_to_uni', output='screen'),
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_hrp2_uni_to_sp', output='screen'),
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_hrp_updater_sp_to_uni', output='screen'),
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_hrp_updater_uni_to_sp', output='screen')])