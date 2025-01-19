
# Frame Assistant

Welcome to **Frame Assistant**, a Python-based tool designed to streamline workflows with advanced utilities powered by the Frame SDK and related libraries. This guide will help you set up the project, configure dependencies, and run the assistant on your Windows machine.

---

## Table of Contents

- [Setup Instructions](#setup-instructions)
  - [1. Install Conda](#1-install-conda)
  - [2. Create a Conda Environment](#2-create-a-conda-environment)
  - [3. Install Required Python Packages](#3-install-required-python-packages)
- [Downloading Whisper Standalone](#downloading-whisper-standalone)
- [Run the Project](#run-the-project)
- [Change Whisper Executable Path](#change-whisper-executable-path)
- [Contributing](#contributing)
- [License](#license)

---

## Setup Instructions

### 1. Install Conda

If you don’t already have Conda installed, download and install it from the official [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/) websites. Follow the installation steps for your Windows system.

### 2. Create a Conda Environment

Once Conda is installed, open a terminal (Command Prompt, PowerShell, or Anaconda Prompt) and run the following command to create a new Conda environment:

```bash
conda create -n frame-dev python=3.9
```

This will create an isolated environment named `frame-dev` with Python 3.9.

### 3. Install Required Python Packages

Activate the newly created environment:

```bash
conda activate frame-dev
```

Then install the necessary packages:

```bash
pip install frame-sdk
pip install frame-utilities-for-python
pip install frameutils
pip install keyboard
```

---

## Downloading Whisper Standalone

To use the **Whisper** executable required by this project, download the latest version of the Whisper Standalone for Windows:

1. Visit the [Whisper Standalone Repository](https://github.com/Purfview/whisper-standalone-win).
2. Download the latest release ZIP file for your Windows version.
3. Extract the ZIP file to a location of your choice, such as:

   ```
   C:\Users\bjorn\Downloads\Faster-Whisper-XXL_r239.1_windows
   ```
5. Set the `WHISPER_EXE_PATH` variable in the `main.py` file to the path where you extracted the Whisper Standalone ZIP.
6. Make sure you install CUDA 12 libraries for the Whisper Standalone. https://www.nvidia.com/download/index.aspx?lang=en-us
---

## Run the Project

After setting up the Conda environment and downloading Whisper Standalone, follow these steps:

1. Activate the Conda environment:

```bash
conda activate frame-dev
```

2. Run the project using the following command:

```bash
python .\main.py
```

---

## Change Whisper Executable Path

The path to the Whisper executable is defined on **line 8** of the `main.py` file. Update the value of the `WHISPER_EXE_PATH` variable to match the path where you extracted the Whisper Standalone ZIP.

For example:

```python
WHISPER_EXE_PATH = r"C:\Users\bjorn\Downloads\Faster-Whisper-XXL_r239.1_windows\Faster-Whisper-XXL\faster-whisper-xxl.exe"
```

Ensure the path matches your system setup.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you'd like to improve this project.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

