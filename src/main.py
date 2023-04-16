import requests
import sys
from tools import *
import time
import colorama

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
colorama.init()
for site in sites.sites:
    try:
        r = requests.get(site[0] + username)
        if r.status_code == 200:
            # check if any of the keywords are on the page or in the html
            for key in site[1]:
                if key in r.text:
                    print('Username found on ' + colorama.Fore.GREEN + site[0] + username + colorama.Fore.RESET)
                    break
                else:
                    time.sleep(1)
                    r = requests.get(site[0] + username)
                    for key in site[1]:
                        if key in r.text:
                            print('Username found on ' + colorama.Fore.GREEN + site[0] + username + colorama.Fore.RESET)
                            break
                    else:
                        print('Username not found on ' + colorama.Fore.RED + site[0] + username + colorama.Fore.RESET)              
        else:
            print('Username not found on ' + colorama.Fore.RED + site[0] + username + colorama.Fore.RESET)    
    except:
        print('Error checking ' + site[0])





