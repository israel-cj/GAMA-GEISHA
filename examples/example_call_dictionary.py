# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 16:58:54 2021

@author: Lenovo
"""
import os
import pickle

path_use = os.getcwd()
path=path_use.replace(os.sep, '/')
path=path + "/" + "dictionary_info.pkl"
sha = pickle.load(open(path, "rb"))