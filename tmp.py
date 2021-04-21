import ujson as json
from tqdm import tqdm

all_relations = ['CausesDesire', 'CreatedBy', 'DefinedAs', 'HasA', 'HasProperty', 'HasFirstSubevent',
                 'InstanceOf', 'ReceivesAction', 'UsedFor']
overall_dict = dict()
for r in all_relations:
    print('We are working on:', r)
    with open('prediction/' + r + '.json', 'r') as f:
        tmp_dict = json.load(f)
    for tmp_k in tqdm(tmp_dict):
        tmp_head = tmp_k.split('$$')[0]
        tmp_tail = tmp_k.split('$$')[1]
        new_k = tmp_head + '$$' + r + '$$' + tmp_tail
        overall_dict[new_k] = tmp_dict[tmp_k]

sorted_result = sorted(overall_dict, key=lambda x: overall_dict[x], reverse=True)
with open('prediction/TransOMCS.txt', 'w') as f:
    for tmp_k in sorted_result:
        f.write(tmp_k.split('$$')[0])
        f.write('\t')
        f.write(tmp_k.split('$$')[1])
        f.write('\t')
        f.write(tmp_k.split('$$')[2])
        f.write('\t')
        f.write(str(overall_dict[tmp_k]))
        f.write('\n')

print('end')