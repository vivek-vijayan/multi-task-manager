__doc__ = '''
Application name : Multi Task Manager
Description: A single standalone application to handle the task running in the system in the app 
Developer: Vivek Vijayan

Date: 19 Oct 2023
Language: PYTHON
'''

# Inbuild Imports:
import os
import sys
import psutil
import tkinter as tk
import time
import datetime
import logging

# Local Imports:
from .mtm_prcs.process import Process

if __name__ == "__main__":
    print("Running the main application")
    _GEN = psutil.process_iter()
    for _E in _GEN:
        print(_E)
