# Frame Assistant: Audio Processing with Brilliant Frame Glasses

## Introduction
This project explores audio processing capabilities using Brilliant Frame glasses, focusing on transcription and speaker diarization. The implementation includes both standalone glasses functionality and integration with external camera setups.

## Technical Overview

### Frame Glasses Implementation
The current implementation utilizes the [Brilliant Labs Python SDK](https://github.com/brilliantlabsAR/frame-sdk-python) for Frame glasses interaction. Key findings include:

- **Hardware Limitations**
  - Simultaneous audio recording and image capture is not supported (yet)
  - Bluetooth data transfer overruns occur during parallel operations
  - Audio is captured as individual WAV files

- **Audio Processing**
  - WAV file quality is sufficient for transcription
  - Compatible with Whisper and Whisper.cpp processing
  - Background transcription during audio recording

### External Camera Setup
Prior to Frame glasses implementation, a high-resolution camera setup was developed:

- **Hardware Components**
  - Logitech BRIO 4K webcam
  - Xeon 6 processor for transcription processing

- **Software Stack**
  - [OBS Studio](https://obsproject.com/) for video capture
  - [SRS (Simple RTMP Server)](https://github.com/ossrs/srs) for streaming
  - [Modified Whisper.cpp](https://github.com/bjornrun/whisper.cpp) with GStreamer support

- **Current Limitations**
  - Speaker Diarization limited to English with Tiny model
  - Planned integration with [Pyannote](https://github.com/pyannote/pyannote-audio) for multilingual support

## Current Implementation

### Frame Assistant Application
A Windows-based Python application ([Frame Assistant](https://github.com/bjornrun/frame-assistant)) has been developed with the following features:

- **Offline Processing**
  - Uses [Whisper Standalone for Windows](https://github.com/Purfview/whisper-standalone-win/releases/tag/Faster-Whisper-XXL)
  - Integrated Pyannote for speaker diarization
  - No internet connection required

- **Performance Features**
  - Background transcription processing
  - Concurrent audio segment recording
  - Real-time processing capabilities

## Future Development

### Planned Enhancements
- Integration of Pyannote for improved multilingual support
- Large model implementation for enhanced accuracy
- Extended speaker diarization capabilities

## Getting Started
For implementation details and setup instructions, please refer to the following resources:
- [Installation Guide](./installation.md)
- [API Documentation](./api-docs.md)
- [Usage Examples](./examples.md)

## Contributing
We welcome contributions to this project. Please see our [Contributing Guidelines](./CONTRIBUTING.md) for more information.

---
*Last Updated: January 2025*
