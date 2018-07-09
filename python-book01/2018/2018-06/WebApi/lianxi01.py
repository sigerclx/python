import json

m={"a":"123",'b':'jacky'}
n={"a":"123"}

m['a']=n
print(m)


json_str = json.dumps(m,ensure_ascii=False,indent=4)

print(json_str)
