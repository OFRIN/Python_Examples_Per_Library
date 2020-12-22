import json

def read_json(path):
    return json.load(open(path))

from notion.client import NotionClient

data_dic = read_json('./private_infomation.json')
client = NotionClient(token_v2=data_dic['token_v2'])

# cv = client.get_collection_view('https://www.notion.so/c8cc0391fc2b48189cdf65a9e41b42bc?v=5db6d1bd2a5943f8bc708e3847e3f9dd')
collection = client.get_block('https://www.notion.so/c8cc0391fc2b48189cdf65a9e41b42bc?v=5db6d1bd2a5943f8bc708e3847e3f9dd').collection

for row in collection.get_rows():
    if row.status == 'Word':
        print('| %50s | %50s | %20s |'%(row.title, row.meaning, row.status))

