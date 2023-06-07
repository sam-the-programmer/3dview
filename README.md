# 3D-View

This repository contains code for a face-tracking engine that makes the contents of the game engine appear 3D, based off of the position of your eyes. **This is all relative to the webcam, so your camera should be directly below or above your screen.** I.e. the object rendered in the scene appears vaguely 3D. However, this is limited by the FOV of your webcam.

> The parallax effect has only been tested on a Laptop with the webcam at the bottom of the screen, so it works well on laptop but is unknown with an external webcam.

## Install

Clone the whole repository, including the `models` folder and its contents.

Install the dependencies in the terminal.

```shell
pip install -r requirements.txt
```

Run the `main.py` file from the root of the project.

```shell
python main.py
```

## Features

### UI
- Adjust parameters in the UI. Toggle with the blue button.

### In Development
- Loading of custom Blender files for 3D viewing.
- Apple-Vision-Pro-style hand-gestures for moving and turning the object.