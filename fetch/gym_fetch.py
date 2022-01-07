from gym.utils import EzPickle
import numpy as np
from fetch import fetch_env


class GymFetchEnv(fetch_env.FetchEnv, EzPickle):
    def __init__(self, action, reward_type='sparse', n_substeps=20, dist_threshold=0.05):
        initial_qpos = {
            'robot0:slide0': 0.405,
            'robot0:slide1': 0.48,
            'robot0:slide2': 0.0,
        }
        if action == "reach":
            obj_keys, goal_key = None, "robot0:grip"
        else:
            initial_qpos['object0:joint'] = [1.25, 0.53, 0.6, 0, 0., 0., 0.]
            obj_keys = "object0",
            goal_key = "object0"

        if action == "slide":
            initial_qpos['robot0:slide0'] = 0.05
            initial_qpos['object0:joint'] = [1.7, 1.1, 0.41, 1., 0., 0., 0.]
            gripper_extra_height = -0.2
            target_offset = np.array([0.4, 0.0, 0.0])
            obj_range = 0.1
            target_range = 0.3
        else:
            gripper_extra_height = 0.2
            target_offset = 0.0
            obj_range = 0.15
            target_range = 0.15

        if action == "push":
            gripper_extra_height = 0.0
        if action in ["reach", "pick-place"]:
            gripper_extra_height = 0.2
        if action != "reach":
            obj_reset = {'object0': dict(track="gripper", avoid="gripper")}

        target_in_the_air = 0.5 if action in ['reach', 'pick-place'] else False
        block_gripper = action in ['reach', 'slide']

        local_vars = locals().copy()
        del local_vars['action']
        del local_vars['self']
        del local_vars['n_substeps']
        del local_vars['dist_threshold']

        fetch_env.FetchEnv.__init__(
            self, f"{action.replace('-', '_')}.xml",
            n_substeps=n_substeps,
            distance_threshold=dist_threshold,
            **local_vars)
        EzPickle.__init__(self)


class GymFetchFloorEnv(fetch_env.FetchFloorEnv, EzPickle):
    def __init__(self, action, reward_type='dense', n_substeps=20, dist_threshold=0.05):
        initial_qpos = {
            'robot0:slide0': 0.405,
            'robot0:slide1': 0.48,
            'robot0:slide2': 0.0,
        }
        obj_keys, goal_key = None, "robot0:grip"

        gripper_extra_height = 0.0  # Initial height of the tip
        target_offset = 0.0
        obj_range = 0.15
        target_range = 0.15

        target_in_the_air = False
        block_gripper = action in ['reach', 'slide']

        local_vars = locals().copy()
        del local_vars['action']
        del local_vars['self']
        del local_vars['n_substeps']
        del local_vars['dist_threshold']

        fetch_env.FetchFloorEnv.__init__(
            self, f"{action.replace('-', '_')}.xml",
            n_substeps=n_substeps,
            distance_threshold=dist_threshold,
            **local_vars)
        EzPickle.__init__(self)


if __name__ == '__main__':
    import gym

    env = gym.make('fetch:PickPlace-v0')
    env = gym.make('fetch:Push-v0')
    # env = gym.make('fetch:Bin-no-bin-v0')
