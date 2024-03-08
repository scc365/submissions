from bs4 import BeautifulSoup
import requests
import sys
from pyfiglet import Figlet

if (args_count := len(sys.argv)) != 4:
  print("not enough args")
  print("expect app.py [id] [moodle_cookie] [figlet_font]")
  sys.exit(1)

url = "https://modules.lancaster.ac.uk/mod/assign/view.php?id=" + str(sys.argv[1])
f = Figlet(font=sys.argv[3])

s = requests.Session()
s.cookies.update({'cosign-https-modules.lancaster.ac.uk': sys.argv[2]})
resp = s.get(url)

if resp.status_code != 200:
  print(f.renderText("Failed to get submission data"))

data = resp.text
soup = BeautifulSoup(data, features="html.parser")
result = soup.find_all(string="Submitted")[0].parent.parent.find_all("td")

print(f.renderText("Solutions Submitted: " + result[0].text))
