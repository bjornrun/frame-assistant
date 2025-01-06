import asyncio
from frame_sdk import Frame
from frame_sdk.display import Alignment, PaletteColors
from frame_sdk.camera import Quality, AutofocusType
import datetime

# Path to the Faster Whisper executable
WHISPER_EXE_PATH = r"C:\Users\bjorn\Downloads\Faster-Whisper-XXL_r239.1_windows\Faster-Whisper-XXL\faster-whisper-xxl.exe"

async def run_whisper(step: int, timestamp: str):
    print(f"Running whisper for step {step}")
    proc = await asyncio.create_subprocess_exec(
        WHISPER_EXE_PATH,
        f"C:\\proj\\bjornrun\\frame-assistant\\output\\{step}_audio_{timestamp}.wav",
        "--diarize", "pyannote_v3.1",
        "--language", "en",
        "--output_dir", ".\\output\\",
        "--output_format", "txt",
        "--vad_method", "pyannote_v3",
        "--beep_off",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()
    # Optional: Handle output if needed
    # print(f'Whisper output for step {step}: {stdout.decode()}')
    return stdout, stderr

async def main():
    # the with statement handles the connection and disconnection to Frame
    async with Frame() as f:
        # you can access the lower-level bluetooth connection via f.bluetooth, although you shouldn't need to do this often
        print(f"Connected: {f.bluetooth.is_connected()}")

        # let's get the current battery level
        print(f"Frame battery: {await f.get_battery_level()}%")
        f.microphone.bit_depth = 16
        f.microphone.sample_rate = 16000
        step = 0
        process = {}
        await f.display.show_text("Say something...", align=Alignment.MIDDLE_CENTER)
        while True:
            print(f"Step: {step}")
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            # timestamp = "20250106_215344"
            # await f.camera.save_photo(f"output\\{step}_photo_{timestamp}.jpg", autofocus_seconds=3, quality=Quality.MEDIUM, autofocus_type=AutofocusType.CENTER_WEIGHTED)
            # await asyncio.sleep(1)
            length = await f.microphone.save_audio_file(f"output\\{step}_audio_{timestamp}.wav")
            print(f"Audio length: {length} bytes")
            # await f.display.show_text("Transcribing...", align=Alignment.MIDDLE_CENTER)
            await asyncio.sleep(1)
            
            # Execute whisper command asynchronously with additional parameters
            process[step] = asyncio.create_task(run_whisper(step, timestamp))
            # await asyncio.sleep(2)
            step += 1
            
            # Continue with the next iteration

    print("disconnected")



asyncio.run(main())
