#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 19:53:39 2018

@author: lab
"""

import time
import subprocess
start = time.time()
prog1 = subprocess.call('perl pal_finder_v0.02.04.pl config_PALfinder.txt',shell = True, cwd = '/mnt/genomes/scripts/pal_finder_v0.02.04')
end = time.time()
print(end-start)