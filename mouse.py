import pynput
from pynput import mouse, keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

import os

def home():
    help_message = '''
    -rm to open the mouse remap menu
        -lb to remap the left mouse button
        -mb to remap the middle mouse button
        -rb to remap the right mouse button
    -reset to reset all current mouse keymappings
    press escape to exit the program
    
    
    '''
    msg = "Mouse and Keyboard Controller"
    print(msg)
    print("Press 'h' for help")
    print("Press 'q' to quit")
    print("Press '-rm' to open the mouse remap menu ")
    letter = input()
    if letter == 'h':
        print(help_message)
    elif letter == 'q'
        os._exit()

    
def remap_menu():
    
    
