import asyncio
from frame_sdk import Frame
from frame_sdk.display import Alignment, PaletteColors
from frame_sdk.camera import Quality, AutofocusType
import datetime
# Add keyboard input library
import keyboard

# Path to the Faster Whisper executable
WHISPER_EXE_PATH = r"C:\Users\bjorn\Downloads\Faster-Whisper-XXL_r239.1_windows\Faster-Whisper-XXL\faster-whisper-xxl.exe"
# Model name for Whisper
WHISPER_MODEL = "large-v3"
# Beam size for Whisper (convert to string for subprocess)
WHISPER_BEAM_SIZE = "5"

async def run_whisper(step: int, timestamp: str):
    print(f"Running whisper for step {step}")
    proc = await asyncio.create_subprocess_exec(
        WHISPER_EXE_PATH,
        f"C:\\proj\\bjornrun\\frame-assistant\\output\\{step}_audio_{timestamp}.wav",
        "--diarize", "pyannote_v3.1",
        "--language", "en",
        "--model", WHISPER_MODEL,
        "--beam_size", str(WHISPER_BEAM_SIZE),  # Ensure it's a string
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
        is_recording = False
        recording_task = None
        
        await f.display.show_text("Press space to start recording...", align=Alignment.MIDDLE_CENTER)
        
        while True:
            if keyboard.is_pressed('space'):
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                if not is_recording:
                    await f.display.show_text("Recording...", align=Alignment.MIDDLE_CENTER)
                    is_recording = True
                recording_task = await f.microphone.save_audio_file(f"output\\{step}_audio_{timestamp}.wav")
                print(f"Audio length: {recording_task} bytes")
                process[step] = asyncio.create_task(run_whisper(step, timestamp))
                step += 1
                await asyncio.sleep(0.3)  # Debounce the spacebar
            else:
                is_recording = False
                await f.display.show_text("Press space to start recording...", align=Alignment.MIDDLE_CENTER)
                
            if keyboard.is_pressed('enter'):
                try:
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    await f.display.show_text("Taking photo...", align=Alignment.MIDDLE_CENTER)
                    photo_data = await f.camera.take_photo(
                        autofocus_seconds=3,
                        quality=Quality.LOW,  # Reduced quality to minimize transfer issues
                        autofocus_type=AutofocusType.CENTER_WEIGHTED
                    )
                    if photo_data:
                        # Save photo data directly to file
                        photo_path = f"output\\{step}_photo_{timestamp}.jpg"
                        with open(photo_path, 'wb') as photo_file:
                            photo_file.write(photo_data)
                        await f.display.show_text("Photo taken!", align=Alignment.MIDDLE_CENTER)
                    else:
                        await f.display.show_text("Photo failed!", align=Alignment.MIDDLE_CENTER)
                    await asyncio.sleep(1)
                    await f.display.show_text("Press space to start recording...", align=Alignment.MIDDLE_CENTER)
                except Exception as e:
                    print(f"Error taking photo: {e}")
                    await f.display.show_text("Error taking photo!", align=Alignment.MIDDLE_CENTER)
                await asyncio.sleep(0.3)  # Debounce the enter key
            
            await asyncio.sleep(0.1)  # Prevent high CPU usage

    print("disconnected")



asyncio.run(main())
