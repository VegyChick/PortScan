#!/usr/bin/env python
#! -*- coding:utf-8 -*-

import ctypes
from ctypes import *

lib = cdll.LoadLibrary(u'./scan.so')
lib.Scan.restype = ctypes.c_char_p
result = lib.Scan("117.51.1.11","1-65534","eth0")
print result.split(" ")