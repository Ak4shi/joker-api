import requests
import time

response = requests.request("GET",url="https://japi.eris9.repl.co/api/getframe/?data=https://d2l56h9h5tj8ue.cloudfront.net/images/cards/seijuurou-akashi-2.jpg%20https://raw.githubusercontent.com/Ak4shi/Joker/main/frame.png%20aka.jpg%20frame.png")
time.sleep(5)
print(response.text)