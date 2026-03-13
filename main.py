from cyberwave import Cyberwave

import pprint
import time
from dotenv import load_dotenv
import os

# Constants
load_dotenv()
CYBERWAVE_API_KEY: str = os.getenv("CYBERWAVE_API_KEY")
ASSET_KEY: str         = os.getenv("ASSET_KEY")
TWIN_ID: str           = os.getenv("TWIN_ARM_ID")
ENVIRONMENT_ID: str    = os.getenv("ENVIRONMENT_ID")

WORKSPACE_ID:str       = "Rui's Workspace"

print("\n")
 
cw = Cyberwave(api_key=CYBERWAVE_API_KEY)
 
# Connect to SO-101
so_101 = cw.twin(
    ASSET_KEY,
    twin_id        = TWIN_ID,
    environment_id = ENVIRONMENT_ID
)

# DEBUG
# pprint.pprint(cw.workspaces.list())
# pprint.pprint(cw.workspaces.get(WORKSPACE_ID))
# pprint.pprint(cw.projects.list())
# pprint.pprint(cw.assets.list(WORKSPACE_ID))

# Sequence of poses
poses: list[dict[str, float]] = [
    {
        "1": -38.9,
        "2": 45.6,
        "3": 0.0,
        "4": 31.5,
        "5": 0.0,
        "6": 0.0,
    },
    {
        "1": -38.9,
        "2": 0.0,
        "3": 0.0,
        "4": 0.0,
        "5": 0.0,
        "6": 0.0,
    },
    {
        "1": 0.0,
        "2": 0.0,
        "3": 0.0,
        "4": 0.0,
        "5": 0.0,
        "6": 0.0,
    },
    {
        "1": 38.9,
        "2": 0.0,
        "3": 0.0,
        "4": 0.0,
        "5": 0.0,
        "6": 0.0,
    },
    {
        "1": 38.9,
        "2": 45.6,
        "3": 0.0,
        "4": 31.5,
        "5": 0.0,
        "6": 0.0,
    },
]

STEPS: int   = 20    # number of incremental steps between poses
DELAY: float = 0.05  # seconds between each step


def move_to_pose(
    current: dict[str, float],
    target:  dict[str, float],
    steps:   int   = STEPS,
    delay:   float = DELAY,
) -> None:
    for step in range(1, steps + 1):
        t = step / steps
        for joint, target_angle in target.items():
            angle = current[joint] + (target_angle - current[joint]) * t
            so_101.joints.set(joint, angle)
        time.sleep(delay)


# Execute pose sequence
current_pose = {joint: 0.0 for joint in poses[0]}

for pose in poses:
    move_to_pose(current_pose, pose)
    current_pose = pose
