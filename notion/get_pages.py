import json
def read_json(path):
    return json.load(open(path))

from notion.client import NotionClient

data_dic = read_json('./private_infomation.json')
client = NotionClient(token_v2=data_dic['token_v2'])

page = client.get_block('https://www.notion.so/Speaking-Correction-eb9e81ebd7ac4e7a845580b39eba6efe')
print('# Title :', page.title)

for child in page.children:
    print(child, 'https://www.notion.so/{}'.format(child.id.replace('-', '')))
