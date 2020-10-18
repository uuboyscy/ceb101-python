import json

with open('tmp.json', 'r') as f:
    tmpstr = f.read()
    data = json.loads(tmpstr)

print(data['test'])
print(data)
dataStr = json.dumps(data)
print(dataStr)
