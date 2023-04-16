import requests
import webbrowser
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

existing_account = "https://snapchat.com/add/teamsnapchat"
non_existing_account = "https://snapchat.com/add/teamsnapchat123"

r1 = requests.get(existing_account)
r2 = requests.get(non_existing_account)

print(r1.status_code, r2.status_code)

# save the output of this script to a file
# and open it in a browser to see the difference

with open('1.html', 'w') as f:
    f.write(str(r1.text.encode('utf-8')))

with open('2.html', 'w') as f:
    f.write(str(r2.text.encode('utf-8')))

# open the files in a browser to see the difference
filename = os.path.abspath('1.html')
webbrowser.open('file://' + filename)

filename = os.path.abspath('2.html')
webbrowser.open('file://' + filename)