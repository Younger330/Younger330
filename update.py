import re
import requests
import xml.etree.ElementTree as ET

feed = requests.get('https://somnusyyy.github.io/atom.xml').text
root = ET.fromstring(feed)


## Statistics
![Stats](https://github-readme-stats.vercel.app/api?username=netcan)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=netcan&hide=ipynb,html&layout=compact)
''')
