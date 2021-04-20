import ujson as json

with open("./Data/gen/extracted_knowledge/UsedFor.json", 'r') as f:
    all = json.load(f)

print(len(all))

tmp = list()
count = 0
for i, item in enumerate(all):
    tmp.append(item)
    if i % 400 == 399:
        with open("./Data/gen/extracted_knowledge/UsedFor"+ str(count) +".json", 'w') as f:
            json.dump(tmp, f)
        count += 1
        tmp = list()
if len(tmp) != 0:
    with open("./Data/gen/extracted_knowledge/UsedFor"+ str(count) +".json", 'w') as f:
        json.dump(tmp, f)

