## Introduction

This is an UI designed for the rebox algorithm (label and bounding box correction). The algorithm generates a new directory of corrected labels, boxes them and generates a video from the boxed images. Go to the Documentation tab to see how the configs work. Check out the Updates tab to see what has been updated for both the underlying algorithm and the UI. See the more detailed explanation of the algorithm in the About tab.


### NOTE:
- Project folder must consist of both images and labels subfolder (Must be called images and labels)
- classes.txt is optional in labels folder
- When running script, it may take more than a few seconds for the first output to be shown. Still looking for a way to show output with 0 buffer after making the algorithm run in a screen.
- Although the resolutions of the image is automatically found in the algorithm, you still need to fill them in the configs (subject to change)
- Documentation may not be up to date


**Usage:**
- Understand each config, (Config explanation is currently in the home page)
- Go to the Configs page, fill the configs, choose a project folder, name the generated video
- Go to the Script page, run the script and see real-time console logs of the process
- After the script finished running, go to the Images and Videos page to check out the result


### Requirements
- install dependencies: ```pip install -r requirements.txt```
- run main.py