import json

with open("sample-data.json", "r") as read_file:
    data = json.load(read_file)
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")
'''''
for i, k in data["imdata"][0]['l1PhysIf']["attributes"].items():
        if i == 'dn':
            print(k, end="                               ")
        if i == "speed":
            print(k, end="    ")
        if i == "mtu":
            print(k, end="    ")
'''''
x = data["imdata"][0]['l1PhysIf']["attributes"]['dn']
y = data["imdata"][0]['l1PhysIf']["attributes"]["speed"]
z = data["imdata"][0]['l1PhysIf']["attributes"]["mtu"]
print(x + "                               " + y + "  " + z)
x = data["imdata"][1]['l1PhysIf']["attributes"]['dn']
y = data["imdata"][1]['l1PhysIf']["attributes"]["speed"]
z = data["imdata"][1]['l1PhysIf']["attributes"]["mtu"]
print(x + "                               " + y + "  " + z)
x = data["imdata"][2]['l1PhysIf']["attributes"]['dn']
y = data["imdata"][2]['l1PhysIf']["attributes"]["speed"]
z = data["imdata"][2]['l1PhysIf']["attributes"]["mtu"]
print(x + "                               " + y + "  " + z)

