# Frame Development Resources

## Official SDKs
- Frame Python SDK  
  https://github.com/brilliantlabsAR/frame-sdk-python
  - Official Python SDK for Brilliant Frame glasses
  - Note: Currently has limitations with simultaneous audio recording and image capture

## Audio Processing
- Whisper.cpp with GStreamer Support  
  https://github.com/bjornrun/whisper.cpp
  - Modified version of Whisper.cpp
  - Includes GStreamer integration
  - Optimized for Xeon 6 processors

- Pyannote Audio  
  https://github.com/pyannote/pyannote-audio
  - Speaker diarization toolkit
  - Supports multilingual processing
  - Compatible with large language models

- Whisper Standalone for Windows  
  https://github.com/Purfview/whisper-standalone-win/releases/tag/Faster-Whisper-XXL
  - Offline transcription capability
  - Integrated Pyannote support
  - Background processing support

## Streaming and Recording
- OBS Studio  
  https://obsproject.com/
  - Professional broadcasting software
  - Compatible with high-resolution cameras
  - Extensive streaming capabilities

- SRS (Simple RTMP Server)  
  https://github.com/ossrs/srs
  - Lightweight streaming media server
  - RTMP protocol support
  - Integration capabilities with OBS

## Applications
- Frame Assistant  
  https://github.com/bjornrun/frame-assistant
  - Windows-compatible application
  - Offline transcription support
  - Background audio processing
  - Integration with Faster-Whisper-XXL

## Implementation Notes
- Audio processing can be performed offline without internet connectivity
- Speaker diarization is available for multiple languages when using Pyannote
- Background processing enables continuous audio recording and transcription

---
*Last Updated: January 2025*