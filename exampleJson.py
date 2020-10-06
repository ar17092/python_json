import urllib.request, json

url="http://localhost:8080/index"

response= urllib.request.urlopen(url).read()

data = json.loads(response)

print(json.dumps(data, indent=4))

print("Nombre:",data["Nombre"],"\nLugar de estudio:",json.dumps(data['educacion'], indent=4))
