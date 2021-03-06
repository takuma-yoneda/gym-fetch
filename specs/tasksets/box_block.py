from cmx import doc

from specs.__init__ import get_obs_spec, render_initial, render_video

if __name__ == '__main__':
    doc @ f"""
    write_protected: true
    ---
    # Latent Planning Task Suite

    This task suite includes two sets of tasks: **box open and place**, **twin box pick and place**. 
    Each task set is composed of a few manipulation primitives, and one (or a few) complex tasks
    that require stitching together the primitives in order to succeed. The goal space is composed
    of multiple objects, for example both a goal location for the object and the lid. The original 
    hindsight experience replay has trouble with learning these complex tasks.


    Primitive Tasks               | Observation Spec                            | Goal Init/Comment                   | 
    -----------------             | ----------------                            | -------                             | ------
    **Box-fixed-open-v0**         | {get_obs_spec('Box-fixed-open-v0')}         | box fixed on the side<br>lift lid.<br>**object target tracks object** | ![](figures/Box-fixed-open-v0.gif)
    **Box-fixed-close-v0**        | {get_obs_spec('Box-fixed-close-v0')}        | box fixed on the side<br>close lid.<br>**object target tracks**.  | ![](figures/Box-fixed-close-v0.gif)
    **Box-fixed-place-easy-v0**   | {get_obs_spec('Box-fixed-place-easy-v0')}   | box is open and fixed<br>place into the box<br>**lid target trakcs**. | ![](figures/Box-fixed-place-easy-v0.gif)
    **Complex Tasks**             |                                             |                                                             | 
    **Box-fixed-place-medium-v0** | {get_obs_spec('Box-fixed-place-medium-v0')} | Place both the lid and<br>the object to the target location | ![](figures/Box-fixed-place-medium-v0.gif)
    **Box-fixed-place-v0**        | {get_obs_spec('Box-fixed-place-v0')}        | place the lid back after<br>placing the object.   | ![](figures/Box-fixed-place-v0.gif)

    ## Details of Each Task
    """
    with doc:
        box_envs = [
            "fetch:Box-fixed-open-v0",
            "fetch:Box-fixed-close-v0",
            "fetch:Box-fixed-place-easy-v0",
            "fetch:Box-fixed-place-medium-v0",
            "fetch:Box-fixed-place-v0", ]

    table = doc.table()
    for env_id in box_envs:
        with table.figure_row() as row:
            render_initial(env_id, row)
            render_video(env_id, 15, row)

    doc.flush()
