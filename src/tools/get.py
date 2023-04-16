import requests

existing_account = "http://twitch.tv/necrownyx"
non_existing_account = "http://twitch.tv/654124085703249857"

r1 = requests.get(existing_account)
r2 = requests.get(non_existing_account)

print(r1.text)
for i in range(0, 100): print('.')
print(r2.text)