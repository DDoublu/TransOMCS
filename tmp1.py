import ujson as json

r = "ReceivesAction"  # UsedFor ReceivesAction

with open("./Data/gen/extracted_knowledge/" + r + ".json", 'r') as f:
    all = json.load(f)

print(len(all))

tmp = list()
# count = 0
for i, item in enumerate(all):
    if i in [16]:
        continue
    tmp.append(item)
    # if i % 400 == 399:
    #     with open("./Data/gen/extracted_knowledge/" + r + str(count) + ".json", 'w') as f:
    #         json.dump(tmp, f)
    #     count += 1
    #     tmp = list()
if len(tmp) != 0:
    with open("./Data/gen/extracted_knowledge/" + r + "_post.json", 'w') as f:
        json.dump(tmp, f)





