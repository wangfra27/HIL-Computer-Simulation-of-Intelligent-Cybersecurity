import numpy as np
import cv2
import vista

camera_config = {'name': 'camera_front',
                 'rig_path': './RIG.xml',
                 'size': (200, 320)}

# lidar_config = {'name': 'lidar_3d',
#                 'yaw_res': 0.1,
#                 'pitch_res': 0.1,
#                 'yaw_fov': (-180., 180.)}

world = vista.World(trace_paths=['/Users/grace/Documents/vista_traces/20210726-155941_lexus_devens_center_reverse'],
                    trace_config={'road_width': 4})
car1 = world.spawn_agent(config={'length': 5.,
                                'width': 2.,
                                'wheel_base': 2.78,
                                'steering_ratio': 14.7,
                                'lookahead_road': True})
# car1.spawn_camera()
camera = car1.spawn_camera(camera_config)

car2 = world.spawn_agent(config={'length': 4.,
                                'width': 1,
                                'wheel_base': 2.78,
                                'steering_ratio': 14.7,
                                'lookahead_road': True})
# car2.spawn_lidar()
camera2 = car2.spawn_camera(camera_config)

display = vista.Display(world, 30)

world.reset()
display.reset()

from vista.utils import transform
from vista.entities.agents.Dynamics import tireangle2curvature

def pure_pursuit_controller(agent):
    # hyperparameters
    lookahead_dist = 5.
    Kp = 3.
    dt = 1 / 30.

    # get road in ego-car coordinates
    ego_pose = agent.ego_dynamics.numpy()[:3]
    road_in_ego = np.array([
        transform.compute_relative_latlongyaw(_v[:3], ego_pose)
        for _v in agent.road
    ])

    # find (lookahead) target
    dist = np.linalg.norm(road_in_ego[:,:2], axis=1)
    dist[road_in_ego[:,1] < 0] = 9999. # drop road in the back
    tgt_idx = np.argmin(np.abs(dist - lookahead_dist))
    dx, dy, dyaw = road_in_ego[tgt_idx]

    # simply follow human trajectory for speed
    speed = agent.human_speed

    # compute curvature
    arc_len = speed * dt
    curvature = (Kp * np.arctan2(-dx, dy) * dt) / arc_len
    curvature_bound = [
        tireangle2curvature(_v, agent.wheel_base)
        for _v in agent.ego_dynamics.steering_bound]
    curvature = np.clip(curvature, *curvature_bound)

    return np.array([curvature, speed])

def follow_human_trajectory(agent):
    action = np.array([
        agent.trace.f_curvature(agent.timestamp),
        agent.trace.f_speed(agent.timestamp)
    ])
    return action

while not car1.done:
    action = follow_human_trajectory(car1)
    action2 = pure_pursuit_controller(car2)
    car1.step_dynamics(action)
    car2.step_dynamics(action2)
    car1.step_sensors()
    car2.step_sensors()

    sensor_data = car1.observations
    sensor_data2 = car2.observations

    vis_img = display.render()
    cv2.imshow('Visualize control', vis_img[:, :, ::-1])
    cv2.waitKey(20)
