import requests
import urllib3
import json

print('-----------------Using API---------------------')
urllib3.disable_warnings()
r = requests.get('https://192.168.189.129:8443/1.0',
                 cert=('lxd.crt', 'lxd.key'), verify=False)
print(r.status_code)
print(r.text)
print(r.json()['type'])

r = requests.get('https://192.168.189.129:8443/1.0/containers/myalpine',
                 cert=('lxd.crt', 'lxd.key'), verify=False)
print(r.status_code)
print(r.text)
print(r.json()['metadata']['expanded_devices']['eth0']['parent'])

