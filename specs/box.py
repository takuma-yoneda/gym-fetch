import gym
import numpy as np
from cmx import doc

scale = 3


def get_obs_spec(env_id):
    env = gym.make(env_id)
    buffer = []
    for k, v in env.observation_space.spaces.items():
        buffer += [f"{k}: {v.shape}"]
    return "<br>".join(buffer)


def render_initial(env_id, doc):
    env = gym.make(env_id)
    img = env.render('rgb_array', width=100 * scale, height=120 * scale)
    doc.image(img, caption="Initial")

    frames = []
    for i in range(10):
        env.reset()
        frames.append(env.render('rgb_array', width=100 * scale, height=120 * scale))

    doc.image(np.array(frames).min(axis=0), caption="After Reset")


def render_video(env_id, n, doc):
    env = gym.make(env_id)
    frames = []
    for ep in range(n):
        env.reset()
        for i in range(10):
            act = env.action_space.sample()
            ts = env.step(act)
            frames.append(env.render('rgb_array', width=100 * scale, height=120 * scale))

    doc.video(np.array(frames), f"{__file__[:-3]}/videos/{env_id}.gif", caption="After Reset")


if __name__ == '__main__':
    doc @ f"""
    # Box open and close Tasks

    This set includes two tasks: opening from the Box, and placing into the Box.

    Name             | Observation Spec                     | Info
    ---------------- | ----------------                     | -------
    **Box-open-v0**  | {get_obs_spec('fetch:Box-open-v0')}  | {{success, dist}}
    **Box-close-v0** | {get_obs_spec('fetch:Box-close-v0')} | {{success, dist}}

    """
    with doc, doc.row() as row:
        render_initial('fetch:Box-open-v0', row)
        render_video('fetch:Box-open-v0', 5, row)

    with doc, doc.row() as row:
        render_initial('fetch:Box-close-v0', row)
        render_video('fetch:Box-close-v0', 5, row)

    doc.flush()
