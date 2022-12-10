# Skyfire

By Helaman Chan 

Email: johnhelaman10@gmail.com

For BYU Idaho CSE 210 - Programming with Classes, Fall 2022

## Description
Debris are falling down the sky and you must shoot them. Be careful not to get hit by them though!

## Controls
* Left and Right arrow keys (or the A and D keys) to move your character to left or right. 
* Space bar to fire a missile.

## Getting Started

Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

```
python3 -m pip install raylib

```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.

```
python3 skyfire
```

Alternatively, you can use Visual Studio Code and start the game by running the "__main.py__" program. (Make sure you are using a python version that has Raylib installed or else it will not work)

## Requirements

* Python 3.8.0 or any version above.
* Raylib Python CFFI 3.7

## Project Structure

```
root                    
+-- skyfire                
  +-- game              
  +-- __main__.py       
+-- README.md          
```

## Bugs and Imperfections

This game is more of an early build, or a proof of concept and an exercise rather than an actual game so please bear in mind of the things that are still need to be fixed. Examples include: 

* Both the debris and missile move very slowly since increasing the velocity makes it less likely that the hits will be registered.
* The player can only fire one missile at a time, and every time the player fires their weapon, the missile returns to the player's position.
* Sometimes the missile would not destroy an object even when colliding with it.
* The missile does not disappear after hitting an object. I tried using the remove_actor method but it wouldn't work
* When the missile isn't fired, it stays at the top left portion of the screen, beside the banner.
