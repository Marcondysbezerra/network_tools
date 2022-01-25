import json

import requests

ipv_six = requests.get("http://ip.jsontest.com/").text
result = json.loads(ipv_six)
print(result['ip'])


