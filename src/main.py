import requests
from tools import *


# cd to the directory of this file
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# read the settings.cfg file
settings = Settings()
with open('./data/settings.cfg') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line.startswith('#'):
            line = line.split('=')
            line[1] = line[1].split(':')
            print(line)
        

# read the sites.cfg file
with open('./data/sites.cfg') as f:
    pass

