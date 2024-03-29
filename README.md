# Python Pool Game

This was my final project for Physics 77: Introduction to Computational Physics. Credit to Frenly Espino and Darby McCauley as my group partners.

In this playable pool game we set out to model ellastic collisions in 2 Dimensions using Python and the PyGame library. I wrote the physics engine to model the nearly perfect ellastic collisions using vector based object oriented programming. Using principles such as conservation of momentum, conservation of energy, and basic vector operations we were able to succesfully model this physical phenomenon.

As a note to the reader, this code runs far better on Windows operating systems than Mac operating systems. While they both still work, the Mac version refreshes the screen differently and much less efficiently hence the lag in refresh rate. Preferably run this on a Windows platform. It is also important to note that this code uses the PyGame library so if one wants to run this on their computer they have to install the PyGame library first along with Python 3.

To play:

1. Download Repo
2. Install pygame by running `pip install pygame` in your terminal
3. In your terminal run `python main.py` when inside the game directory
4. Move mouse to control stick direction, hold the space bar (~1-3 seconds) to charge up your shot.
5. Have fun playing the game!

To auto sink the balls press `W` and to auto sink the 8 ball, press `Q`. Press in that order for a neat surprise :)

![image info](results/pool_game.gif)
