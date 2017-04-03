# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 23:56:13 2017

@author: Asus
"""

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#define global vaiables
counter = 0

#define helper functions
def increment():
    global counter
    counter = counter + 1
    
#define event handler functions

def tick():
    increment()
    global counter
    print (counter)

def buttonpress():
    global counter
    counter = 0
    
#create a frame

frame = simplegui.create_frame("simpleGui test",100,100)

# Register event handlers

timer = simplegui.create_timer(1000,tick)
frame.add_button("click me!",buttonpress)

#start frame and timer

frame.start()

timer.start()