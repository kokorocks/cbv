from httpx import get
import import_toml
import json
json_config = import_toml.load_toml_from_parent("config.toml")

r=get(json_config['endpoint']).text
#print(r)

with open('kjv.min.json','w') as f:
    json.dump(json.loads(r),f,indent=2)

i=input('1. gzv translate\n2. oev translate\n3. gtv (new testament only)\n4. exit\nanswer: ')
while i != '4':
    if i == '1':
        import gzv.main
    elif i == '2':
        import oev.main
    elif i == '3':
        import gtv.main
    i=input('\n1. gtv translate\n2. oev translate\n3. gtv (new testament only)\n4. exit\n')

    