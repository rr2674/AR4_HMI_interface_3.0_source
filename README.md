# AR4-MK1 Version 3 – porting to Raspberry Pi

This project is for **educational purposes** and targeted for Raspberry Pi 5.

```bash
cat /proc/device-tree/model
# Raspberry Pi 5 Model B Rev 1.0
```

This project is a port of existing Windows-based AR4-MK1 Version 3 source code found This project is a port of existing Windows-based AR4-MK1 Version 3 source code found [here](https://anninrobotics.com/downloads/).

This document is a refactor of the original [readme.txt](readme.txt) extracted from the downloaded zip.

---

## Instructions for Installing AR4 Source Code on Raspberry Pi

- Review AR4 source code [video](https://youtu.be/2VGkgCKXVc0 for reference.

### 1. Install Python 3.10.7 or Higher
Depending on your Raspberry Pi image, Python may already be installed. To check which version, run:

```bash
python --version
# or
python3 --version
```

### 2. Open Terminal and navigate to Documents directory

```bash
cd ~/Documents
```

### 3. Clone Source Code

```bash
git clone git@github.com:rr2674/AR4_HMI_interface_3.0_source.git
```

### 4. Create and activate Virtual Environment
Run the following inside the `AR4_HMI_interface_3.0_source` folder:

```bash
cd AR4_HMI_interface_3.0_source
python3 -m venv .venv    # Create virtual environment once
source .venv/bin/activate  # Remember to activate each session
```

### 5. Instll Required modules

```bash
python -m pip install pyserial
python -m pip install inputs
python -m pip install ttkthemes
python -m pip install opencv-python
python -m pip install matplotlib
```

## Instructions for Installing Arduino IDE

Our instructions are a bit different, but you can watch [Install and Run Arduino IDE on Raspberry Pi 5 and Linux Ubuntu](https://www.youtube.com/watch?v=KwOl3wfDB24) for general reference.

1. Download the Linux ARM version of the Arduino IDE from the official Arduino [website](https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE).

   - Inside **Legacy IDE (1.8.19)**, select **Linux ARM 64 bits** and then click the **Download** button.

2. Install the IDE by running the following commands:

   ```bash
   cd ~/Downloads
   tar -xvf arduino-1.8.19-linuxaarch64.tar.xz
   mv arduino-1.8.19 ~/arduino_ide_installer
   cd ~/arduino_ide_installer
   sudo sh install.sh


3. Follow the [Teensyduino core instructions](#instructions-for-installing-teensyduino-core-arduino-ide-1819).

## Instructions for Installing Teensyduino Core (Arduino IDE 1.8.19)

1. Download the Teensyduino installer package.  
   It can be found under the section **“Arduino 1.8.x Software Development”** at this [site](https://www.pjrc.com/teensy/td_download.html).

   - Select **Linux Installer (ARM 64 bit / AARCH64 / Jetson TX2)** and click the **Download** button.

2. Follow the official Linux installation [instructions](https://www.pjrc.com/teensy/td_download.html).

   > **Note:** The Arduino Linux package step (step 2 in the PJRC instructions, as of 2025-09-04) should already been completed per [above](#instructions-for-installing-arduino-ide).  

   > **Note:** During installation, the add-on installer will need to know where the Arduino software is installed.  
   The location will be the full path to:  
   ```bash
   ~/arduino_ide_installer
   ```

3. The Teensy board should now be listed in Arduino IDE.

## Instructions for using AR4 on Raspberry Pi

```bash
source .venv/bin/activate  # only once; at start of session
python3 AR4.py
```

## Additional Port notes

-  Convert Winows icon (.ico) to PNG:

```bash
sudo apt-get install imagemagick
convert AR.ico AR.png
```

-  commands to verify connectiity between Raspberry Pi and Teensyduino

See new USB device when you plug it in:

```bash
dmesg -w
```

