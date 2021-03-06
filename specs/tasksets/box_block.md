
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
**Box-fixed-open-v0**         | achieved_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;lid: (3,)<br>desired_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;lid: (3,)<br>observation: (43,)         | box fixed on the side<br>lift lid.<br>**object target tracks object** | ![](figures/Box-fixed-open-v0.gif)
**Box-fixed-close-v0**        | achieved_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;lid: (3,)<br>desired_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;lid: (3,)<br>observation: (43,)        | box fixed on the side<br>close lid.<br>**object target tracks**.  | ![](figures/Box-fixed-close-v0.gif)
**Box-fixed-place-easy-v0**   | achieved_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>desired_goal:<br>&nbsp;&nbsp;&nbsp;&nbsp;object0: (3,)<br>observation: (43,)   | box is open and fixed<br>place into the box<br>**lid target trakcs**. | ![](figures/Box-fixed-place-easy-v0.gif)
**Complex Tasks**             |                                             |                                                             | 
**Box-fixed-place-medium-v0** | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (43,) | Place both the lid and<br>the object to the target location | ![](figures/Box-fixed-place-medium-v0.gif)
**Box-fixed-place-v0**        | achieved_goal: (6,)<br>desired_goal: (6,)<br>observation: (43,)        | place the lid back after<br>placing the object.   | ![](figures/Box-fixed-place-v0.gif)

## Details of Each Task

```python
box_envs = [
    "fetch:Box-fixed-open-v0",
    "fetch:Box-fixed-close-v0",
    "fetch:Box-fixed-place-easy-v0",
    "fetch:Box-fixed-place-medium-v0",
    "fetch:Box-fixed-place-v0", ]
```
| **Box-fixed-open-v0** | **distribution** |   |
|:---------------------:|:----------------:|:-:|
| ![figures/Box-fixed-open-v0_init.png?ts=657064](figures/Box-fixed-open-v0_init.png?ts=657064) | ![figures/Box-fixed-open-v0_reset.png?ts=817517](figures/Box-fixed-open-v0_reset.png?ts=817517) | ![figures/Box-fixed-open-v0.gif?ts=681189](figures/Box-fixed-open-v0.gif?ts=681189) |
| **Box-fixed-close-v0** | **distribution** |   |
| ![figures/Box-fixed-close-v0_init.png?ts=338959](figures/Box-fixed-close-v0_init.png?ts=338959) | ![figures/Box-fixed-close-v0_reset.png?ts=394865](figures/Box-fixed-close-v0_reset.png?ts=394865) | ![figures/Box-fixed-close-v0.gif?ts=114687](figures/Box-fixed-close-v0.gif?ts=114687) |
| **Box-fixed-place-easy-v0** | **distribution** |   |
| ![figures/Box-fixed-place-easy-v0_init.png?ts=720561](figures/Box-fixed-place-easy-v0_init.png?ts=720561) | ![figures/Box-fixed-place-easy-v0_reset.png?ts=789205](figures/Box-fixed-place-easy-v0_reset.png?ts=789205) | ![figures/Box-fixed-place-easy-v0.gif?ts=450425](figures/Box-fixed-place-easy-v0.gif?ts=450425) |
| **Box-fixed-place-medium-v0** | **distribution** |   |
| ![figures/Box-fixed-place-medium-v0_init.png?ts=010486](figures/Box-fixed-place-medium-v0_init.png?ts=010486) | ![figures/Box-fixed-place-medium-v0_reset.png?ts=070622](figures/Box-fixed-place-medium-v0_reset.png?ts=070622) | ![figures/Box-fixed-place-medium-v0.gif?ts=829206](figures/Box-fixed-place-medium-v0.gif?ts=829206) |
| **Box-fixed-place-v0** | **distribution** |   |
| ![figures/Box-fixed-place-v0_init.png?ts=568802](figures/Box-fixed-place-v0_init.png?ts=568802) | ![figures/Box-fixed-place-v0_reset.png?ts=636770](figures/Box-fixed-place-v0_reset.png?ts=636770) | ![figures/Box-fixed-place-v0.gif?ts=471702](figures/Box-fixed-place-v0.gif?ts=471702) |
