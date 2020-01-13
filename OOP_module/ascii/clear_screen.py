#!/usr/bin/env python3
"""
Use for clear console . We use this in our game to clean ASCII from previous scene.
"""
import platform    # For getting the operating system name
import subprocess  # For executing a shell command


def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command = "cls" if platform.system().lower() == "windows" else "clear"

    # Action
    return subprocess.call(command) == 0


clear_screen()
