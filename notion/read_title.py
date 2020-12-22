import json

def read_json(path):
    return json.load(open(path))

from notion.client import NotionClient

data_dic = read_json('./private_infomation.json')
client = NotionClient(token_v2=data_dic['token_v2'])

page = client.get_block('https://www.notion.so/c8cc0391fc2b48189cdf65a9e41b42bc?v=5db6d1bd2a5943f8bc708e3847e3f9dd')
print('# Title :', page.title)
