from cyberwave import Cyberwave

import time
from dotenv import load_dotenv
import os

# Constants
load_dotenv()
CYBERWAVE_API_KEY: str = os.getenv("CYBERWAVE_API_KEY")
ASSET_KEY: str         = os.getenv("ASSET_KEY")
TWIN_ID: str           = os.getenv("TWIN_ID")
ENVIRONMENT_ID: str    = os.getenv("ENVIRONMENT_ID")
 
cw = Cyberwave(api_key=CYBERWAVE_API_KEY)
 
# Connect to SO-101
so_101 = cw.twin(
    ASSET_KEY,
    twin_id        = TWIN_ID,
    environment_id = ENVIRONMENT_ID
)

count: int  = 0
degree: int = 0
while count < 10:
    so_101.joints.set("1", degree)

    degree += 10
    count  += 1
    time.sleep(0.1)
