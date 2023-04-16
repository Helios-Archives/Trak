import colorama
import requests
import webbrowser
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

saveResult = True
openResult = False

def parse(text1, text2, text3):
    for i in range(len(text1)):
        if text1[i] != text3[i] and text1[i:i+10] == text2[i:i+10] and not text1[i:i+10] in text3:
            return text1[i:i+50]

existing_account = "https://twitter.com/AFL"
existing_account2 = "https://twitter.com/lilzzzzza"
non_existing_account = "https://twitter.com/478456845673451251345"

r1 = requests.get(existing_account)
r2 = requests.get(existing_account2)
r3 = requests.get(non_existing_account)

colorama.init()
if r1.status_code == 200 and r2.status_code == 200 and r3.status_code == 200:
    print(colorama.Fore.GREEN + 'Success unique account identifier for' + str(existing_account.split('/')[2]) + ' is: ' + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + parse(r1.text, r2.text, r3.text) + colorama.Fore.RESET)
elif r3.status_code == 404:
    print(colorama.Fore.GREEN + 'Non existing account returns 404' + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + 'Enter <html in the variable field' + colorama.Fore.RESET)
else:
    print(colorama.Fore.RED + 'Error occured the existing accounts did not all return valid requests' + colorama.Fore.RESET)
    

# save the output of this script to a file
# and open it in a browser to see the difference

# save the files to the current directory
if saveResult:
    with open('1.html', 'w') as f:
        f.write(str(r1.text.encode('utf-8')))

    with open('2.html', 'w') as f:
        f.write(str(r2.text.encode('utf-8')))

    with open('3.html', 'w') as f:
        f.write(str(r3.text.encode('utf-8')))

# open the files in a browser to see the difference
if openResult:
    filename = os.path.abspath('1.html')
    webbrowser.open('file://' + filename)

    filename = os.path.abspath('2.html')
    webbrowser.open('file://' + filename)