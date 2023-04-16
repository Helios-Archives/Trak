import requests
import sys
from tools import *

try: username = sys.argv[1]; print('Username: ' + username)
except: username = input('Username: ')

# cd to the directory of this file
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# read the cfg files
settings = Settings('./data/settings.cfg')
sites = Sites('./data/sites.cfg')
sites.removeSites(settings.exclude)

print(sites.sites)
# get the list of sites to check
for site in sites.sites:
    print('Checking ' + site[0] + username)
    try:
        r = requests.get(site[0] + username)
        if r.status_code == 200:
            # check if any of the keywords are on the page or in the html
            for key in site[1]:
                if key in r.text:
                    print('Username found on ' + site[0])
                    break
                else:
                    for key in site[1]:
                        if key in r.text:
                            print('Username found on ' + site[0])
                            break
                        else:
                            for key in site[1]:
                                if key in r.text:
                                    print('Username found on ' + site[0])
                                    break
                                else:
                                    print('Username not found on ' + site[0])
        else:
            print('Username not found on ' + site[0])
    except:
        print('Error checking ' + site[0])





