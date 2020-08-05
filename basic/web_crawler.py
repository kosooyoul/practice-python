import sys
import io
import requests
from bs4 import BeautifulSoup

print('# Start')

# To be able to print Korean(encoding: cp949) on terminal utf-8
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Get web page, and parse html, and find elements
response = requests.get('https://www.google.com/')
document = BeautifulSoup(response.text, 'html.parser')
anchors = document.select('a')

# Print texts of elements
for anchor in anchors:
	print(anchor.get_text())

print('# End')