import re
import xml.etree.ElementTree as ET

import requests

feed = requests.get("https://zorchp.github.io/feed.xml").text
root = ET.fromstring(feed)
nsfeed = {"nsfeed": "http://www.w3.org/2005/Atom"}
with open("README.md", "w") as f:
    f.write(
        r"""
```
  _____  _               _____                   _            
  \_   \( )_ __ ___     / _  /  ___   _ __  ___ | |__   _ __  
   / /\/|/| '_ ` _ \    \// /  / _ \ | '__|/ __|| '_ \ | '_ \ 
/\/ /_    | | | | | |    / //\| (_) || |  | (__ | | | || |_) |
\____/    |_| |_| |_|   /____/ \___/ |_|   \___||_| |_|| .__/ 
                                                       |_|    
```
"""
    )

    f.write(
        r"""
## Latest talks
"""
    )
    # talks = requests.get(
    #     "https://raw.githubusercontent.com/zorchp/presentation/master/README.md"
    # ).text
    # for topic, url in re.findall("- (.*): (.*)", talks)[:5]:
    #     f.write("- [{}]({})\n".format(topic, url))

    f.write(
        r"""
## Latest blog posts
"""
    )
    for entry in root.findall("nsfeed:entry", nsfeed)[:5]:
        text = entry.find("nsfeed:title", nsfeed).text
        url = entry.find("nsfeed:link", nsfeed).attrib["href"]
        published = entry.find("nsfeed:published", nsfeed).text[:10]
        f.write("- {} [{}]({})\n".format(published, text, url))

    f.write(
        """
[>>> More blog posts](https://zorchp.github.io/archive/)

## Statistics
![Stats](https://github-readme-stats.vercel.app/api?username=zorchp)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=zorchp&hide=ipynb,html&layout=compact)
"""
    )
