from cyberwave import Cyberwave

# Constants
CYBERWAVE_API_KEY: str = "6aa0fc00-971b-4ebf-bb96-de1e2a0fac8c"
 
cw = Cyberwave(api_key=CYBERWAVE_API_KEY)
 
# Connect to SO-101
so_101 = cw.twin(
    "the-robot-studio/so101",
    twin_id="fbee3ee1-d9e0-4eb1-b9b5-59b80ef0ff58",
    environment_id="759af6d6-9fc4-4739-9b06-d4897cb6a79b"
)


# Move and rotate in the studio
# so_101.edit_position(x=1, y=0, z=0.5)
# so_101.edit_rotation(yaw=90)  # degrees
 
# Joint control
so_101.joints.arm_joint = 45  # degrees
list_joints: list = so_101.joints.list()
print(f"{list_joints = }")

so_101.joints

# so_101.joints.set(joint_name="arm_joint", )


###


# # Pose example (keyframe: "release near/half")
# twin = cw.twins.get("fbee3ee1-d9e0-4eb1-b9b5-59b80ef0ff58")

# twin.motion.asset.pose(
#     "release near/half",
#     transition_ms=800,
#     environment_uuid="759af6d6-9fc4-4739-9b06-d4897cb6a79b"
# )