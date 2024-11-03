# Home-Automation-with-voice-recognition

Project Summary:
the goal of this prject is to provide a platform for home automation. we have used python 3.13 and arduino IDE to make this project. This project correlates a user given voice command with a a collection of preset voice commands stored in a json file. The code performs correlation and the preset command with the most similarity to the voice command is selected. Each command has a binary string associated with it and if the command is selected, the relevant binary string is sent through the serial monitor to the microcontroller. We have used an ESP-32 DOIT DEVKIT V1, but the code should be compatible with any microcontroller. in addition, the code has features to add voice commands, view the command list and delete unwanted commands. it also has a password protection system to provide security.

Requirements to use the code
  Libraries and softwares to be installed:
    1)Python 3.13
    2)CP210x universal windows driver
    3)Arduino IDE
    4) ESP-32 board (from board manager)
    5)GTTS , playsound , sounddevice , json , serial , time , os , tkinter , numpy , scipy libraries
  Changes to be made
    1) Based on the microcontroller and its pins, modify the output pins in void setup() in the firmware_automation code
    2) In menu.py on lines 10, 78 and 95 and in co_relation.py on line 51, add file path to the json file as saved in your system
    3) Add new voice commands in your json file using the code provided
    4) In security_gui.py, set the password as desired on line 18
