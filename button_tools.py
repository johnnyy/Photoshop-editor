
import sys

import cv2
import tkinter
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from  PIL import Image,ImageTk
import matplotlib.pyplot as plt
import numpy as np
import os


def pencil_button(button_pencil, button_ant):
    if (button_ant is 'None'):
        pass
    else:
        button_ant.config(highlightbackground='white')
    button_pencil.config(highlightbackground='black')
    
def command_pencil(image,x1,y1,x2,y2,color,linethickness):
    return cv2.line(image,(x1,y1),(x2,y2), color, linethickness)

def button(button, button_ant):

    if (button_ant is 'None'):
        pass
    else:
        button_ant.config(highlightbackground='white')
    if(button is 'None'):
        pass
    else:

        button.config(highlightbackground='black')

