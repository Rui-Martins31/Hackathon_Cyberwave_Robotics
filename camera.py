from cyberwave import Cyberwave
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()
token = os.getenv("CYBERWAVE_API_KEY")

client = Cyberwave(
    token=token,
)

# Get or create a twin to stream to
twin_uuid = os.getenv("TWIN_ID")

# Create camera streamer
streamer = client.video_stream(
    twin_uuid=twin_uuid,
    camera_id=0,  # Default camera (change if you have multiple cameras)
    fps=10,  # Frames per second, optional
)

async def main():
    try:
        await streamer.start()
        print("Stream is active. Press Ctrl+C to stop...")

        # Keep streaming until interrupted
        while True:
            await asyncio.sleep(1)

    except KeyboardInterrupt:
        print("Stopping stream...")
    except Exception as e:
        print(f"Error during streaming: {e}")
    finally:
        await streamer.stop()
        client.disconnect()
        print("Stream stopped and resources cleaned up")

asyncio.run(main())