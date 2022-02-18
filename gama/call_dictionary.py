# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 10:31:12 2021

@author: Lenovo
"""

import pickle
import os

path_use = os.getcwd()
path=path_use.replace(os.sep, '/')
path=path + "/" + "dictionary_info.pkl"
sha = pickle.load(open(path, "rb"))