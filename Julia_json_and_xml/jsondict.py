import json
 
dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
 
json = json.dumps(dict)
f = open("dict.json","w")
f.write(json)
f.close()
with open('dict.json', 'r') as fp:
    dict = json.load(fp)