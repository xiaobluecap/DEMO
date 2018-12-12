import pickle
import json

d={'url':'index.html','title':'首页','content':'首页'}

with open(r'/dump.txt','wb') as du:
    json.dump(d)
