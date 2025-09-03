# AR4-MK1 Version 3 – Raspberry Pi Port

This project is for **educational purposes**.

This project is a port of existing Windows-based AR4-MK1 Version 3 source code found This project is a port of existing Windows-based AR4-MK1 Version 3 source code found [here](https://anninrobotics.com/downloads/).

This document is a refactor of the original [readme.txt](readme.txt) extracted from the downloaded zip.

---

## Instructions for Installing AR4 Source Code on Raspberry Pi

- Review source code video: [https://youtu.be/2VGkgCKXVc0](https://youtu.be/2VGkgCKXVc0)

### 1. Install Python 3.10.7 or Higher
Depending on your Raspberry Pi image, Python may already be installed. To check, run:

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

## Instructions for using AR4 on Raspberry Pi

## Additional Port notes

-  Convert Winows icon (.ico) to PNG:

```bash
sudo apt-get install imagemagick
convert AR.ico AR.png
```