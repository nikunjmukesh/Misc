# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 01:06:58 2017

@author: Asus
"""

import cx_Freeze

executables = [cx_Freeze.Executable("pygame1.py")]

cx_Freeze.setup(
        name="A bit racey",
        version = "5.0.1",
        options = {"build_exe":{"packages":["pygame"], "include_files":["racecar.png"]}},
        
        executables = executables
        )