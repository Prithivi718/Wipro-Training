import re
import requests

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")

html = r.text

text = re.findall(r'>([^<>]+)<', html)

cleaned = [t.strip() for t in text if t.strip()]

print(cleaned)