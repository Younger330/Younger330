import re
import requests
import xml.etree.ElementTree as ET

feed = requests.get('https://somnusyyy.github.io/atom.xml').text
root = ET.fromstring(feed)

with open('README.md', 'w') as f:
    f.write(r'''
    ```
 _          _ _                            _     _ 
| |__   ___| | | ___   __      _____  _ __| | __| |
| '_ \ / _ | | |/ _ \  \ \ /\ / / _ \| '__| |/ _` |
| | | |  __| | | (_) |  \ V  V | (_) | |  | | (_| |
|_| |_|\___|_|_|\___/    \_/\_/ \___/|_|  |_|\__,_|
                                                   

* 1999
* Skills: C/Java/Python
* Interests: OS, Coding
```
''')
    
f.write('''


## Statistics
![Stats](https://github-readme-stats.vercel.app/api?username=somnusyyy)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=somnusyyy&hide=ipynb,html&layout=compact)
''')
