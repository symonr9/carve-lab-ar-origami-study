import viz # general viz module
import vizinfo # vizinfo is used along w/ vizinput to gather input throughout the program 
import vizshape # vizshape is used for the creation and manipulation of the box sensors and tiles. 
import math # vizmath is used for various mathematical operations used in the program.
import viztask
import vizproximity # vizproximity is used for the creation and function of all proximity sensors.
import vizinput # vizinput is used along w/ vizinfo to gather input throughout the program 
import vizconnect # Vizconnect is used for tracking the position and orientation of the head and hand. 
import hand # (From fitz test) Kept in case it was needed.
import random # Used to cycle test list.
import time	# Used for its CPU clock time function
import os.path #used to check file I/O
import VideoVision
import vizdlg
import win32api
import win32con
from threading import Timer

from config import * 

viz.go();
