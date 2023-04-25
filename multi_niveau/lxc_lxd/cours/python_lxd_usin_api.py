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

r = requests.delete('https://192.168.189.129:8443/1.0/containers/oli2',
                    cert=('lxd.crt', 'lxd.key'), verify=False)

print(r.status_code)

payload = {
    "name": "oli3"
}

mydata = json.dumps(payload).encode('utf-8')
r = requests.post('https://192.168.189.129:8443/1.0/containers/oli2',
                  cert=('lxd.crt', 'lxd.key'), verify=False, data=mydata)

print(r.status_code)
print(r.text)

payload = {
    "name": "oli4",
    "source": {
        "type": "image",
        "certificate": "",
        "figerprint": "9e7158fc0683"
    },
    "instance_type": ""
}

mydata = json.dumps(payload).encode('utf-8')
r = requests.post('https://192.168.189.129:8443/1.0/containers',
                  cert=('lxd.crt', 'lxd.key'), verify=False, data=mydata)

print(r.status_code)
print(r.text)

payload = {
    "action": "start"
}

mydata = json.dumps(payload).encode('utf-8')

r = requests.put('https://192.168.189.129:8443/1.0/containers/oli2/state',
                 cert=('lxd.crt', 'lxd.key'), verify=False, data=mydata)

print(r.status_code)
print(r.text)


payload = {
    "command": ["touch", "/tmp/toto.txt"],
    "width": 80,
    "height": 20
}

mydata = json.dumps(payload).encode('utf-8')
r = requests.post('https://192.168.189.129:8443/1.0/containers/oli2/exec',
                  cert=('lxd.crt', 'lxd.key'), verify=False, data=mydata)

print(r.status_code)
print(r.text)