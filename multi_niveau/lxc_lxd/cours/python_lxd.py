#!/usr/bin/python3

from pylxd import Client

client = Client()
print('Un premier conteneur---------')
cont = client.containers.all()
imgs = client.images.all()

for c in cont:
    print(c.name)
    print(c.status)
    print(c.config)

print('==================Les images=======================================')
for img in imgs:
    print(img.fingerprint)

print('==================Création de conteneur=======================================')
config = {
    "name": "oli2",
    "source": {
        "type": "image",
        "certificate": "",
        "fingerprint": "3cea5349712c0678bab52c325e2620cb5a1125152cdaa2965bfc61b8d6eb9f44"
    },
    "instance_type": ""
}

client.containers.create(config, wait=True)
cont_oli2 = client.containers.get('oli2')
print(cont_oli2.config)
cont_oli2.start()




